import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def primos():
    limite = 100
    qtdPrimos = 1
    numero = 3
    primos = "<h1>Números primos</h1><br>2,"
    # primos = "2,"

    while qtdPrimos < limite:
        ehprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                ehprimo = 0
                break
        if(ehprimo):
            primos = primos + str(numero) + ","
            qtdPrimos += 1
            if(qtdPrimos % 10 == 0):
                primos = primos + "<br>"
        numero += 1
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
