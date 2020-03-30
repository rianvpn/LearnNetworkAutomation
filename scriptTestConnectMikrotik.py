import paramiko
import time

ip_addr = '192.168.1.2'
usr = 'admin'
pw = ''

ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_addr,username=usr,password=pw)

print("Success login to {}".format(ip_addr))

time.sleep(2)
print("Now Exit")
ssh_client.close
