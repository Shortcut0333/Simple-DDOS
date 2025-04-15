import socket
import time

ASCII_ART = r"""
  ___ _            _           _    __ ____________
 / __| |_  ___ _ _| |_ __ _  _| |_ /  \__ /__ /__ /
 \__ \ ' \/ _ \ '_|  _/ _| || |  _| () |_ \|_ \|_ \
 |___/_||_\___/_|  \__\__|\_,_|\__|\__/___/___/___/
             Github.com/Shortcut0333
"""

def create_packet(size):
    return b"A" * size  # Create a packet filled with 'A's of the specified size

def main():
    print(ASCII_ART)
    
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    num_packets = int(input("Enter the number of packets to send: "))
    packet_size = int(input("Enter the size of each packet (in bytes): "))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_data = create_packet(packet_size)

    for i in range(num_packets):
        sock.sendto(packet_data, (target_ip, target_port))
        print(f"Packet {i + 1}/{num_packets} sent: {packet_data}")
        time.sleep(1)

    sock.close()
    print("Copyright © shortcut0333 on GitHub")

if __name__ == "__main__":
    main()