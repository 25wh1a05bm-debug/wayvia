#!/usr/bin/env python3
"""
WAYVIA Web Application Server
Lightweight HTTP server serving WAYVIA with clean MIME types and CORS support.
"""

import http.server
import socketserver
import os
import sys

PORT = 5173
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.js'):
            return 'application/javascript'
        if path.endswith('.css'):
            return 'text/css'
        if path.endswith('.svg'):
            return 'image/svg+xml'
        return super().guess_type(path)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def run():
    port = PORT
    for attempt in range(5):
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print("==================================================")
                print("[*] WAYVIA Web Application Server Running")
                print(f"[*] Local URL: http://localhost:{port}")
                print(f"[*] Directory: {DIRECTORY}")
                print("==================================================")
                sys.stdout.flush()
                httpd.serve_forever()
        except OSError as e:
            if attempt < 4:
                port += 1
            else:
                raise e

if __name__ == "__main__":
    run()
