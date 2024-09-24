import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    
    # Resolve target to IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        if any(c.isalpha() for c in target):  # Detect if target is a hostname
            return "Error: Invalid hostname"
        else:
            return "Error: Invalid IP address"

    # Scan the ports in the provided range
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout to avoid infinite waiting
        result = sock.connect_ex((target_ip, port))  # Connect to the port
        if result == 0:  # Port is open
            open_ports.append(port)
        sock.close()
    
    if verbose:
        return generate_verbose_output(target, target_ip, open_ports)
    
    return open_ports

def generate_verbose_output(target, target_ip, open_ports):
    result = f"Open ports for {target} ({target_ip})\nPORT     SERVICE\n"
    
    for port in open_ports:
        service = ports_and_services.get(port, "unknown")  # Get service name, default to 'unknown'
        result += f"{port:<9}{service}\n"
    
    return result.strip()
