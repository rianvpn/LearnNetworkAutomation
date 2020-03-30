import paramiko
import time

ip_addr = '192.168.1.2'
usr = 'admin'
pw = ''

ssh_client= paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_addr,username=usr, password=pw)

print("Success login to {}".format(ip_addr))

ssh_client.exec_command("interface bridge add name=loopback0\n")
time.sleep(4)
ssh_client.exec_command("ip address add address 10.2.2.1/32 interface=loopback0\n")
ssh_client.close