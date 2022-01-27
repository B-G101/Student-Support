# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render tab1.html
@app.route('/tab1/')
def kangaroos():
    return render_template("tab1.html")


@app.route('/tab2/')
def walruses():
    return render_template("tab2.html")


@app.route('/tab3/')
def hawkers():
    return render_template("tab3.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
