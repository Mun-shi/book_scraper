import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

def send_email_alert(book_title, book_price, book_url):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    subject = f"Price Alert: {book_title}"
    body = f"The book '{book_title}' is now available at £{book_price}!\nCheck it out: {book_url}"

    # Use EmailMessage to support UTF-8 characters like £
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body)  # Automatically uses UTF-8

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
