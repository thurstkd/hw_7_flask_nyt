"""
this is an example destination
https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=yourkey


In your “top_headlines.py” file, write code to retrieve the top 5 articles from the New
York Times from the technology section. Make sure to include your API key in a file
called “secrets.py”.
"""

from flask import Flask, render_template
import requests
import json
import secrets
app = Flask(__name__)

from bs4 import BeautifulSoup
import requests
import json

response= requests.get("https://api.nytimes.com/svc/topstories/v2/technology.json?api-key="+secrets.API_key)
json_str = response.text
query_result = json.loads(json_str)
results = query_result['results']
headlines = []
for result in results[:5]:
    headlines.append(result['title'])

h1 = headlines[0]
h2 = headlines[1]
h3 = headlines[2]
h4 = headlines[3]
h5 = headlines[4]

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):     
    return render_template('name.html', name=nm, h1=h1, h2=h2, h3=h3, h4=h4, h5=h5)

@app.route('/headlines/<nm>')
def list_headlines(nm):     
    return render_template('top_news.html', name=nm, h1=h1, h2=h2, h3=h3, h4=h4, h5=h5)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)