from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import json
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

        name = request.form.get('Title')
        description = request.form.get('Description')

        conn = sqlite3.connect('/static/data/studysets.db')
        cursor = conn.cursor()
        cursor.execute("insert into sets (name, description) values((?),(?))",(name,description))
        conn.commit()
        conn.close()


        # ---Create a new flashcard in the db for every flashcard that was inputted in the form---
        # Code below
        term = request.form.get('Term')
        answer = request.form.get('Answer')

    return render_template("create.html")

@app.route('/study', methods=["GET","POST"])
def study():
    conn = sqlite3.connect("./static/data/studysets.db")
    curs = conn.cursor()
    if request.method=="POST":
        study_set = request.form.get("set")
        
        current_set={}
        rows = curs.execute("SELECT * FROM sets WHERE name='"+str(study_set)+"'")
        for row in rows:
            current_set = {'rowid':row[0],'name':row[1], 'description':row[2]}
        flashcards=[]
        rows = curs.execute("SELECT * FROM flashcards WHERE set_id=" + str(current_set['rowid']))
        for row in rows:
            flashcard = {'rowid':row[0],'set_id':row[1], 'term':row[2], 'definition':row[3]}
            flashcards.append(flashcard)

    conn.close() 
    return render_template("study.html", study_set=study_set, flashcards=flashcards)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')



