from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def post_json_handler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
 
app.run(host='0.0.0.0', port= 8090)