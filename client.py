import socket

def main():
    s = socket.socket()
    port = 8080
    s.connect(('10.0.0.2', port))
    print (s.recv(1024).decode())
    s.close()

if __name__ == "main":
    main()

# ToDo: Automatic reconnect - 4 in under 3 sec
