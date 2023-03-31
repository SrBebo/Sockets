#!/usr/bin/python 
##tcp server
import socket #importamos el modulo socket

serversocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creamos el socket

#host= '192.132.1.2' #esta será la dirección ipv4 de nuestra maquina
host = socket.gethostname() #obtenemos el nombre de la maquina, esto con fines de automatizacion y que el programa sea mas inteligente
port = 444  #reservamos un puerto para la conexion

serversocket.bind(('192.132.1.2', port)) #ligamos el socket a la direccion con el host o simplemente ingresamos la direccion ipv4 de nuestra maquina

serversocket.listen( 3 )# el numero 3 es la cantidad de conexiones que se pueden hacer 

while True: #creamos un bucle infinito para que este siempre escuchando
    clientsocket, address = serversocket.accept() #aceptamos la conexion del cliente y guardamos la direccion en address
    print ("Conexion establecida con %s" % str(address)) #imprimimos la direccion de la conexion 
    message = 'Gracias por conectarte' + "\r\n" #creamos el mensaje que queremos enviar
    clientsocket.send(message.encode('ascii')) #enviamos el mensaje al cliente 
    clientsocket.close() #cerramos la conexion con el cliente 



