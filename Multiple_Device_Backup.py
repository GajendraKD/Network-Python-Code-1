file1 = open("devices_output_New_1.txt", "w")

for devices in devices_list:

    file1 = open(str(devices) + '.txt', 'w')

    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    iosv_devices = {
        'device_type': 'arista_eos',
        'ip': ip_address_of_device,
        'username': Username,
        'password': Password
    }

    net_connect = ConnectHandler(**iosv_devices)
    Hostname = net_connect.send_command('show hostname')
    Hostname = '*' * 25 + '  ' + Hostname.split('\n')[0].partition(": ")[2] + '  ' + '*' * 25 + '\n'
    file1.write(Hostname)

   # front_dash = '=' * 25 + '  '
   # last_dash = '  ' + '=' * 25 + '\n'
   # configuration = front_dash + 'Configuration start' + last_dash
   # file1.write('\n')
   # file1.write(configuration.replace("start", "end"))
   # file1.write('\n')

    output = ""

    with open('commands_file') as f:
        commands_list = f.read().splitlines()
    for cmd in commands_list:
        output = output + cmd + "\n"
        output = output + net_connect.send_command(cmd) + '\n'

    file1.write(output)
    file1.close()
