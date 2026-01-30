from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Application Succesfully deployed on my EC2 Instance"

app.run(host="0.0.0.0", port=5000)
