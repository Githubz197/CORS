from flask import Flask, request, Response, flash, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
CORS(app)


@app.route("/status")
def ServerStatusLive():
    flash("We are LIVE")
    return render_template('live.html')

@app.route("/live")
def WhoisLive():
    return render_template('online.html')

# Font Calvin S - ASCII ART

# ╔═╗┌─┐┌┬┐
# ║ ╦├┤  │ : Request Get
# ╚═╝└─┘ ┴ 

#@app.route('/proxy/<path:url>')  THIS WAS THE ORIGINAL, but I changed to /json/:
@app.route('/json/<path:url>')
def getJson(url):
    response = requests.get(url)
    response_headers = {'Content-Type': 'application/json'}
    return Response(response.content, status=response.status_code, headers=response_headers)

@app.route('/text/<path:url>')
def getText(url):
    response = requests.get(url)
    response_headers = {'Content-Type': 'text/plain'}
    return Response(response.content, status=response.status_code, headers=response_headers)

@app.route('/download/<path:url>') # it doesnt know the type to display it so it downloads it?
def getDownload(url):
    response = requests.get(url)
    response_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return Response(response.content, status=response.status_code, headers=response_headers)


#Alternative way declaring headers twice adds both to the dictionary "headers"
@app.route('/html/<path:url>')
def getHTML(url):
    request_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=request_headers)
    response_headers = {'Content-Type': 'text/html'}
    return Response(response.content, status=response.status_code, headers=response_headers)
 
@app.route('/notype/<path:url>') # same as HTML but doesnt specify the RETURN RESPONSE type in headers
def getHTMLL(url):
    request_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=request_headers)
    return Response(response.content, status=response.status_code)

@app.route('/proxyif/<path:url>', methods=['GET', 'POST']) #both are JSON... redundant?
def proxyif(url):
    if request.method == 'POST':
        data = request.get_json()
        response = requests.post(url, json=data)
    else:
        response = requests.get(url)
    response_headers = {'Content-Type': 'application/json'}
    return Response(response.content, status=response.status_code, headers=response_headers)


# ╔═╗┌─┐┌─┐┌┬┐
# ╠═╝│ │└─┐ │ : Request Post
# ╩  └─┘└─┘ ┴ 

# method GET happens when accesing the page that triggers the request.POST and returns a RESPONSE

@app.route('/post/<path:url>', methods=['GET', 'POST']) # the methods just mean you can access and send
def post(url):
    request_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.post(url, headers=request_headers)
    response_headers = {'Content-Type': 'text/html'}
    return Response(response.content, status=response.status_code, headers=response_headers)

@app.route('/twi/<path:url>', methods=['GET', 'POST'])
def twi(url):
    target_headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    
    if request.method == 'POST':
        username = request.form['channel']
        payload = f"channel={username}"
    else:
        payload = None
        
    response = requests.post(url, headers=target_headers, data=payload)
    response_headers = {'Content-Type': 'text/html'}
    return Response(response.content, status=response.status_code, headers=response_headers)


if __name__ == '__main__':
    app.run()
