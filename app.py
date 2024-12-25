# app.py
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Basit bir HTTP sunucu oluştur
def run(server_class=TCPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)  # Sunucu 8000 portunda çalışacak
    httpd = server_class(server_address, handler_class)
    print('Sunucu başlatıldı, 8000 portunu dinliyor...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
