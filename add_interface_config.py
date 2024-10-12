import getpass
import time
from netmiko import ConnectHandler, file_transfer, juniper

host = "10.85.250.24"
u = "labroot"
p = "lab123"


router = {
    'device_type': "juniper_junos",
    'ip': host,
    'username': u,
    'password': p,
}

connection=ConnectHandler(**router)

connection.config_mode()

config_commands= [
    'set interfaces ge-0/0/0 description test',
    
]

output=connection.send_config_set(config_commands)

commit_output=connection.commit()

print(output)
print(commit_output)

connection.exit_config_mode()
connection.disconnect()

