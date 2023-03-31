#!/usr/bin/python 

import socket #importamos el modulo socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creamos el socket

#host = socket.gethostname() #obtenemos el nombre de la maquina

port = 444 #reservamos un puerto para la conexion

clientsocket.connect(('192.132.1.2', port)) #conectamos con el servidor

message = clientsocket.recv(1024) #recibimos el mensaje del servidor

print(message.decode('ascii'))






