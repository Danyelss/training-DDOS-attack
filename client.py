import socket
import time

def main():
    s = socket.socket()
    port = 8080
    while true:
        s.connect(('10.0.0.9', port))
        print (s.recv(1024).decode())
        s.close()
        time.sleep(0.75)

if __name__ == "main":
    main()

# ToDo: Automatic reconnect - 4 in under 3 sec
