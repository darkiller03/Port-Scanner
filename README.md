# Port Scanner

## Project Overview

The **Port Scanner** is a Python application that scans a range of ports for a given target (IP address or hostname) to identify which ports are open. The program can work in both standard and verbose modes. In verbose mode, it provides detailed output showing the open ports along with the corresponding services.

This project is part of the Certification **Information security** on [FreeCodeCamp](https://www.freecodecamp.org/).

## Project Files

- **port_scanner.py**: The main file that implements the core functionality for scanning ports.
- **common_ports.py**: Contains a dictionary that maps port numbers to common services.
- **test_module.py**: Contains unit tests that ensure the port scanner functions correctly.
- **main.py**: An entry point for manually running the program and seeing the results in different modes.

## Usage

### Scanning Ports

You can use the port scanner to scan a range of ports on an IP address or domain name. By default, the program returns a list of open ports.

```python
import port_scanner

# Scan ports of an IP address
open_ports = port_scanner.get_open_ports("209.216.230.240", [440, 445])
print(open_ports)  # Output: [443]
```

## Verbose Mode

In verbose mode, the program returns more detailed information, including the open ports and the corresponding services.

```python

import port_scanner

# Scan ports with verbose mode enabled
verbose_output = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
print(verbose_output)
```
**Sample output in verbose mode:**

```mathematica

Open ports for scanme.nmap.org (45.33.32.156)
PORT     SERVICE
22       ssh
80       http
```

## Error Handling

The program provides error messages for invalid IP addresses and hostnames:

    If the hostname is invalid, it returns: "Error: Invalid hostname".
    If the IP address is invalid, it returns: "Error: Invalid IP address".

**Example**

```python

import port_scanner

# Invalid hostname
print(port_scanner.get_open_ports("invalid.hostname", [20, 80]))  
# Output: Error: Invalid hostname

# Invalid IP address
print(port_scanner.get_open_ports("266.255.9.10", [20, 80]))
# Output: Error: Invalid IP address
```

## Running the Program

```bash
python main.py