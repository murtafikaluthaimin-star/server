import socket
import time

HOST = '127.0.0.1'
PORT = 5001

start = time.time()

for i in range(10):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        pesan = f"Halo dari client {i}"
        s.sendall(pesan.encode())
        data = s.recv(1024)
        print(f"[Client {i}] Balasan: {data.decode()}")

end = time.time()
print(f"Selesai semua request dalam {end - start:.2f} detik")
