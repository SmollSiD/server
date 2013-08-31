import socket
import os
#test comment
class Server():
    sock=socket.socket()
    def runServer(self,port=6063):
        str=""
        self.sock.bind(('',int(port)))
        while True:
            self.sock.listen(1)
            conn,addr = self.sock.accept()
            print(addr)
            while True:
                data=conn.recv(1024)
                if not data:
                    break
                str=data.decode('utf-8')
            if str=="xbmc_on":
                os.startfile("xbmc")
            if str=="xbmc_off":
                os.system("TASKKILL /IM xbmc.exe")
            print(str)
    def stopServer(self):
        self.sock.close()
serv=Server()
serv.runServer()

