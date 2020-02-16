#!/usr/bin/python3
"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
alumna: Meritxell Diaz
"""

import socket
import calculadora2

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()#le digo al socket que empiece a recibir
    print('HTTP request received:')
    prueba = recvSocket.recv(1024)

    print(prueba)
    if str(prueba).find("GET") == -1:
        print("HAY una str vacia")
        continue

    args = str(prueba).split(' ')
    if args[1] == "/":
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hello World!</h1></body></html>" +
                        b"\r\n")
        recvSocket.close()
        continue

    args = args[1].split('/')
    print(args)
    if len(args) != 4:
        #me han pasado algo malo
        print("Error: Si quieres usar la calculadora debes poner funcion/op1/op2")
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hello World!</h1><p>Si quieres usar la calculadora debes poner funcion/op1/op2</p></body></html>" +
                        b"\r\n")
        recvSocket.close()
        continue
    #si estoy aqui es porque ya puedo llmar a la calculadora
    result = calculadora2.calcular(args[1], args[2], args[3])

    if result == None:
        #ha introducido mal los parametros o ha dividido por 0
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hello World!</h1><p>Debes poner una operacion y operandos validos</p></body></html>" +
                        b"\r\n")
        recvSocket.close()
    else:
        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        bytes("<html><body><h1>Hello World!</h1><p>El resultado es: {}</p></body></html>".format(result),"utf-8") +
                        b"\r\n")
        recvSocket.close()
        print("El resultado es: "+ str(result))
