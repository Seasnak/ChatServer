#!/usr/bin/python3
import sys
import socket
import time

def connect_to_server(ip, sock):
    return 0

if __name__ == "__main__":
    print("Client Script Initialized!")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    username = input("Enter Username: ")
    server_ip = input("Enter Server IP: ")
    port = 8096 #int(input("Enter Port: "))
    hostname = socket.gethostname()
    client_ip = socket.gethostbyname(hostname)

    client_socket.connect((server_ip, port))
    print(f"Connected to Server at IP {server_ip}.")
    client_socket.send(username.encode())
    server_name = client_socket.recv(1024)
    server_name = server_name.decode()
    print(f"Joined Server: {server_name}")
    print("Enter [exit] to exit.")
    while True:
        message = input(f"{username} > ")
        if message == "[exit]":
            client_socket.send(message.encode())
            message = client_socket.recv(1024)
            if message.decode() == "[OK]":
                print(f"Exiting from {server_name}.")
                break
            else:
                print("Error: Couldn't exit chat server, please try again.")
        client_socket.send(message.encode())
