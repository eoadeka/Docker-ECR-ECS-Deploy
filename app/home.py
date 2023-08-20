from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# Predefined list of quotes
quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "In the middle of every difficulty lies opportunity.",
    "The future belongs to those who believe in the beauty of their dreams."
]

@app.route("/")
def home():
 random_quote = random.choice(quotes)
 return render_template('index.html', quote=random_quote)

if __name__ == "__main__":
 port = int(os.environ.get('PORT', 5000))
 app.run(debug=True, host="0.0.0.0", port=port)