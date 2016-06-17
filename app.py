from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/")
def hello():
    return send_from_directory('static', 'index.html')


if __name__ == "__main__":

    app.run()
