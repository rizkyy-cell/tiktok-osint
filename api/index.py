from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return {"status": "ok", "message": "Server berjalan!"}

# Untuk Vercel, tidak perlu app.run()