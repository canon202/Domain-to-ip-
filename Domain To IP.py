#Domain to ip

import socket
import pyfiglet
from termcolor import colored  


banner = pyfiglet.figlet_format("domain to ip")
colored_banner = colored(banner, color="magenta")  
print(colored_banner)  

def domain_to_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error as e:
        return f"Error: {e}"

if __name__ == "__main__":
    domain = input("Enter your domain: ")
    ip = domain_to_ip(domain)
    colored_ip = colored(f"IP Address: {ip}", color="blue")  
    print(colored_ip)  