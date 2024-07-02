# server/app.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {host}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
# example only- no need to write this out

from app import app
from flask import request

request_context = app.test_request_context()
request_context.push()
