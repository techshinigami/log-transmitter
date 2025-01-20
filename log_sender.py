import socket
from os import path

FORMAT = 'utf-8'

def send_log(file_path: str, server_address: str, port: int) -> None:
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (server_address, port)

    if path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip().encode(FORMAT)
                udp_client.sendto(line, server_address)
                print(f"Sent: f{line}")
    else:
        print(f"[ERROR] File not found.")

    udp_client.close()

if __name__ == "__main__":
    file_path = input("Enter the file name: ").strip()
    server_address = input("Enter the server address: ").strip()
    port = int(input("Enter the port number: ").strip())
    send_log(file_path, server_address, port)