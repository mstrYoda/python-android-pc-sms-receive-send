import socket,json

s = socket.socket()

port = 2595
#host = socket.gethostname()
host = '192.168.0.16'

s.connect((host,port))

cevap = {'numara':'12342143','msj':'python deneme'}

s.sendall(json.dumps(cevap).encode('utf-8'));

s.close();
