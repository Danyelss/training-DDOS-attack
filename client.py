import socket
import time

def main():
    while True:
        s = socket.socket()
        port = 8080
        try:
            s.connect(('10.166.0.2', port))
            string = s.recv(1024).decode()
            if string:
                print (string)
        finally:
            s.close()
        time.sleep(0.75)

if __name__ == "__main__":
    main()

# ToDo: Automatic reconnect - 4 in under 3 sec
