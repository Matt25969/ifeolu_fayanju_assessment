from flask import render_template
from front import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/chara')
def character():
    return render_template('character.html', title='Character')

@app.route('/party')
def party():
    return render_template('party.html', title='Party')

