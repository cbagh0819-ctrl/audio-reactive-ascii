import http.server
import os
import sys
import webbrowser
import socket

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class DualStackServer(http.server.ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = True

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Prevent browser caching of index.html
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")
        sys.stdout.flush()

def find_available_port(start_port=8000, max_attempts=10):
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(('127.0.0.1', port))
                return port
            except OSError:
                continue
    return start_port

def main():
    port = find_available_port(PORT)
    server_address = ('127.0.0.1', port)
    
    with DualStackServer(server_address, CustomHandler) as httpd:
        url = f"http://127.0.0.1:{port}"
        print(f"\n=======================================================")
        print(f"  CYBER-ASCII ENGINE SERVER ONLINE")
        print(f"  URL: {url}")
        print(f"  Directory: {DIRECTORY}")
        print(f"  Mode: Multi-threaded ThreadingHTTPServer")
        print(f"  Press Ctrl+C to stop.")
        print(f"=======================================================\n")
        
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == '__main__':
    main()
