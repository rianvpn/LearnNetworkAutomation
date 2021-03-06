# masukan library.
import paramiko
import time
# mendefiniskan ip address username dan pasword.
ip_address = '192.168.1.3'
username = 'cisco'
password = 'cisco'
# \koneksi ke cisco dengan parameter yang sudah didefinisikan sebelumnya.
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username, password=password)
# menampilkan jika login sudah sukses, lalu masuk ke shell ntuk mengirim perintah ke cisco.
print("Success login to {}".format(ip_address))
conn = ssh_client.invoke_shell()
# kirimkan perintah untuk menambahkan interface loopback, setelah itu delay 1 detik.
conn.send("conf t\n")
conn.send("in lo0\n")
conn.send("ip add 10.1.1.1 255.255.255.255\n")
time.sleep(1)
# print output ke console
output = conn.recv(65535)
print(output.decode())
# keluar dari ssh
ssh_client.close