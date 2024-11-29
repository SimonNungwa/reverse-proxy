# Reverse Proxy Library

A lightweight, reusable Python library for creating a reverse proxy to forward requests from a frontend to a backend server. This proxy supports all HTTP methods and is built using **FastAPI** and **httpx**.

---

## Features

- **HTTP Method Support**: Supports `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, and `OPTIONS`.
- **Request Forwarding**: Forwards headers, query parameters, and body to the target server.
- **Asynchronous**: Uses `httpx.AsyncClient` for fast, non-blocking communication.
- **Easy to Use**: Simple setup and modular design for reuse in different projects.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/reverse-proxy.git
   cd reverse-proxy
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Optionally, install as a package:
   ```bash
   pip install .
   ```

---

## Usage

### Import the Library
```python
from reverse_proxy import ReverseProxy
import uvicorn

# Target backend URL
TARGET_URL = "http://127.0.0.1:8001"

# Initialize the reverse proxy
proxy = ReverseProxy(target_url=TARGET_URL)

# Start the proxy server
if __name__ == "__main__":
    uvicorn.run(proxy.get_app(), host="127.0.0.1", port=8000)
```

This example forwards all requests from `http://127.0.0.1:8000` to the target backend `http://127.0.0.1:8001`.

### Customizing the Proxy
You can modify the `ReverseProxy` class to add custom logic for request processing, authentication, or logging.

---

## Example Project

1. Start a backend server (e.g., with FastAPI or Flask) on `http://127.0.0.1:8001`.
2. Run the proxy server:
   ```bash
   python main.py
   ```
3. Make requests to the proxy at `http://127.0.0.1:8000`.

---

## Dependencies

- `fastapi`
- `httpx`
- `uvicorn`

Install all dependencies with:
```bash
pip install fastapi httpx uvicorn
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

