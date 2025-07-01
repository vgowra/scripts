from netmiko import ConnectHandler
import getpass

#prompt for username and password
username = input("Enter your Username: ")
password = getpass.getpass("Enter your password: ")

# Read bulk devices FQDNs/IPs from a file
with open('devices.txt') as f:
    devices = [host.strip() for host in f.readlines()]

# Read device configurations that are neede to be added/deleted/modified from a file
with open('commands.txt') as f:
    commands = [cmd.strip() for cmd in f.readlines()]

# Loop through each device and run command
for host in devices:
    try:
        conn = ConnectHandler(
            device_type='juniper_junos',
            host=host,
            username=username,
            password=password,
        )
        output = conn.send_config_set(commands, exit_config_mode=False)
        commit_output = conn.commit()
        print(f"{host} configuration successful:\n{output}\n{commit_output}")
        conn.disconnect()
    except Exception as e:
        print(f"{host} failed: {str(e)}")
