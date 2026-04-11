from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello DevOps! This is Deepthi's app!")

server = HTTPServer(("0.0.0.0", 8000), MyHandler)
print("Server running on port 8000...")
server.serve_forever()
