import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def handle_client(conn, addr):
    print(f"[TERHUBUNG] Client dari {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        pesan = data.decode()
        print(f"[{addr}] >> {pesan}")
        conn.sendall(f"Pesan diterima: {pesan}".encode())
    conn.close()
    print(f"[PUTUS] Client {addr}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER MULTITHREAD] Menunggu koneksi di {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[AKTIF CLIENT] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
