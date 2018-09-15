import requests
from bs4 import BeautifulSoup
from Guess import Guess

# extract raw text from html page
url = "http://www.ams.sunysb.edu/~tucker/ams301.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

# obtain email address and list of guess strings
seperator = "explanation to "
text2 = text.split(seperator)[1]
lines = text2.split("\n")
email = lines[0]
lines.pop(0)
puzzles = []
'''
for i in range(0,10):
	print(lines[i])
'''
for line in lines:
	if line.isspace() or not line:
		continue
	if "week" in line.lower():
		break
	puzzles.append(line)
	
# obtain guess arrays
attempts = []	
for line in puzzles:
	attempts.append(line.split())

guesses_sequence = []
guesses_black = []
guesses_white = []

for line in attempts:
	guess = []
	for i in range(4):
		guess.append(line[i])
	guesses_sequence.append(guess)
	if "black" in line: 
		guesses_black.append(line[line.index("black") - 1])
	elif "black," in line: 
		guesses_black.append(line[line.index("black,") - 1])
	else:
		guesses_black.append(0)
	if "white" in line: 
		guesses_white.append(line[line.index("white") - 1])
	elif "white," in line: 
		guesses_white.append(line[line.index("white,") - 1])
	else:
		guesses_white.append(0)

guesses = []
for i in range(len(guesses_sequence)):
	guesses.append(Guess(guesses_sequence, guesses_black, guesses_white))

def get_guesses():
	return guesses