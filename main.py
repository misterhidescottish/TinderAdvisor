from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


git add static/img/*
git commit -m "Aggiunte immagini per il sito"
git push origin main

