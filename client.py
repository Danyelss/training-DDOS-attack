import socket
import time

def main():
    while true:
        s = socket.socket()
        port = 8080
        s.connect(('10.0.0.9', port))
        print (s.recv(1024).decode())
        s.close()
        time.sleep(0.75)

if __name__ == "__main__":
    main()

# ToDo: Automatic reconnect - 4 in under 3 sec
