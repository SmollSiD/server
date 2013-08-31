__author__ = 'user'
import socket
sock = socket.socket()
sock.connect(('localhost',6063))
str=input()
sock.send(str.encode('utf-8'))
sock.close()