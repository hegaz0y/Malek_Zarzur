# HEGAZY Telegram Exploit

## Overview
This is an advanced Telegram penetration testing exploit that allows security researchers to demonstrate vulnerabilities in Telegram's file-sharing system. The exploit leverages video injection techniques to extract user IP addresses when a target interacts with a disguised media file.

## Features
- **IP Logging**: Captures and logs IP addresses of users who open the injected media.
- **Telegram Exploitation**: Uses Telegram's document-sharing feature to deliver the payload.
- **Stealth Mode**: The file appears to be a normal video but executes hidden JavaScript code.
- **Advanced Penetration Testing**: Useful for ethical hackers to assess security flaws.

## How It Works
1. The attacker sends a disguised file via Telegram.
2. When the victim opens the file, a hidden JavaScript snippet fetches their IP address and geolocation.
3. The extracted data is sent to a remote Flask server (`server.py`), which logs the details.
4. The attacker retrieves the logged IP addresses for analysis.

## Installation & Usage
### Prerequisites
- Python 3
- Flask
- Requests
- A Telegram bot API token

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Hegazy/telegram-exploit.git
   cd telegram-exploit
   ```
2. Install dependencies:
   ```bash
   pip install flask flask_cors requests
   ```
3. Start the logging server:
   ```bash
   python server.py
   ```
4. Edit `tg.py` and replace `your_bot_token`, `your_chat_id`, and `your_ip` with the correct values.
5. Run the exploit:
   ```bash
   python tg.py
   ```

## Legal Disclaimer
This tool is intended for educational and security research purposes only. Unauthorized use against systems without permission is illegal. The creator is not responsible for any misuse.

## Author
**Hegazy** - Security Researcher & Ethical Hacker.
