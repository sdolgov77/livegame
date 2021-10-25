from flask import Flask
from flask import render_template
from game_of_life import *

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template('index.html')

@app.route('/live')
def live():
    universe = GameOfLife()
    if universe.counter:
        universe.form_new_generation()
    universe.counter += 1
    return render_template('live.html', life=universe)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)