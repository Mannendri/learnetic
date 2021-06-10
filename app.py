from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    # ---Display all study sets---
    # Code below
    conn = sqlite3.connect("./static/data/studysets.db")
    curs = conn.cursor()
    sets = []
    rows = curs.execute("SELECT * FROM sets")
    for row in rows:
        set = {'id':row[0],'name':row[1], 'description':row[2]}
        sets.append(set)
    conn.close() 
    return render_template("index.html", sets=sets)

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