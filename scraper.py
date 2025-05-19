import requests
from bs4 import BeautifulSoup
from email_alert import send_email_alert  # Make sure this file exists
import os
from dotenv import load_dotenv

load_dotenv()

ALERT_PRICE = 20.00  # You can adjust this threshold

BASE_URL = "https://books.toscrape.com/"

def get_books():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    books = []
    alert_books = []

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        book_cards = soup.select('article.product_pod')

        for book in book_cards:
            title_tag = book.h3.a
            title = title_tag['title']
            link = "https://books.toscrape.com/catalogue/" + title_tag['href']
            price_text = book.find('p', class_='price_color').text.strip()
            price = float(price_text.replace('£', '').replace('Â', ''))

            book_data = {
                'title': title,
                'link': link,
                'price': price
            }

            books.append(book_data)

            if price <= 20.00:  # Alert threshold
                alert_books.append(book_data)

        # Pagination
        next_btn = soup.select_one('li.next a')
        if next_btn:
            next_url = next_btn['href']
            base_url = url.rsplit('/', 1)[0]
            url = f"{base_url}/{next_url}"
        else:
            url = None

    return books, alert_books

