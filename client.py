#!/usr/bin/python3
import sys
import socket
import time

def connect_to_server(ip, sock):
    return 0

if __name__ == "__main__":
    print("Client Script Initialized!")

    username = input("Enter Username: ")
    server_ip = "127.0.0.1" #input("Enter Server IP: ")
    port = 8096 #int(input("Enter Port: "))
    client_ip = socket.AF_INET

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    client_socket.connect((server_ip, port))
    print(f"Connected to Server at IP {server_ip}.")
    client_socket.listen()
    conn, addr = client_socket.accept()
    message = ""
    while True:
        data = conn.recv(4096)
        if not data: break
        message += data
    print(message)
    conn.close()
    print("Disconnected from Server")
