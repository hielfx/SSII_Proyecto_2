__author__ = 'Daniel Sánchez'
# encoding:utf-8

import socket
import sys
import json
import crypt_utils as c_utl  # custom crypto module
# import gui_utils as g_utl  # Custom interface module
import os
from hashlib import sha256


class ClientSocket:

    def __init__(self):
        self.socket = socket.socket()
        self.socket.settimeout(5)  # If the socket doesnt receive a response in 5 seconds it will raise a exception

    def connect(self, host=socket.gethostbyname(socket.gethostname()), port=7070):
        # try:
        self.socket.connect((host, port))
        # except Exception:
        #     g_utl.generate_msgbox("Error", "You can not establish a connection because the target machine expressly "
        #                                 "rejected that connection. Check if the server socket is running.\n"
        #                                 "The connection address was '{0}:{1}'".format(host, port), "error")
        # except socket.timeout:
        #     g_utl.generate_msgbox("Timeout", "Exceeded the timeout for the connection when waiting for data (timeout: 5 seconds).", "warning")

    def stop_socket(self):
        """Shut down one or both halves of the connection. If how is SHUT_RD, further receives are disallowed.
        If how is SHUT_WR, further sends are disallowed.
        If how is SHUT_RDWR, further sends and receives are disallowed."""
        self.socket.shutdown(socket.SHUT_RDWR)

    def close_socket(self):
        self.socket.close()

    def get_socket(self):
        return self.socket

    def send_data(self, message):
        key = "P$1_m3$$4G3_k3Y"
        # key = os.urandom(8)
        hmac = c_utl.hash_message(str.encode(message), key=bytes(str.encode(key)), mode=sha256)[1]  # We get the hashed message
        nonce = c_utl.generate_nonce()
        dict = {"message": message,
                "nonce": nonce,
                "hmac": hmac}

        _data = json.dumps(dict)

        # try:
        self.socket.sendall(bytes(str.encode(_data)))

        received = str(self.socket.recv(1024), "utf-8")
        _dict = json.loads(received)

        return _dict
        #     # We show the server response in a window
        #     g_utl.generate_server_response(_dict)
        #
        #     # print(received)
        # except socket.timeout:
        #     g_utl.generate_msgbox("Timeout", "Exceeded the timeout for the connection (timeout: 5 seconds).", "warning")

if __name__ == "__main__":
    # g_utl.generate_client_interface()
    pass
    # client = ClientSocket()
    # try:
    #     host = host=socket.gethostbyname(socket.gethostname())
    #     port = 7070
    #     client.connect(host, port)
    # except Exception:
    #     g_utl.generate_msgbox("Error", "You can not establish a connection because the target machine expressly "
    #                                 "rejected that connection. Check if the server socket is running.\n"
    #                                 "The connection address was '{0}:{1}'".format(host, port), "error")
    # except socket.timeout:
    #     g_utl.generate_msgbox("Timeout", "Exceeded the timeout for the connection when waiting for data (timeout: 5 seconds).", "warning")
    # try:
    #     _dict = client.send_data("mensaje de prueba")
    #     g_utl.generate_server_response(_dict)  # We show the server response in a window
    # except socket.timeout:
    #     g_utl.generate_msgbox("Timeout", "Exceeded the timeout for the connection (timeout: 5 seconds).", "warning")
    # finally:
    #     # client.stop_socket()
    #     client.close_socket()