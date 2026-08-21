from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Server berjalan! Silakan lanjut ke tahap 2."

@app.route('/api/health')
def health():
    return {"status": "ok"}
