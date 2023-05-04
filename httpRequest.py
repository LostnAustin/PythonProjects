import socket

mysock = socket.socket(socket.AFINET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysoc.send(cmd)

while True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
   print(data.decode())
  mysock.close()
