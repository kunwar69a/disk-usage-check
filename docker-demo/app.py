from http.server import BaseHTTPRequestHandler, HTTPServer
import os

MESSAGE = os.getenv("APP_MESSAGE", "Hello from my Docker app!")
PORT = int(os.getenv("PORT", "8080"))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"healthy")
            return

        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(MESSAGE.encode())
            return

        self.send_error(404, "Not found")


server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"Listening on port {PORT}")
server.serve_forever()