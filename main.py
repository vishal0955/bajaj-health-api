from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    r = requests.get('https://hiring.bajajfinservhealth.in/api/renderMe')
    data = r.text
    parse_json = json.loads(data)
    lst = []
    for item in parse_json:
        login = item['login']
        avatar_url = item['avatar_url']
        html_url = item['url']['html_url']
        types = item['type']
        lst.append({"login":login, "avatar_url":avatar_url, "html_url":html_url, "type":types})
    return render_template('index.html', lst=lst)

if __name__ == '__main__':
  app.run(debug=True)
