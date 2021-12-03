#Anne O'Brien
#Student ID: L00170336
#Question5_File_2


#Curl already installed via SSH

#This script is to create a directory structure labs with subfolders lab1 and lab2.

# import paramiko

import paramiko

# my Ubuntu login details
IP = "192.168.220.136"
username = "anne"
password = "holiday75"

# start the SSH

client = paramiko.SSHClient()

# add to known hosts

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to my server, if connected print success and IP address, if fails print unable to connect

try:

   client.connect(hostname=IP, username=username, password=password)
   connection = client.invoke_shell()
   client.exec_command("mkdir Labs\n")
   client.exec_command("mkdir Labs/lab1\n")
   client.exec_command("mkdir Labs/lab2\n")

   print('Labs created.')
except:
   print("[!] Cannot connect to", hostname)
   exit()