from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/create', methods=["GET","POST"])
def create():
    return render_template("create.html")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')