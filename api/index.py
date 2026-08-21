from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>TikTok OSINT - Tahap 1</title>
        </head>
        <body>
            <h1>✅ Server Python berhasil jalan!</h1>
            <p>Ini adalah halaman utama.</p>
            <p>API Health: <a href="/api/health">/api/health</a></p>
        </body>
        </html>
        ''')
        return

# Untuk endpoint /api/health kita buat juga
# Tapi karena handler hanya untuk GET, kita bisa parsing path
