from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

class ServerThread(Thread):
    
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.socket = socket
        self.address = address

    def run(self):
        print(f"Nueva conexión del cliente {self.address}")

        while True:
          try:
              message = self.socket.recv(1024).decode("ISO-8859-1")
              if len(message) > 0:
                print(f"{self.address}: {message}")
              self.socket.sendall("ok".encode())
          except:
            print(f"Conexión perdida con {self.address}")
            self.socket.close()
            return
            

server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(5)

print("Servidor escuchando el puerto 8080")

while True:
   (client, address) = server.accept()
   new_thread = ServerThread(client, address)
   new_thread.start()