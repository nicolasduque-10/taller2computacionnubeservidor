from socket import *

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print("El servidor HTTP está listo para recibir mensajes")
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print("Conexión establecida con {}\n".format(clienteDireccion))
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    mensaje_split = mensaje.split()
    try:
        #get host and port to check the HTTP request
        host = gethostbyname(gethostname())+':'+str(servidorPuerto)
        if mensaje_split[0] != 'GET' or mensaje_split[4]!=host:
            2/0

        f = open(mensaje_split[1],"r")
        mensajeRespuesta = "HTTP/1.1 200 OK\r\n\r\n"+f.read()
        f.close()

    except:
        mensajeRespuesta = "HTTP/1.1 404 NOT FOUND\r\n\r\n"

    print("Mensaje recibido de ", clienteDireccion)
    print(mensaje)
    print(mensajeRespuesta)
    conexionSocket.send(bytes(mensajeRespuesta, "utf-8"))

conexionSocket.close()
