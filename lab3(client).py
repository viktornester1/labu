import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.102", 8000))


while True:
    data = client.recv(4096)
    print(data.decode("utf-8"))
    client.send(input("--->").encode("utf-8"))

