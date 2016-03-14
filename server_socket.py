__author__ = 'Daniel Sánchez'
# encoding:utf-8

import socketserver
import sys
import traceback
import logger  # Custom logger module
import crypt_utils  # Custom utils module
import json
import socket as sck
import gui_utils as g_utl


class ServerSocket:
    """This is the Server Socket class.
    It will provide methods to run and close the Server Socket."""

    def __init__(self, host='', port=7070):

        class MyTCPHandler(socketserver.BaseRequestHandler):
            """Request handler for our server"""

            def handle(self):
                 # self.request is the TCP socket connected to the client
                logger.get_logger().info("Receiving data...")
                self.data = self.request.recv(1024).strip()

                logger.get_logger().info("{0} wrote: {1}".format(self.client_address[0], self.data))
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)


                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())

        try:
            logger.get_logger().info("Creating the server socket...")
            s = socketserver.TCPServer((host, port), MyTCPHandler)
            logger.get_logger().info("Server socket created successfully")
            self.socket = s
            self.host = host
            self.port = port
            # s.bind(host, port)

        except Exception:
            traceback.print_exc()
            logger.generate_error_message("Error while trying to create the socket with ip '{0}:{1}'".format(sck.gethostbyname(sck.gethostname()), port))

    def run_server(self):
        logger.get_logger().info("Starting server...")
        try:
            logger.get_logger().info("Server socket started successfully.\n")
            self.socket.serve_forever()  # The server will run forever

        except Exception:
            logger.generate_error_message("Error while trying to start the server.")

    def stop_server(self):
        logger.get_logger().info("Stopping the server...")
        try:
            self.socket.shutdown()  # To close the server
            # self.socket.server_close()
            logger.get_logger().info("Server stopped successfully.\n")

        except Exception:
            logger.generate_error_message("Error while trying to stop the server.")

    def close_server(self):
        logger.get_logger().info("Closing the server...")
        try:
            self.socket.server_close()  # To close the server
            # self.socket.server_close()
            logger.get_logger().info("Server closed successfully.\n\n")

        except Exception:
            logger.generate_error_message("Error while trying to close the server.")


if __name__ == "__main__":
    g_utl.generate_server_interface()
    # server = ServerSocket()
    # server.run_server()