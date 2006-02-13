NETSCAN v1.0 - Simple Port Scanner
==================================

DATE: May 2006
AUTHOR: [Your Name]

DESCRIPTION:
    NetScan is a lightweight command-line utility designed to scan 
    TCP ports on a target host to identify open services. 
    It is useful for basic network administration and security 
    auditing.

REQUIREMENTS:
    - Python 2.4 or higher must be installed on your system.

USAGE:
    Open your terminal or command prompt and run:
    
    python netscan.py <target_ip> [start_port] [end_port]

EXAMPLES:
    Scan first 1024 ports of localhost:
    python netscan.py 127.0.0.1

    Scan specific range on a remote host:
    python netscan.py 192.168.1.1 20 80

NOTES:
    - This tool is for educational purposes only.
    - Please use responsibly on networks you own.
