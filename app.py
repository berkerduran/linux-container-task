from http.server import BaseHTTPRequestHandler, HTTPServer

# Basit bir HTTP istek işleyicisi
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Yanıt başlıkları
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Yanıt içeriği (str.encode() kullanarak HTML içeriğini bytes'a dönüştür)
        self.wfile.write("<html><body><h1>Merhaba, dunya !</h1></body></html>".encode('utf-8'))

# Sunucu ayarları
def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)  # Sunucu 8000 portunda çalışacak
    httpd = server_class(server_address, handler_class)
    print('Sunucu başlatıldı, 8000 portunu dinliyor...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
