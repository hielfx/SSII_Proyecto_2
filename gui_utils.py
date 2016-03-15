__author__ = 'Daniel Sánchez'
# encoding:utf-8
import tkinter.messagebox as msgbox
import tkinter as tk
import logger
import binascii
import os
from hashlib import sha1, sha224, sha256, sha384, sha512, md5
import hmac
import sqlite3
import datetime
from client_socket import ClientSocket
from server_socket import ServerSocket
import threading
import socket

# Possible options to the message box's format
msgbox_options = {"info": msgbox.showinfo,
           "warning": msgbox.showwarning,
           "error": msgbox.showerror}


def generate_msgbox(title="", message="", msgbox_option="info"):
    if msgbox_option not in msgbox_options:
        option = "info"  # if the option is none of the options, we set it "info" as default
    # In order to display a message box we need a root window
    root = tk.Tk()
    root.withdraw()  # With this sentence, we hide the root window in order to display only the message box

    msgbox_options[msgbox_option](title, message)  # displays the message box


def generate_server_interface():
    root = tk.Tk()
    root.title("Server socket - Stopped")
    root.resizable(width=tk.FALSE, height=tk.FALSE)
    root.geometry("300x60")
    global server
    server = None

    # Server status frame
    status_frame = tk.Frame(root)
    status_frame.pack()

    label = tk.Label(status_frame, text="Server status:")
    label.pack(side=tk.LEFT, padx=1, pady=1)
    status = tk.Label(status_frame, text="stopped", fg="red")
    status.pack(side=tk.LEFT, padx=1,pady=1)
    address = tk.Label(status_frame, text="Address: {0}:{1}".format(socket.gethostbyname(socket.gethostname()), "7070"))
    address.pack(side=tk.LEFT, padx=1, pady=1)

    # server = ServerSocket()

    # Button frames
    button_frame = tk.Frame(root)
    button_frame.pack()

    def start_server_callback():
        globals()['server'] = ServerSocket()

        thr = threading.Thread(target=globals()['server'].run_server, args=(), kwargs={})
        thr.start()

        root.title("Server socket - Running")
        status['text'] = "running"
        status['fg'] = "green"

        stop_btn['state'] = tk.NORMAL
        start_btn['state'] = tk.DISABLED

    start_btn = tk.Button(button_frame, text="Start server", command=start_server_callback)
    start_btn.pack(side=tk.LEFT, padx=1, pady=1)

    def stop_server_callback():
        server.stop_server()

        root.title("Server socket - Stopped")
        status['text'] = "stopped"
        status['fg'] = "red"
        stop_btn['state'] = tk.DISABLED
        start_btn['state'] = tk.NORMAL
        msgbox.showinfo("Stop server", "The server was stopped.")

    stop_btn = tk.Button(button_frame, text="Stop server", command=stop_server_callback, state=tk.DISABLED)
    stop_btn.pack(side=tk.LEFT, padx=1, pady=1)

    def on_closing():
        server.close_server()  # We clean the socket
        root.quit()  # We close the window

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle the windows close
    root.mainloop()


def generate_client_interface():
    client = ClientSocket()
    main = tk.Tk()
    main.title("Client Socket - Disconnected")
    root = tk.Frame(main)
    root.pack(fill=tk.X)
    root = tk.Tk()

    # Connection frame


    # Origin account name
    origin_label = tk.Label(root, text="Origin account name")
    origin_label.pack(fill=tk.X)
    origin_text = tk.Entry(root, width=80)
    origin_text.pack(side=tk.LEFT, padx=1, pady=1)

    def on_closing():
        client.close_socket()  # We clean the socket on exit
        root.quit()  # We close the window

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Handle the windows close
    root.mainloop()


def generate_server_response(dict):
    message = dict['message']  # The client message returned by the server
    nonce = dict['nonce']  # The client nonce returned by the server
    hmac = dict['hmac']  # The message hmac returned by the server
    replay = dict['replay']  # Sends if it's been a reply attack
    integrity = dict['integrity']  # Sends if the integrity is correct

    root = tk.Tk()
    root.title("Server response")
    root.resizable(0, 0)


    # The status frame
    status_frame = tk.Frame(root)
    status_frame.pack()

    status_label = tk.Label(status_frame, text="Message status:", font="bold")
    status_label.grid(row=0, column=0)
    status = tk.Label(status_frame, font="bold")
    if replay:
        status['text'] = "The NONCE was sent already (maybe replay attack)."
        status['fg'] = "orange"
    elif not integrity:
        status['text'] = "The message was modified. The integrity failed."
        status['fg'] = "red"
    else:
        status['text'] = "The message was received correctly."
        status['fg'] = "green"
    status.grid(row=0, column=1)

    # The content frame
    content = tk.Frame(root)
    content.pack()

    message_label = tk.Label(content, text="Message received by the server:", font="10")
    message_label.grid(row=0, column=0, padx=2, pady=2, sticky=tk.E)
    _message = tk.Label(content, text="'{0}'".format(message))
    _message.grid(row=0, column=1, padx=2, pady=2, sticky=tk.W)

    hmac_label = tk.Label(content, text="HMAC received by the server:", font="10")
    hmac_label.grid(row=1, column=0, padx=2, pady=2, sticky=tk.E)
    _hmac = tk.Label(content, text="{0}".format(hmac))
    _hmac.grid(row=1, column=1, padx=2, pady=2, sticky=tk.W)

    nonce_label = tk.Label(content, text="NONCE received by the server:", font="10")
    nonce_label.grid(row=2, column=0, padx=2, pady=2, sticky=tk.E)
    _nonce = tk.Label(content, text="{0}".format(nonce))
    _nonce.grid(row=2, column=1, padx=2, pady=2, sticky=tk.W)

    def accept_callback():
        root.destroy()

    accept_btn = tk.Button(text="Accept", command=accept_callback, font="12")
    accept_btn.pack(padx=2, pady=2)

    root.mainloop()

if __name__ == "__main__":
    pass