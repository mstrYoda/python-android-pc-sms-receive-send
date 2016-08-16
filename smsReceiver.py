import socket

s = socket.socket()

port = 4595
#host = socket.gethostname()
host = ''
s.bind((host,port))

s.listen(1)

while True:
	c,addr = s.accept()
	print 'got connection from' , addr
	gelen = c.recv(2048)
	while (gelen):
            print gelen
            gelen = c.recv(2048)

	c.send(b'asdfdsa');

	c.close()
		


