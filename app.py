#importação da biblioteca do Flask, com os métodos adicionados
from flask import Flask, request, jsonify, redirect, url_for, render_template, make_response

app = Flask(__name__)

#ROTA BÁSICA (GET)
@app.route('/')
def home():
    return "Bem-vindo à aplicação Flask."