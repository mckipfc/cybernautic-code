import socket
import requests

# List of subdomains to check for potential inlets
SUBDOMAINS = ['www', 'mail', 'ftp', 'api', 'dev', 'test']

def extract_title(html):
    start = html.lower().find("<title>")
    if start == -1:
        return None

    # Exclude "<title>" in the output
    titlestart = start + 7

    # Look for end title
    end = html.lower().find("</title>", titlestart)
    if end == -1:
        return None

    #
    title = html[titlestart:end]
    cleaned = " ".join(title.split())
    return cleaned

def get_http_info(subdomain):
    try:
        # Try https first
        res = requests.get(f"https://{subdomain}", timeout=3)
    except requests.exceptions.RequestException:
        try:
            # If no https due to network error from https, check http
            res = requests.get(f"http://{subdomain}", timeout=3)
        except requests.exceptions.RequestException as e:
                print ("   No web response:", e)
                return
    # If title is found in either http or https, print it
    title = extract_title(res.text)
    if title:
        print(f"    Title: {title}")
    else:
        print("    No title tag found")


# Puts together subdomains to find IP address
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
