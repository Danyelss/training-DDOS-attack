import socket
import threading
import time
addrs_dict = {}
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.timer = 3
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            if address[0] not in addrs_dict.keys() or addrs_dict[address[0]] <= time.time():
                print(addrs_dict)
                addrs_dict[address[0]] = time.time() + self.timer
                threading.Thread(target = self.listenToClient,args = (client,address)).start()
            else:
                client.close()
                print("You shall not pass !!!")

    def listenToClient(self, client, address):
        print ('Connected to ', address )
        try:
            client.send('I am the main server'.encode())
        except:
            pass
        client.close()
        return False

if __name__ == "__main__":
    port_num = 8080
    ThreadedServer('',port_num).listen()
