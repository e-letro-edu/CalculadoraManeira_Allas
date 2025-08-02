from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)  # ← habilita CORS para todas as rotas

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"

def power(a, b):
    return a ** b

def module(a, b):
    return a % b

def square_root(a, _=None):
    return math.sqrt(a)

operationDictionary = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "**": power,
    "%": module,
    "V": square_root
}

@app.route("/calcular", methods=["POST"])
def calcular():
    dados = request.get_json()
    a = dados.get("a")
    b = dados.get("b")
    operacao = dados.get("operacao")

    if operacao not in operationDictionary:
        return jsonify({"erro": "Operação inválida"}), 400

    try:
        resultado = operationDictionary[operacao](a, b)
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
