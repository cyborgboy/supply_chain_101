# app.py

import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Read quotes from the JSON file created by Scrapy
    with open('quotes.json', 'r') as f:
        quotes = json.load(f)
    return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(debug=False)
