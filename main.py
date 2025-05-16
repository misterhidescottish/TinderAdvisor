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


<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TinderAdvisor Abbonamenti Scontati</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <img src="{{ url_for('static', filename='img/logo.png') }}" alt="TinderAdvisor Logo" class="logo">
        <h1>🔥 TinderAdvisor</h1>
        <p>Ti aiutiamo a ottenere più match e attivare l'abbonamento giusto, a un prezzo ridotto.</p>
    </header>

    <section class="piani">
        <h2>💸 Scegli il tuo piano scontato</h2>

        <div class="card">
            <img src="{{ url_for('static', filename='img/plus.jpg') }}" alt="Tinder Plus">
            <h3>🔥 Tinder Plus</h3>
            <ul>
                <li>Swipe illimitati</li>
                <li>Rewind & Passport</li>
                <li>No pubblicità</li>
            </ul>
            <p class="prezzo">Solo 7€</p>
            <a href="https://t.me/TinderAdvisor" target="_blank" class="btn">Acquista ora</a>
        </div>

        <div class="card">
            <img src="{{ url_for('static', filename='img/gold.jpg') }}" alt="Tinder Gold">
            <h3>✨ Tinder Gold</h3>
            <ul>
                <li>Vedi chi ti ha likato</li>
                <li>5 SuperLike a settimana</li>
                <li>1 Boost al mese</li>
            </ul>
            <p class="prezzo">Solo 11€</p>
            <a href="https://t.me/TinderAdvisor" target="_blank" class="btn">Acquista ora</a>
        </div>

        <div class="card">
            <img src="{{ url_for('static', filename='img/platinum.jpg') }}" alt="Tinder Platinum">
            <h3>💎 Tinder Platinum</h3>
            <ul>
                <li>Like prioritari</li>
                <li>Messaggia prima del match</li>
                <li>Visibilità massima</li>
            </ul>
            <p class="prezzo">Solo 15€</p>
            <a href="https://t.me/TinderAdvisor" target="_blank" class="btn">Acquista ora</a>
        </div>
    </section>

    <footer>
        <p>Creato con ❤️ da TinderAdvisor. Nessun abbonamento automatico. Codice digitale via Telegram.</p>
    </footer>
</body>
</html>

body {
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
    background-color: #111;
    color: #fff;
    text-align: center;
}

header {
    padding: 2rem;
}

.logo {
    width: 80px;
    margin-bottom: 1rem;
}

h1 {
    font-size: 2rem;
    color: #00bfff;
}

.piani {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 2rem;
}

.card {
    background-color: #1c1c1c;
    border-radius: 10px;
    width: 280px;
    margin: 1rem;
    padding: 1rem;
    box-shadow: 0 0 20px #00bfff44;
}

.card img {
    width: 100%;
    border-radius: 10px;
}

.card h3 {
    color: #00bfff;
}

.card ul {
    list-style: none;
    padding: 0;
    margin: 0.5rem 0;
}

.card li {
    margin: 0.5rem 0;
}

.prezzo {
    font-size: 1.2rem;
    color: #0f0;
    margin-top: 0.5rem;
}

.btn {
    background-color: #00bfff;
    color: #111;
    text-decoration: none;
    padding: 0.5rem 1.5rem;
    border-radius: 6px;
    font-weight: bold;
    display: inline-block;
    margin-top: 1rem;
}

footer {
    margin-top: 3rem;
    font-size: 0.8rem;
    opacity: 0.6;
    padding: 2rem;
}

