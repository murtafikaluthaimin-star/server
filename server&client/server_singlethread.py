import socket

HOST = '127.0.0.1'
PORT = 5001

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[SERVER SINGLETHREAD] Menunggu koneksi di {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
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

if __name__ == "__main__":
    main()
