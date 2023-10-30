import socket

# Cria um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define a porta e o endereço do servidor
server_address = ('localhost', 12345)

# Faz o bind do socket com o endereço e a porta
server_socket.bind(server_address)

# Começa a ouvir por conexões
server_socket.listen(1)

print(f'Esperando por uma conexão em {server_address[0]}:{server_address[1]}...')

# Aguarda a conexão do cliente
client_socket, client_address = server_socket.accept()
print(f'Conexão de {client_address}')

# Recebe a mensagem do cliente
data = client_socket.recv(1024)
print(f'Mensagem recebida: {data.decode()}')

# Envia uma resposta de volta ao cliente
response = 'Mensagem recebida com sucesso!'
client_socket.sendall(response.encode())

# Fecha a conexão com o cliente
client_socket.close()
