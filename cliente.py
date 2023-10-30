import socket

# Cria um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço e a porta do servidor
server_address = ('localhost', 12345)

# Conecta ao servidor
client_socket.connect(server_address)

# Envia uma mensagem para o servidor
message = 'Olá, servidor!'
client_socket.sendall(message.encode())

# Recebe a resposta do servidor
data = client_socket.recv(1024)
print(f'Mensagem do servidor: {data.decode()}')

# Fecha a conexão com o servidor
client_socket.close()
