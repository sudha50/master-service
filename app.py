import os
import requests
from flask import Flask, request

from messages import make_response
import config

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    payload = {
                "message": "welcome to the master microservice",
                "status": "success"
            }
    return make_response(payload, 200)


@app.route("/sum", methods=["POST"])
def sum():
    list = request.get_json()['list']
    payload = {
               "list": list
            }
    response = requests.post(f'http://{config.SUM_HOST}:{config.SUM_PORT}/sum', json=payload)
    return make_response(response.json(), 200)

@app.route("/mul", methods=["POST"])
def mul():
    list = request.get_json()['list']
    payload = {
               "list": list
            }
    response = requests.post(f'http://{config.MUL_HOST}:{config.MUL_PORT}/mul', json=payload)
    return make_response(response.json(), 200)


if __name__ == "__main__":
    app.run(debug=config.DEBUG_MODE, host="0.0.0.0", port=8000)