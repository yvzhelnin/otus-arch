import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello with love from ' + os.environ['HOSTNAME'] + '!\n'

@app.route("/health")
def health_check():
    return '{"status": "OK"}\n'

@app.route("/version")
def version():
    return '{"version": 0.6}\n'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = '80')
