import socket
import sys

def scan_port(ip, port):
    """
    Attempts to connect to a specific port on the given IP address.
    Returns True if the port is open, False otherwise.
    """
    # Create a TCP socket
    # AF_INET refers to IPv4; SOCK_STREAM refers to TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout so the scan doesn't hang forever
    s.settimeout(0.5)
    
    try:
        # Attempt to connect to the port
        result = s.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except Exception, e:
        # In Python 2, we use 'except Exception, e' instead of 'as e'
        print "Error scanning port %d: %s" % (port, str(e))
        return False
    finally:
        s.close()

def main():
    # Check if the target IP is provided via command line
    if len(sys.argv) < 2:
        print "Usage: python netscan.py <target_ip> [start_port] [end_port]"
        print "Example: python netscan.py 127.0.0.1 1 1024"
        sys.exit(1)

    target_ip = sys.argv[1]
    
    # Default port range if not provided
    start_port = 1
    end_port = 1024

    if len(sys.argv) == 4:
        start_port = int(sys.argv[2])
    if len(sys.argv) == 5:
        end_port = int(sys.argv[3])

    print "------------------------------------------"
    print "Starting scan on host: %s" % target_ip
    print "Range: Port %d to %d" % (start_port, end_port)
    print "------------------------------------------"

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print "[+] Port %d is OPEN" % port
            open_ports.append(port)

    print "------------------------------------------"
    print "Scan Complete."
    print "Total open ports found: %d" % len(open_ports)
    print "------------------------------------------"

if __name__ == "__main__":
    main()
