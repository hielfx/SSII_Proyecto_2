__author__ = 'Daniel Sánchez'
# encoding:utf-8

import socketserver
import sys
import traceback
import logger  # Custom logger module


class ServerSocket:
    """This is the Server Socket class.
    It will provide methods to run and close the Server Socket."""

    def __init__(self, host='', port=7070):

        class MyTCPHandler(socketserver.BaseRequestHandler):
            """Request handler for our server"""

            def handle(self):
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())

        s = socketserver.TCPServer((host, port), MyTCPHandler)
        try:
            s.bind(host, port)
        except Exception:
            logger.generate_error_message("Error while trying to create the socket with ip '{0}:{1}'".format(s.server_address[0], s.server_address[1]))

        self.socket = s
        self.host = host
        self.port = port

    def run_server(self):
        # The server will run forever
        self.socket.serve_forever()

    def close_server(self):
        # To close the server
        self.socket.server_close()

if __name__ == "__main__":
    ServerSocket().run_server()