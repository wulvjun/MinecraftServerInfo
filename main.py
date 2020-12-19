import socket
import codecs
class mcstatus:
    def __init__(self,hostname,port,timeout = 0.6):
        self.hostname= hostname
        self.timeout =timeout
        self.port =port
    def getserverinfo(self):
        s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip =socket.gethostbyname(self.hostname)
        try: 
             s.settimeout(self.timeout)
             s.connect((ip,self.port))
             s.send(bytearray([0xFE,0x01]))
             data_raw =s.recv(1024)
             s.close()

             data =data_raw.decode('cp437').split('\x00\x00\x00') 
             #data_other =data_raw.split('\x00\x00\x00')
             #data_ =codecs.utf_16_be_decode(data_other[1:])[0]
             info = {}
             #info['其它信息'] = codecs.utf_16_be_decode(data_raw[1:])[0]     
             info['支持版本'] = data[2].replace("\x00","")
             #info['服务器名称'] = codecs.utf_16_be_decode(data_other[3]).replace("\x00","")
             info['在线人数'] = data[4].replace("\x00","")
             info['最大人数'] = data[5].replace("\x00","")
             return(info)
        except socket.error:
             return(False)

server_ip = input ("服务器IP:");
if __name__ =='__main__':
    app = mcstatus(server_ip,25565)
    print (app.getserverinfo())
# mc.66ko.cc
