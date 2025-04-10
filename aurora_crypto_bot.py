import requests
import feedparser
import time

BOT_TOKEN = '8162793103:AAFDevvF3POq-Ojg086KY84WOS4Q7-wo8Zg'
CHAT_ID = '6092168721'
RSS_URL = 'https://www.coindesk.com/arc/outboundfeeds/rss/'
CHECK_INTERVAL = 600  # 10分钟

sent_titles = set()

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'HTML'}
    requests.post(url, data=payload)

def fetch_and_send_news():
    feed = feedparser.parse(RSS_URL)
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        if title not in sent_titles:
            message = f"<b>{title}</b>\n{link}"
            send_telegram_message(message)
            sent_titles.add(title)

if __name__ == "__main__":
    while True:
        fetch_and_send_news()
        time.sleep(CHECK_INTERVAL)
