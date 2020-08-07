from netmiko import ConnectHandler
import time

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.100',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
    'verbose' : True,
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.101',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
    'verbose' : True,
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.102',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
    'verbose' : True,
}


with open('l2_101') as file:
    lines = file.read().splitlines()
print(lines)

all_devices = [iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
    print(output)
  
with open('l3_102') as file:
    lines = file.read().splitlines()
print(lines)

all_devices = [iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
    print(output)
    time.sleep(1)

with open('l2_100') as file:
    lines = file.read().splitlines()
print(lines)

all_devices = [iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()
    output = net_connect.send_config_set(lines)
    print(output)
    time.sleep(1)    
  
    
    
