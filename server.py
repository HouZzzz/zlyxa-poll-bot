from http.server import BaseHTTPRequestHandler, HTTPServer

#just for vercel
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = 'Hello, world!'
        self.wfile.write(bytes(message, 'utf8'))