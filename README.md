# recon-pulse
A lightweight OSINT tool to automate subdomain enumeration, port scanning, and WHOIS lookups for a target domain.
# 🚀 Recon-Pulse

A lightweight, automated Open Source Intelligence (OSINT) and reconnaissance tool built in Python. Designed for ethical hackers and penetration testers to quickly gather critical intelligence about a target domain before starting an assessment.

## ✨ Features
* 🌐 **WHOIS Lookup:** Retrieves domain registration, registrar info, creation, and expiration dates.
* 🛡️ **HTTP Header Analyzer:** Grabs server headers and flags missing security configurations (e.g., HSTS, X-Frame-Options).
* 🔌 **Port Scanner:** Performs a fast TCP port scan on essential services (FTP, SSH, HTTP, HTTPS) to check for open entry points.

---

## 🛠️ Installation & Setup

Follow these simple steps to get `recon-pulse` running on your local machine.

### 1. Clone the Repository
Open your terminal or command prompt and run the following command to download the project files:

git clone https://github.com/sayanssha/recon-pulse.git

cd recon-pulse

pip install -r requirements.txt

python recon_pulse.py example.com

Example Output:-
-------------------------------------------------------
🚀 Recon-Pulse: Automated Reconnaissance Tool
-------------------------------------------------------
Target: example.com
Scan Started: 2026-07-07 00:05:00

[+] Gathering WHOIS Information...
Registrar: MarkMonitor Inc.
Creation Date: 1992-08-14 04:00:00
Expiration Date: 2026-08-13 04:00:00

[+] Fetching HTTP Server Headers...
Server: ECS (nyb/1D1C)
X-Powered-By: Not Set (Potential finding)
Strict-Transport-Security: max-age=63072000; includeSubDomains
X-Frame-Options: SAMEORIGIN

[+] Scanning Common Ports (21, 22, 80, 443)...
Resolved IP: 93.184.215.14
[*] Port 21: CLOSED / FILTERED
[*] Port 22: CLOSED / FILTERED
[!] Port 80: OPEN
[!] Port 443: OPEN

[+] Reconnaissance Complete.
