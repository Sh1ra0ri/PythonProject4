import http.server
import requests

PORT = 8000
HTML_URL = "https://raw.githubusercontent.com/Sh1ra0ri/PythonProject4/main/contacts.html"

# Загружаем HTML
HTML = requests.get(HTML_URL).text

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):  # ← ОБЯЗАТЕЛЬНО do_GET (с большой G и E)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

# noinspection PyTypeChecker
http.server.ThreadingHTTPServer(("", PORT), Handler).serve_forever()