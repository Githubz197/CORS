from flask import Flask, request, Response, flash, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
CORS(app)


@app.route("/live")
def live():
    flash("We are LIVE")
    return render_template('live.html')

@app.route('/proxy/<path:url>')
def proxy(url):
    response = requests.get(url)
    headers = {'Content-Type': 'application/json'}
    return Response(response.content, status=response.status_code, headers=headers)

@app.route('/html/<path:url>')
def getHTML(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return Response(response.content, status=response.status_code, headers=headers)

@app.route('/proxyy/<path:url>', methods=['GET', 'POST'])
def proxyy(url):
    if request.method == 'POST':
        data = request.get_json()
        response = requests.post(url, json=data)
    else:
        response = requests.get(url)
    headers = {'Content-Type': 'application/json'}
    return Response(response.content, status=response.status_code, headers=headers)

@app.route('/proxx/<path:url>', methods=['GET', 'POST'])
def proxx(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    target_headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    payload = "channel=popazik"
    response = requests.post(url, headers={**headers, **target_headers}, data=payload)
    headers = {'Content-Type': 'text/html'}
    return Response(response.content, status=response.status_code, headers=headers)

if __name__ == '__main__':
    app.run()
