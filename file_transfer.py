#!/usr/bin/python3

from netmiko import ConnectHandler, file_transfer

cisco = {
    'device_type': 'cisco_xr',
    'ip': '10.176.33.186',
    'username': 'g1392823',
    'password': 'Ynysmeudwy@66',
    
}

source_file = "test1.txt"
dest_file = "testa.txt"
direction = "put"
file_system = "harddisk:"
 
# Create the Netmiko SSH connection
ssh_conn = ConnectHandler(**cisco)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
)
print(transfer_dict)
pause = input("Hit enter to continue: ")