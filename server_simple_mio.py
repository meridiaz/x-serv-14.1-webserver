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

Page = "HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1>Hello World!</h1><p>{}</p></body></html>" + "\r\n"

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1236))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

def sendsocket (cad, recvSocket):
    recvSocket.send(bytes(Page.format(cad),"utf-8"))
    recvSocket.close()
# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print('Waiting for connections')
    (recvSocket, address) = mySocket.accept()#le digo al socket que empiece a recibir
    print('HTTP request received:')
    peti = recvSocket.recv(1024)

    if str(peti).find("GET") == -1:
        #si estoy aqui es que me han puesto una peticion vacia, caso que ocurre
        #siempre en la primera conexion
        continue

    args = str(peti).split(' ')

    if args[1] == "/":
        sendsocket("", recvSocket)
        continue
    #busco los argumentos de la calculadora
    args = args[1].split('/')

    if len(args) != 4:
        #me han pasado algo malo para la calculadora
        print("Error: Si quieres usar la calculadora debes poner funcion/op1/op2")
        sendsocket("Si quieres usar la calculadora debes poner funcion/op1/op2", recvSocket)
        continue
    #si estoy aqui es porque ya puedo llamar a la calculadora con todos sus args
    result = calculadora2.calcular(args[1], args[2], args[3])
    sendsocket(result, recvSocket)
    print(result)
