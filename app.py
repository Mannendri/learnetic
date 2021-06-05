from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    # ---Display all study sets---
    # Code below
    return render_template("index.html")

@app.route('/create', methods=["GET","POST"])
def create():
    if request.method == 'POST':
        # ---Create a study set in the db with its title and description---
        # Code below

        # ---Create a new flashcard in the db for every flashcard that was inputted in the form---
        # Code below
        pass
    return render_template("create.html")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')