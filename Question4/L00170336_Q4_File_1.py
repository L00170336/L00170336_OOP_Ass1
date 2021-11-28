"""

#   OOP Assignment 1 - Question 4
#	anne OBrien
#	L00170336


#
"""
import socket
import threading

target = "192.168.220.129"   # This is the name of my Ubunto server I want to connect to, to scan
def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        if port == 22:  # Return SSH if Port 22 open
            print(f"SSH is open     ")
        elif port == 25:  # Return SMTP if Port 25 open
            print(f"SMTP is open     ")
        elif port == 80:  # Return HTTP if Port 80 open
            print(f"HTTP is open     ")
        elif port == 3389:  # Return RDP if Port 3389 open
            print(f"RDP is open     ")
        else:
            print(f"{port} is open     ")
    except:
        pass


for port in range(1,5050):
    thread = threading.Thread(target =port_scanner, args=[port])
    thread.start()