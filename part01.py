from flask import Flask, request

app = Flask(__name__)
    
@app.route('/', methods = ['POST'])
def api_message():
    SERVER_PASSWORD = "aa"
    if request.headers['Content-Type'] == 'application/json':
        for k, v in request.get_json().items():
            client_password=v
        if client_password == SERVER_PASSWORD:
            return "Access Granted", 200
        else:
            return "Access Denied", 403
    else:
        return "415 Unsupported Media Type"