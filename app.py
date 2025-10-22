from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/numero/<int:num>')
def evaluar_numero(num):
    etiqueta = "par" if num % 2 == 0 else "impar"
    return jsonify({
        "numero": num,
        "etiqueta": etiqueta
    })

if __name__ == '__main__':
    app.run(debug=True)
