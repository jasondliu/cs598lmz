import socket
import pickle
import sys
import time

def create_player(num, username, password):

	client.send("create")
	client_input = client.recv(1024)
	client.send(username)
	client_input = client.recv(1024)
	if client_input == "username taken":
		return

	client.send(password)
	client_input = client.recv(1024)
	client_input = client.recv(1024)
	f = open(num + ".txt", "w")
	f.write(client_input)
	f.close()

def login_player(num, username, password):
	client.send("login")
	client_input = client.recv(1024)
	client.send(username)
	client_input = client.recv(1024)
	if client_input != "user not found":
		client.send(password)
		client_input = client.recv(1024)
		client_input = client.recv(1024)
