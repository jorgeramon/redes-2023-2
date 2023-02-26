from socket import AF_INET, SOCK_STREAM, socket

client = socket(AF_INET, SOCK_STREAM)

client.connect(("127.0.0.1", 8080))

print("Conectado al servidor, escribe algo:")

while True:
  message = input()
  client.sendall(message.encode())
  response = client.recv(1024).decode("ISO-8859-1")
  print(f"Servidor:{response}")
