import socket

def port_scan(target_host, target_ports):
    for port in target_ports:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(1)  # Set a timeout for connection attempts

        try:
            client_socket.connect((target_host, port))
            print(f"Port {port} is open on {target_host}")
            client_socket.close()
        except Exception:
            print(f"Port {port} is closed on {target_host}")

def main():
    start_ip = input("Enter the starting IP (e.g., 192.168.1.1): ")
    end_ip = input("Enter the ending IP (e.g., 192.168.1.10): ")

    # Extract the first three octets and last octet as integer
    ip_prefix = ".".join(start_ip.split(".")[:-1])  # Example: "192.168.1"
    start_ip_int = int(start_ip.split(".")[-1])
    end_ip_int = int(end_ip.split(".")[-1])

    target_ports = [80, 21, 22, 23, 443, 53, 25, 110]

    print(f"\nScanning IP addresses from {start_ip} to {end_ip}...\n")

    for i in range(start_ip_int, end_ip_int + 1):
        target_host = f"{ip_prefix}.{i}"
        print(f"Scanning {target_host}...")
        port_scan(target_host, target_ports)

if __name__ == "__main__":
    main()
