import requests
from bs4 import BeautifulSoup

url = "http://www.ams.sunysb.edu/~tucker/ams301.html"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

seperator = "explanation to "
text2 = text.split(seperator)[1]
lines = text2.split("\n")
email = lines[0]
lines.pop(0)

puzzles = []
for line in lines:
	if line.isspace():
		continue
	if "week" in line.lower():
		break
	puzzles.append(line)

for line in puzzles:
	print(line)
