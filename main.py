from random import randint

# Starting ip address
first_ip = '0.0.0.0'
# Final ip address
last_ip = '255.255.255.255'

# Ip address is unique?
is_unique = False
# Number of generated ip addresses
N = 5000

first_ip_list = [int(_) for _ in first_ip.split('.')]
last_ip_list = [int(_) for _ in last_ip.split('.')]

ip_list = []

for i in range(N):
    while True:
        ip = [randint(first_ip_list[i], last_ip_list[i]) for i in range(4)]
        ip_str = '.'.join(str(_) for _ in ip)

        if is_unique and ip_str in ip_list:
            continue

        ip_list.append(ip_str)
        break

with open('ip_list', 'w', encoding='utf-8') as file:
    for i in ip_list:
        print(i, file=file)

