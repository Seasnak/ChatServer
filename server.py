#!/usr/bin/python3
import sys
import socket
import time

port = 5000

# def receive_message(client_socket) :


if __name__ == "__main__":
    print("Server Script Initialized!")

    # AF_INET = ipv4 address, SOCK_STREAM = TCP Connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # set socket to be able to take packets from the same ip (SO_REUSEADDR = 1)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    hostname = socket.gethostname () #input("Enter IP: ")
    ip = socket.gethostbyname(hostname)
    port = 8096 #int(input("Enter Port Number: "))
    server_name = input("Enter Server Name: ")

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

    conn, addr = server_socket.accept()
    print(f"Got Connection from {addr}")

    client_name = conn.recv(1024)
    client_name = client_name.decode()

    message = f"{server_name}"
    conn.send(message.encode())

    while True:
        message = conn.recv(1024)
        message = message.decode()
        if message == "[exit]":
            message = "[OK]"
            conn.send(message.encode())
            print(f"{addr} has disconnected.")
            break
        print(client_name, '>', message)
