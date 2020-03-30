import paramiko
import time

devices = [
    {
        'ip_address' : '192.168.1.3',
        'vendor' : 'cisco',
        'username': 'cisco',
        'password' : 'cisco'
    },
    {
        'ip_address' : '192.168.1.2',
        'vendor' : 'mikrotik',
        'username': 'admin',
        'password' : ''
    }

]

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for device in devices:
    ssh_client.connect(hostname=device['ip_address'],username=device['username'], password=device['password'])
    print("\nSuccess login to {}".format(device['ip_address']))

    if device['vendor'] == 'cisco':
        conn = ssh_client.invoke_shell()
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())

    else:
        time.sleep(2)
        print("Now Exit")
        ssh_client.close

