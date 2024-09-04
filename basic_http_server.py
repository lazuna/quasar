from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000
server_address = ('', PORT)

httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"Serving on port {PORT}...")
httpd.serve_forever()
