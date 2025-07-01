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
    print(f"\n{'='*40}\nConnecting to {host}\n{'='*40}")
    try:
        net_connect = ConnectHandler(
            device_type='cisco_ios', # change if NX-OS, ASA & so on..
            host=host,
            username=username,
            password=password,
        )
        output = net_connect.send_command('show ip int brief')
        print(output)
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to connect to {host} : {e}")

print("\nScript completed.")
