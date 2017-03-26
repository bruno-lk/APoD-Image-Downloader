# python3

import urllib.request
import urllib.error
from html.parser import HTMLParser

# Astronomy Picture of the Day
URL = 'https://apod.nasa.gov/apod/astropix.html'
imgURL = 'http://apod.nasa.gov/apod/' # incompleta

# acha a tag referente a imagem original
# https://docs.python.org/3/library/html.parser.html
# formato: <a href="image/XXX/XXX.jpg">
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					# if value[len(value)-3:len(value)]=="jpg" and value[0:5] == "image":
					if value.startswith('image') and value.endswith('jpg'):
						# print (imgURL + value)
						self.output=value

try:
	# abre URL, enviando requisição
	response = urllib.request.urlopen(URL)
except urllib.error.HTTPError as e:
	print(e.code)
	# print(e.read())
else:
	# armazena resposta do servidor
	html = response.read() # This response is a file-like object

parser = MyHTMLParser()
parser.feed(html.decode('utf-8'))
imgURL = imgURL + parser.output
print (imgURL)