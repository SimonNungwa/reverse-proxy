from flask import Flask, render_template, request, Response
import httpx

app = Flask(__name__)

# Configuration for the target server
TARGET_SERVER = "https://example.com"  # Replace with the URL you want to proxy to


@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def reverse_proxy(path):
    try:
        # Construct the target URL
        target_url = f"{TARGET_SERVER}/{path}"

        # Capture the incoming request data
        headers = dict(request.headers)
        data = request.get_data() if request.method in ("POST", "PUT", "PATCH") else None
        params = request.args

        # Forward the request to the target server using httpx
        with httpx.Client() as client:
            response = client.request(
                method=request.method,
                url=target_url,
                headers=headers,
                params=params,
                content=data
            )

        # Construct the response to return to the client
        proxied_response = Response(
            response.content,
            status=response.status_code,
            headers=dict(response.headers),
        )

        return proxied_response
    except Exception as e:
        return f"An error occurred: {e}", 500


class HandleRequest:
    def __init__(self, target_server):
        self.target_server = target_server

    def proxy(self, path, method, headers, params=None, data=None):
        """Handles the proxy logic."""
        url = f"{self.target_server}/{path}"
        with httpx.Client() as client:
            response = client.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                content=data,
            )
        return response


# To use the HandleRequest class
# handle_request = HandleRequest(TARGET_SERVER)
