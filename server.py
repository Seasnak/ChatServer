#!/usr/bin/python3
import sys
import socket
import time

port = 5000

# def receive_message(client_socket) :


if __name__ == "__main__":
    print("Server Script Initialized!")

    ip = "127.0.0.1" #input("Enter IP: ")
    port = int(input("Enter Port Number: "))

    # AF_INET = ipv4 address, SOCK_STREAM = TCP Connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set socket to be able to take packets from the same ip (SO_REUSEADDR = 1)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #binding the ip to the port and listening
    try:
        server_socket.bind((ip, port))
    except:
        print(f"Error: Couldn't bind {ip} to {port}")
        sys.exit()
    server_socket.listen()

    sockets_list =  [server_socket]
    clients = {}
    print(f"Listening for connections on {ip}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Got Connection from {addr}")
        conn.send("Server Received Message")
        message = ""
        while True:
            data = conn.recv(4096)
            if not data: break
            message += data
        print(message)
        conn.close()
        print("Client Disconnected")
