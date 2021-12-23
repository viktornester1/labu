import socket
import lab1

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.0.102", 8000))

server.listen(3)
print("Server is running")
while True:
    user_socket, address = server.accept()
    while True:

        if result1 == '':
            lab1.ceasar()
        else:
            break
        from lab1 import result1
        user_socket.send(encrypted.encode("utf-8"))
        data = user_socket.recv(2048)
        print(data.decode("utf-8"))
