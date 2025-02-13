import socket
import threading

# Mude isso
ip = '127.0.0.1'
port = 7777


def conectar(ip, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.send("Conexao iniciada\n".encode())
        print('Conexao iniciada')
        return client
    except Exception as error:
        print(f"Erro inesperado ao tentar conexao: {error}")

def enviar(client):
    # Parte de enviar mensagens
    while True:
        msg = input("Client >>> ")
        send = msg + "\n"
        client.sendall(send.encode())

def receber(client):
    while True:
        try:
            received = client.recv(1024).decode().strip()
            if not received:
                print("Servidor desconectado.")
                break
            print(received)
            # Adicionar comandos para respostas ou ações automatizadas
            if received == "/exit":
                print("/exit recebido, encerrando conexão!")
                client.close()
                quit()
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            break

def main():
    client = conectar(ip, port)
    thread_enviar = threading.Thread(target=enviar, args=(client, ))
    thread_receber = threading.Thread(target=receber, args=(client, ))

    thread_enviar.start()
    thread_receber.start()

   

if __name__ == "__main__":
    main()
