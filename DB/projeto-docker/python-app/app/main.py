import os
from flask import Flask, jsonify
from database import get_db_connection, close_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Aplicação Python com PostgreSQL no Docker"})

@app.route('/professor')
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id_professor, nome_completo, email, telefone FROM professor')
    users = cursor.fetchall()
    cursor.close()
    close_db_connection(conn)

    return jsonify([
        {"id_professor": user[0], "nome_completo": user[1], "email": user[2], "telefone": user[3]}
        for user in users
    ])

@app.route('/healthcheck')
def healthcheck():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
