import socket
import requests
import whois
import argparse
from datetime import datetime

def print_banner():
    """Prints the tool's banner."""
    print("-" * 55)
    print("🚀 Recon-Pulse: Automated Reconnaissance Tool")
    print("-" * 55)

def get_whois(domain):
    """Fetches WHOIS registration data for the target domain."""
    print("\n[+] Gathering WHOIS Information...")
    try:
        domain_info = whois.whois(domain)
        print(f"Registrar: {domain_info.registrar}")
        print(f"Creation Date: {domain_info.creation_date}")
        print(f"Expiration Date: {domain_info.expiration_date}")
    except Exception as e:
        print(f"[-] Error fetching WHOIS data. Is the domain valid?")

def get_headers(domain):
    """Fetches HTTP headers to identify server software and configurations."""
    print("\n[+] Fetching HTTP Server Headers...")
    try:
        # Use HTTPS by default,and  fallback to HTTP if needed
        url = f"https://{domain}"
        response = requests.get(url, timeout=5)
        
        # Only to print the most interesting security-related headers
        interesting_headers = ['Server', 'X-Powered-By', 'Strict-Transport-Security', 'X-Frame-Options']
        for header in interesting_headers:
            if header in response.headers:
                print(f"{header}: {response.headers[header]}")
            else:
                print(f"{header}: Not Set (Potential finding)")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching headers: {e}")

def scan_ports(domain):
    """Scans a short list of common ports to see what services are open."""
    print("\n[+] Scanning Common Ports (21, 22, 80, 443)...")
    try:
        target_ip = socket.gethostbyname(domain)
        print(f"Resolved IP: {target_ip}")
        
        # 21=FTP, 22=SSH, 80=HTTP, 443=HTTPS
        ports = [21, 22, 80, 443] 
        
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1) # 1 second timeout for faster scanning
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[!] Port {port}: OPEN")
            else:
                print(f"[*] Port {port}: CLOSED / FILTERED")
            sock.close()
    except socket.gaierror:
        print("[-] Error resolving domain name.")

def main():
    # Setup command line arguments
    parser = argparse.ArgumentParser(description="Recon-Pulse: A lightweight OSINT and Recon tool.")
    parser.add_argument("target", help="The target domain to scan (e.g., example.com)")
    args = parser.parse_args()

    domain = args.target

    # Run the tool 
    print_banner()
    print(f"Target: {domain}")
    print(f"Scan Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    get_whois(domain)
    get_headers(domain)
    scan_ports(domain)
    
    print("\n[+] Reconnaissance Complete.")

if __name__ == "__main__":
    main()
             #made purely by sayantan saha    
