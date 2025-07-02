import requests

# === CONFIGURATION ===
TELEGRAM_BOT_TOKEN = '7910847201:AAG5eorIYAaRmVsCwqXEjoOGsv6uKdw7sj4'
TELEGRAM_CHAT_ID = '@billboardbot256'  # Or use your numeric chat ID

# === 1. Set your fixed post content ===
def generate_post():
    return "Drake is a Canadian artist born in 1986 and has won 5 Grammys as of July 2025"

# === 2. Send message to Telegram ===
def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'Markdown'  # Optional
    }

    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("Message sent to Telegram.")
    else:
        print("Failed to send message.")
        print(response.text)

# === 3. Main execution ===
if __name__ == "__main__":
    post = generate_post()
    print("Sending Post:\n", post)
    send_to_telegram(post)
