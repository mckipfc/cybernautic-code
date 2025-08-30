import socket
import requests

# We need a list of subdomains to check for potential inlets
SUBDOMAINS = ['www', 'mail', 'ftp', 'api', 'dev', 'test']

# Adds subdomains+userinput+.com and if it finds something, it'll = IP address
def check_subdomains(domain):
    for sub in SUBDOMAINS:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            print(f"[+] Found: {url} -> {ip}")
            get_http_info(url)
        except socket.gaierror:
            pass
#
def get_http_info(subdomain):
    try:
        # Here we are seeing if it is reachable through http
        res = requests.get(f"http://{subdomain}", timeout=3)
        if "<title>" in res.text:
            print(f"    Title: {res.text.split('<title>')[1].split('</title>')[0]}")
        else:
            print("    No title tag found")
    except Exception:
     try:
         # Here, if the above code fails, we check https for reachability
        res = requests.get(f"https://{subdomain}", timeout=3)
        if "<title>" in res.text:
            print(f"    Title: {res.text.split('<title>')[1].split('</title>')[0]}")
        else:
            print("    No title tag found")
     except Exception:
        print("No web response")

if __name__ == "__main__":
    domain = input("Enter domain (e.g. example.com): ").strip()
    check_subdomains(domain)
