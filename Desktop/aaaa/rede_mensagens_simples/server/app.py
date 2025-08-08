import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('mensagens.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')
    c.execute('''CREATE TABLE IF NOT EXISTS mensagens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    remetente TEXT,
                    destinatario TEXT,
                    conteudo TEXT)''')
    conn.commit()
    conn.close()

# Suas rotas aqui (igual você já tem) ...

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))  # Usa a porta do Render ou 5000 como fallback
    app.run(host='0.0.0.0', port=port)        # Escuta em todas interfaces
