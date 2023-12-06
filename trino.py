from flask import Flask, render_template, request

app = Flask(__name__)

class Complex:
    def __init__(self, x, y):
        self.real = x
        self.img = y

    def assign(self, x, y):
        self.real = x
        self.img = y

    def create(self):
        if self.img >= 0:
            return f"La partie imaginaire est positive ou nulle ({self.real} + {self.img}i)"
        else:
            return f"La partie imaginaire est négative ({self.real} + {self.img}i)"

    def mul(self, a, b, c, d):
        e = a * c - b * d
        f = a * d + b * c
        return f"Résultat de la multiplication : {e} + {f}i"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    x = float(request.form['real'])
    y = float(request.form['img'])

    complex_number = Complex(x, y)
    create_result = complex_number.create()
    mul_result = complex_number.mul(2, 1, 5, 2)

    return render_template('result.html', create_result=create_result, mul_result=mul_result)
# Route spéciale pour servir les fichiers statiques (images, etc.)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)