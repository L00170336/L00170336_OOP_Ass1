"""

#   OOP Assignment 1 - Question 4
#	anne OBrien
#	L00170336


"""
import socket
import threading
import sys

target = "192.168.220.129"  # Which Host to Scan


def port_scanner(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        socket.getfqdn("8.8.8.8")

        if port == 22:  # Will print SSH if this port is open
            print(f"SSH is open")
        elif port == 80:  # Will print HTTP if this port is open
            print(f"HTTP is open")
        else:
            print(f"{port} is open")
    except:
        pass


for port in range(1, 1025):
    thread = threading.Thread(target=port_scanner, args=[port])
    thread.start()
