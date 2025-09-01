# Subdomain Scanner

A Python tool that scans for common subdomains and checks if they are reachable.
If the website subdomain is reachable it checks if the subdomain has any titles
that you may find interesting and would want to focus on.

# Features
- Resolves common subdomains (www, mail, ftp, api, etc.)
- Resolves IP addresses
- Checks HTTP/HTTPS accessibility
- Extracts webpage <title> if found
  
## Requirements
- Python 3.x
- requests library
```bash
pip install -r requirements.txt
```

## Usage
Run the scanner against a domain:
```bash
python subdomain_scanner.py example.com 
[+] Found: www.example.com -> 93.184.216.34
     Title: Example Domain

[+] Found: mail.example.com -> 93.184.216.34
     No title tag found
```
# Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/mckipfc/Subdomain_Scanner.git
cd Subdomain_Scanner
pip install -r requirements.txt
