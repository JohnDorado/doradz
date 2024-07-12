# app.py
from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Example data for photography services
services = [
    {"name": "Weddings", "description": "Capture the special moments of your wedding day."},
    {"name": "Pre-weddings", "description": "Beautiful pre-wedding photoshoots."},
    {"name": "Events", "description": "Professional event photography for all occasions."},
    {"name": "Birthdays", "description": "Memorable birthday celebrations captured."},
    {"name": "Boudoir", "description": "Elegant and intimate boudoir photography."},
]

@app.route('/services')
def services_page():
    return render_template('services.html', services=services)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Running on port 5001
