import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello with love from ' + os.environ['HOSTNAME'] + '!'

@app.route("/health")
def health_check():
    return '{"status": "OK"}'

@app.route("/version")
def version():
    return '{"version": 0.6}'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = '80')
