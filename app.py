from flask import Flask, render_template
from scraper import get_books

app = Flask(__name__)

@app.route('/')
def index():
    books, alert_books = get_books()
    return render_template('index.html', books=books, alert_books=alert_books)

if __name__ == '__main__':
    app.run(debug=True)
