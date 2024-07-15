from http.server import BaseHTTPRequestHandler
import requests, random, traceback

def generate_version():
  ver = []
  for i in range(random.randint(1, 3)):
    ver.append(str(random.randint(100, 999)))
  return '.'.join(ver)

def create_header():
  moz = random.randint(3, 5)
  android = random.randint(10, 14)
  ver = random.randint(3, 5)
  return { 'User-Agent': f'Mozilla/{moz}.0 (Linux; Android {android}; K) AppleWebKit/{generate_version()} (KHTML, like Gecko) Version/{ver}.0 Chrome/{generate_version()} Mobile Safari/{generate_version()}' }

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    result = None
    try:
      req = requests.get('https:/' + self.path, headers=create_header())
      self.send_response(200)
      result = req.text
    except:
      e = traceback.format_exc()
      self.send_response(500)
      result = str(e)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    self.wfile.write(result.encode('utf-8'))