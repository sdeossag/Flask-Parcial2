from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/numero/<int:num>')
def evaluar_numero(num):
    factorial = math.factorial(num)
    etiqueta = "par" if num % 2 == 0 else "impar"
    return jsonify({
        "numero": num,
        "factorial": factorial,
        "etiqueta": etiqueta
    })

if __name__ == '__main__':
    app.run(debug=True)
