from http.server import BaseHTTPRequestHandler
import requests, json, random, string, traceback

def generate_version():
  ver = []
  for i in range(random.randint(1, 3)):
    ver.append(str(random.randint(100, 999)))
  return '.'.join(ver)

def generate_model():
  name = ''
  for i in range(3):
    name += random.choice(string.ascii_uppercase)
  name += str(random.randint(100, 999))
  return name

def create_header():
  moz = random.randint(3, 5)
  android = random.randint(10, 14)
  ver = random.randint(3, 5)
  return { 'User-Agent': f'Mozilla/{moz}.0 (Linux; Android {android}; {generate_model()}) AppleWebKit/{generate_version()} (KHTML, like Gecko) Version/{ver}.0 Chrome/{generate_version()} Mobile Safari/{generate_version()}' }

def fetch_proxy():
  req = requests.get('http://pubproxy.com/api/proxy?speed=1&https=true')
  ip = req.json()['data'][0]['ip']
  return { 'https': [ip] }

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    result = None
    try:
      req = requests.get('https:/' + self.path, proxies=fetch_proxy(), headers=create_header())
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