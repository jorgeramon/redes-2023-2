from socket import AF_INET, SOCK_STREAM, socket

host = "www.indicedepaginas.com"
request = f"GET / HTTP/1.1\r\nHost:{host}\r\nConnection: close\r\n\r\n"

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, 80))
client.sendall(request.encode())

response = b""

while True:
  chunk = client.recv(4096)
  if len(chunk) == 0:
    break
  response = response + chunk

client.close()

content = response.decode("ISO-8859-1").split("\r\n\r\n", 1)[1]

with open("indicedepaginas.html", "w") as file:
  file.write(content)