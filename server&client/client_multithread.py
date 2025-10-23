import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 5000

def kirim_pesan(nomor):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        pesan = f"Halo dari client {nomor}"
        s.sendall(pesan.encode())
        data = s.recv(1024)
        print(f"[Client {nomor}] Balasan: {data.decode()}")

threads = []
start = time.time()
for i in range(10):
    t = threading.Thread(target=kirim_pesan, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print(f"Selesai semua request dalam {end - start:.2f} detik")
