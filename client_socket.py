__author__ = 'Daniel Sánchez'
# encoding:utf-8

import socket
import sys


class ClientSocket:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self,host='',port=7070):
        self.socket.connect((host, port))

    def close_socket(self):
        self.socket.close()

    def send_data(self, _data):
        # TODO encrypt data
        self.socket.sendall(bytes(_data), "utf-8")

if __name__ == "__main__":

    HOST, PORT = socket.gethostname(), 7070

    data = input("Enter data: ")

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
    finally:
        sock.close()

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
