import os
from flask import Flask

app = Flask(__name__)


def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


@app.route('/')
def primos():
    limite = 100
    primos = "<h1>Números primos</h1><br>"
    pula_linha = 10
    for num in range(2, limite+1):
        ehprimo = primo(num)
        if(ehprimo):
            primos += str(num) + ", "
            pula_linha -= 1
        if(pula_linha == 0):
            primos += "<br>"
            pula_linha = 10
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
