"https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=MDzQ2nxmbphA5PHT9xyJuhXZmEL5vChe"
from bs4 import BeautifulSoup
import requests
import json

response= requests.get("https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=MDzQ2nxmbphA5PHT9xyJuhXZmEL5vChe")
json_str = response.text
query_result = json.loads(json_str)
results = query_result['results']
#print(results)
for result in results:
    print(result['title'])