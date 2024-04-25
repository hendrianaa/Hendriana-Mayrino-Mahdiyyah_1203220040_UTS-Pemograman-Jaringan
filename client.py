
import socket

# Inisialisasi socket client
server_ip = '127.0.0.1'
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Kirim permintaan koneksi ke server
    client_socket.sendto("Connect".encode(), (server_ip, server_port))
        
    while True:
        # Terima kata warna dari server
        data, addr = client_socket.recvfrom(1024)
        color_en = data.decode()

        # Tampilkan kata warna dalam bahasa Inggris
        print(f"Kata warna dalam bahasa Inggris: {color_en}")

        # Terima input dari pengguna
        response = input("Masukkan kata warna dalam bahasa Indonesia: ")

        # Kirim jawaban ke server
        client_socket.sendto(response.encode(), (server_ip, server_port))

        # Terima feedback dari server
        feedback, addr = client_socket.recvfrom(1024)
        print(f"Feedback dari server: {feedback.decode()}")

except KeyboardInterrupt:
    print("\nTerima kasih telah bermain! Tutup koneksi.")
    client_socket.close()
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
    client_socket.close()
