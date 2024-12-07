from flask import Flask, request, Response
import httpx
from itertools import cycle

app = Flask(__name__)

# List of backend servers to balance the load
BACKEND_SERVERS = [
    "http://backend1.example.com",
    "http://backend2.example.com",
    "http://backend3.example.com",
]

# Cycle through servers for round-robin load balancing
server_pool = cycle(BACKEND_SERVERS)


@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def load_balancer(path):
    try:
        # Select the next backend server
        target_server = next(server_pool)
        target_url = f"{target_server}/{path}"

        # Forward the incoming request
        headers = dict(request.headers)
        data = request.get_data() if request.method in ("POST", "PUT", "PATCH") else None
        params = request.args

        with httpx.Client() as client:
            response = client.request(
                method=request.method,
                url=target_url,
                headers=headers,
                params=params,
                content=data,
            )

        # Construct the response to send back to the client
        proxied_response = Response(
            response.content,
            status=response.status_code,
            headers=dict(response.headers),
        )

        return proxied_response
    except Exception as e:
        return f"An error occurred while balancing the load: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
