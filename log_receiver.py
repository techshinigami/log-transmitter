import socket

FORMAT = 'utf-8'

def receive_log(server_address: str, port: int) -> None:
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_server.bind((server_address, port))
    print(f"[LISTENING] Server is listening on {server_address}:{port}")

    while True:
        data, addr = udp_server.recvfrom(1024)  # Buffer size of 1024 bytes
        print(f"[RECEIVED] From {addr}: {data.decode(FORMAT)}")

if __name__ == "__main__":
    server_address = socket.gethostbyname(socket.gethostname())
    port = int(input("Enter the port number: ").strip())
    receive_log(server_address, port)
