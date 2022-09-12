from flask import Flask, render_template
from biudzetas import zurnalas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/biudzetas")
def biudzetas():
    return render_template('biudzetas.html', zurnalas=zurnalas)

if __name__ == "__main__":
    app.run(debug=True)