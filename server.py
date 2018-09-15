from flask import Flask, render_template, jsonify
import json
from web_scraper import get_guesses

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solver')
def solver():
	return render_template('solver.html')

@app.route('/solution')
def solution():
	return render_template('tucker_solution.html')

@app.route('/solve')
def solve():
	guesses = request.args.guesses

@app.route('/get_guesses')
def guesses():
	guesses = get_guesses()
	return jsonify(sequence=guesses[0].sequence, num_whites=guesses[0].num_whites, num_blacks=guesses[0].num_blacks)

if __name__ == '__main__':
   app.run(debug = True)