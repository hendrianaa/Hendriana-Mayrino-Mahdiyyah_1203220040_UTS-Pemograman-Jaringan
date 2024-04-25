import socket
import random
import time

# Membuat daftar kata warna dalam bahasa Inggris
colors_en = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white']

# Membuat daftar kata warna dalam bahasa Indonesia sesuai dengan urutan kata warna dalam bahasa Inggris
colors_id = ['merah', 'biru', 'hijau', 'kuning', 'oranye', 'ungu', 'merah muda', 'cokelat', 'hitam', 'putih']

# Inisialisasi soket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    global server_socket
    # Bind soket ke alamat dan port
    server_address = ('localhost', 54321)  # Menggunakan alamat IP loopback dan port 54321
    server_socket.bind(server_address)
    
    # Menginisialisasi daftar klien yang terhubung
    clients = []

    print("Server is running...")
    
    while True:
        # Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien
        color_en = random.choice(colors_en)
        print("Server sending color:", color_en)
        for client in clients:
            server_socket.sendto(color_en.encode(), client)

        # Menerima respon dari klien selama 5 detik
        server_socket.settimeout(5)
        start_time = time.time()
        while time.time() - start_time < 5:
            try:
                # Menerima pesan dari klien
                data, address = server_socket.recvfrom(1024)
                color_id = data.decode().strip().lower()
                # Mengecek jawaban dari klien
                if color_id in colors_id:
                    print("Received from", address, ":", color_id)
                    # Memberikan nilai feedback 100 jika jawaban benar
                    server_socket.sendto(b'100', address)
                else:
                    print("Received from", address, ":", color_id, "(Incorrect)")
                    # Memberikan nilai feedback 0 jika jawaban salah
                    server_socket.sendto(b'0', address)
            except socket.timeout:
                pass

        # Menghapus klien yang tidak merespon dalam waktu yang ditentukan
        clients = [client for client in clients if time.time() - client[1] < 5]

def run_server():
    try:
        main()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Menutup soket ketika server berhenti
        server_socket.close()

if __name__ == "__main__":
    run_server()


# import socket
# import random
# import time

# # Membuat daftar kata warna dalam bahasa Inggris
# colors_en = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white']

# # Membuat daftar kata warna dalam bahasa Indonesia sesuai dengan urutan kata warna dalam bahasa Inggris
# colors_id = ['merah', 'biru', 'hijau', 'kuning', 'oranye', 'ungu', 'merah muda', 'cokelat', 'hitam', 'putih']

# # Inisialisasi soket UDP
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# def main():
#     global server_socket
#     # Bind soket ke alamat dan port
#     server_address = ('localhost', 12345)
#     server_socket.bind(server_address)
    
#     # Menginisialisasi daftar klien yang terhubung
#     clients = []

#     print("Server is running...")
    
#     while True:
#         # Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien
#         color_en = random.choice(colors_en)
#         print("Server sending color:", color_en)
#         for client in clients:
#             server_socket.sendto(color_en.encode(), client)

#         # Menerima respon dari klien selama 5 detik
#         server_socket.settimeout(5)
#         start_time = time.time()
#         while time.time() - start_time < 5:
#             try:
#                 # Menerima pesan dari klien
#                 data, address = server_socket.recvfrom(1024)
#                 color_id = data.decode().strip().lower()
#                 # Mengecek jawaban dari klien
#                 if color_id in colors_id:
#                     print("Received from", address, ":", color_id)
#                     # Memberikan nilai feedback 100 jika jawaban benar
#                     server_socket.sendto(b'100', address)
#                 else:
#                     print("Received from", address, ":", color_id, "(Incorrect)")
#                     # Memberikan nilai feedback 0 jika jawaban salah
#                     server_socket.sendto(b'0', address)
#             except socket.timeout:
#                 pass

#         # Menghapus klien yang tidak merespon dalam waktu yang ditentukan
#         clients = [client for client in clients if time.time() - client[1] < 5]

# def run_server():
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\nServer stopped.")
#     except Exception as e:
#         print("An error occurred:", e)
#     finally:
#         # Menutup soket ketika server berhenti
#         server_socket.close()

# if __name__ == "__main__":
#     run_server()
