from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Raise Your Awareness W.A – Level Up From Within"

if __name__ == "__main__":
    app.run(debug=True)
