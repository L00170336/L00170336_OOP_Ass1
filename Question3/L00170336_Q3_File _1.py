

#
# Student:	Anne O’Brien

# File :   	L00170336_Q3_File_1

# Description :  Question 3 – Connect to my Ubuntu VM using SSH port


# import paramiko module

import paramiko


# configure the login details

hostname = "192.168.220.129"

username = "anne"

password = "holiday75"


# initialize the SSH client

client = paramiko.SSHClient()


# add to known hosts

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())




# connect to the server, if connected print, if fails print other statement

try:

   client.connect(hostname=hostname, username=username, password=password)

   print("Connected to: ", hostname)




except:

   print("[!] Cannot connect to", hostname)

   exit()
