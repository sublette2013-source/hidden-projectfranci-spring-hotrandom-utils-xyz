from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """ [Paste the full HTML_TEMPLATE from the last script I gave you here] """

GAMES = [  # Paste the full GAMES list here ]

@app.route('/')
def home():
    category = request.args.get('category')
    filtered = GAMES if not category or category == 'all' else [g for g in GAMES if g['category'] == category]
    return render_template_string(HTML_TEMPLATE, games=filtered)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
