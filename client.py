import socket
import time

def main():
    while True:
        s = socket.socket()
        port = 8080
        try:
            s.connect(('10.0.0.9', port))
            string = s.recv(1024).decode()
            if string:
                print (string)
        except:
            s.close()
        time.sleep(0.75)

if __name__ == "__main__":
    main()

# ToDo: Automatic reconnect - 4 in under 3 sec
