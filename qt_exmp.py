from PyQt4 import QtGui,QtCore,uic
import PyQt4
import socket
import os

class MyWindow(QtGui.QWidget):
   def __init__(self,parent=None):
       QtGui.QWidget.__init__(self,parent)
       uic.loadUi('client.ui',self)
       self.adrr='192.168.0.80'
       self.comm_box.hide()
       self.ico=QtGui.QIcon("icon.png")
       self.tray=QtGui.QSystemTrayIcon(self.ico)
       traySignal = "activated(QSystemTrayIcon::ActivationReason)"
       self.connect(self.tray,QtCore.SIGNAL(traySignal),self.showProgr)
   def closeEvent(self,e):
           e.ignore()
           self.hide()
           self.tray.show()
   def showProgr(self,reason):
       if reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.tray.hide()
            self.show()
   def slot1(self):
    sock = socket.socket()
    port=self.le1.text()
    sock.connect(('192.168.0.80',int(port)))
    str=self.le2.text()
    sock.send(str.encode('utf-8'))
    sock.close()
    self.conn_box.hide()
    self.comm_box.show()
   def send_comm(self,comm):
       sock = socket.socket()
       port=self.le1.text()
       sock.connect((self.adrr,int(port)))
       str=comm
       sock.send(str.encode('utf-8'))
       sock.close()
   def xbmc_on(self):
        self.send_comm("xbmc_on")
   def xbmc_off(self):
       self.send_comm("xbmc_off")




if __name__=="__main__":
    import sys
    app=QtGui.QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec_())

