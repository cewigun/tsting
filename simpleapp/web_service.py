import flask
import http
import json
import os
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = flask.Flask(__name__)


@app.route("/")
def hello():
    print(">>>>>>>>>>>>>>>")
    targethost = os.environ['targethost']
    print(">>>>>>>>>>>>>>> " + targethost)
    conn = http.client.HTTPConnection(targethost)
    conn.request("GET", "/")
    response = json.loads(conn.getresponse().read().decode("utf-8"))
    response["test"] = "added"
    conn.close()
    return flask.jsonify(response)


@app.route("/healthcheck")
def health():
    return flask.jsonify({
        "status": "ok"
    })


@app.route("/healthcheck/fail")
def health_fail():
    return flask.jsonify({
        "status": "error"
    }), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0")
