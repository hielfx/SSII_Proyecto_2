__author__ = 'Daniel Sánchez'
# encoding:utf-8

import socket
import sys
import json
import crypt_utils as c_utl  # custom crypto module
import gui_utils as g_utl  # Custom interface module
import os
from hashlib import sha256


class ClientSocket:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host=socket.gethostbyname(socket.gethostname()), port=7070):
        try:
            self.socket.connect((host, port))
        except ConnectionRefusedError:
            c_utl.generate_msgbox("Error", "You can not establish a connection because the target machine expressly "
                                        "rejected that connection. Check if the server socket is running.\n"
                                        "The connection address was '{0}:{1}'".
                               format(host, port), "error")

    def stop_socket(self):
        self.socket.shutdown()

    def close_socket(self):
        self.socket.close()

    def send_data(self, message):
        key = b"P$1_m3$$4G3_k3Y"
        hmac = c_utl.hash_message(message, key, mode=sha256)[1]  # We get the hashed message
        nonce = c_utl.generate_nonce()
        dict = {"message": message,
                "nonce": nonce,
                "hmac": hmac}

        _data = json.dumps(dict)

        self.socket.sendall(bytes(str.encode(_data)))

        received = str(self.socket.recv(1024), "utf-8")
        # self.socket.sendall(_data)
        # received = str(self.socket.recv(1024), "utf-8")
        # print(received)

if __name__ == "__main__":
    # g_utl.generate_client_interface()
    client = ClientSocket()
    client.connect()
    # data = bytes(str.encode(input("Prueba >")))
    client.send_data("mensaje de prueba")

# if __name__ == "__main__":
#
#     HOST, PORT = socket.gethostname(), 7070
#
#     data = input("Enter data: ")
#
#     # Create a socket (SOCK_STREAM means a TCP socket)
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     try:
#         # Connect to server and send data
#         sock.connect((HOST, PORT))
#         sock.sendall(bytes(data + "\n", "utf-8"))
#
#         # Receive data from the server and shut down
#         received = str(sock.recv(1024), "utf-8")
#     finally:
#         sock.close()
#
#     print("Sent:     {}".format(data))
#     print("Received: {}".format(received))
