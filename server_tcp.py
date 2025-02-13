import socket
import threading

# Mude isso
ip = '0.0.0.0'
port = 7777

def escutar(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f"Escutando na porta {port}...")

    # Receber o socket e o endereco e guardar
    connection, address = server.accept()
    print(f"Conexao recebida de {address[0]}, pela porta de saida {address[1]}")

    return connection

def receber(server):
    while True:
        try:
            data = server.recv(1024).decode().strip()
            print(data)
            if not data:
                print("Client desconectado.")
                break
        except Exception as erro:
            print(f"Erro ao receber dados: {erro}")
            quit()


def enviar(server):
    while True:
        try:
            msg = input("Server >>> ")
            send = msg + "\n"
            server.send(send.encode())
        except Exception as erro:
            print(f"Erro ao enviar mensagem: {erro}")

def main():
    server = escutar(ip, port)
    
    thread_receber = threading.Thread(target=receber, args=(server,))
    thread_enviar = threading.Thread(target=enviar, args=(server,))

    thread_receber.start()
    thread_enviar.start()

if __name__ == "__main__":
    main()