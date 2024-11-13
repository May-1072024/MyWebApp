import http.server
import socketserver
import os

# Define the port and the directory to serve
PORT = 8000
DIRECTORY = "webapp"

class CustomHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Set up the server
with socketserver.TCPServer(("", PORT), CustomHttpRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server.")
        httpd.shutdown()
