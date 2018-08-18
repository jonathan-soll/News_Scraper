# app.py

from flask import Flask, jsonify
from scraping import scrape
from loop import print_hey

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(Products = scrape())

if __name__ == "__main__":
    app.run(debug=True)
