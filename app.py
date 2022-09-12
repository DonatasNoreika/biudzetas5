from flask import Flask, render_template, request, redirect
from biudzetas import zurnalas, irasyti_zurnala

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/biudzetas")
def biudzetas():
    return render_template('biudzetas.html', zurnalas=zurnalas)

@app.route("/balansas")
def balansas():
    return render_template('balansas.html', balansas=sum(zurnalas))

@app.route("/prideti", methods=['GET', 'POST'])
def prideti():
    if request.method == "POST":
        suma = float(request.form['suma'])
        zurnalas.append(suma)
        irasyti_zurnala()
        return redirect("biudzetas")
    return render_template('prideti.html')

if __name__ == "__main__":
    app.run(debug=True)