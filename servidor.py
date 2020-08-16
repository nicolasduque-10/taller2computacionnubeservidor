#David Martinez, Miguel Castillo Y Nicolás Duque

from socket import *

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)

while 1:

    conexionSocket, clienteDireccion = servidorSocket.accept()
    service = str( conexionSocket.recv(1024), "utf-8" )
    if service.lower()=='saldo':
        with open(r'saldoSergio.txt','r') as f:
            saldo='Tu saldo actual es de: '+f.read()
            conexionSocket.send(bytes(saldo, "utf-8"))
            print("Conexión establecida con {}\n".format(clienteDireccion))
            print("Cliente solicita saldo. \n")
            print(saldo)
    elif service.lower()=='debitar':
        with open(r'saldoSergio.txt','r') as f:
            saldo=float(f.read())
            print("Cliente solicita debito. \n ")
            print(saldo)
        with open(r'saldoSergio.txt','w') as f:
            X = str( conexionSocket.recv(1024), "utf-8" )
            X=float(X)
            if X>saldo:
                response='Saldo insuficiente :(\n'
                f.write(str(saldo))
                print("Saldo insuficiente. \n")
            else:
                response='OK :)\n'
                print(saldo-X)
                f.write(str(saldo-X))
            conexionSocket.send(bytes(response, "utf-8"))
        
    elif service.lower()=='acreditar':
        with open(r'saldoSergio.txt','r') as f:
            saldo=float(f.read())
        with open(r'saldoSergio.txt','w') as f:
            Y = str(conexionSocket.recv(1024), "utf-8" )
            Y=float(Y)
            nuev_saldo=str(saldo)
            f.write(nuev_saldo)
            response=f'Nuevo saldo: {nuev_saldo}\n'
            print(response)
            conexionSocket.send(bytes(response, "utf-8"))

    conexionSocket.close()
