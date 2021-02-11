from flask import Flask
#from ddtrace import tracer
import os

# tracer.configure(
#     hostname='datadog',
#     port=8126,
# )

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
