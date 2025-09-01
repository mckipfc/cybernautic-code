import socket
import requests

# We need a list of subdomains to check for potential inlets
SUBDOMAINS = ['www', 'mail', 'ftp', 'api', 'dev', 'test']

def extract_title(html):
    start = html.lower().find("<title>")
    if start == -1:
        return None

    ## start + 7 means it won't include "<title>" in the output
    titlestart = start + 7

    end = html.lower().find("</title>", titlestart)
    if end == -1:
        return None

    title = html[titlestart:end]
    cleaned = " ".join(title.split())
    return cleaned

def get_http_info(subdomain):
    try:
        # Here we are seeing if it is reachable through http
        res = requests.get(f"http://{subdomain}", timeout=3)
        title = extract_title(res.text)
        if title:
            print(f"    Title: {title}")
        else:
            print("    No title tag found")
            except requests.exceptions.RequestException:
            print("    No web response")
    except requests.exceptions.RequestException:
        print("    No web response")

# Adds [SUBDOMAINS]+[userinput]+[.com] and if it finds something, it'll = IP address
def check_subdomains(domain):
    for sub in SUBDOMAINS:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            print(f"[+] Found: {url} -> {ip}")
            get_http_info(url)
        except socket.gaierror:
            pass

if __name__ == "__main__":
    domain = input("Enter domain (e.g. example.com): ").strip()
    check_subdomains(domain)
