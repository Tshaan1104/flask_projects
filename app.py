from flask import Flask,make_response
app = Flask(__name__)

@app.route("/")
def index():
    resp = make_response({"msg":"hello"})
    resp.status_code = {204}
    return resp