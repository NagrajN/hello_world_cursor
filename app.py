from flask import Flask, render_template

app = Flask(__name__)

# Sample news articles
articles = [
    {
        "title": "Python 3.13 Released",
        "summary": "The latest version of Python brings improved performance and new features for developers worldwide."
    },
    {
        "title": "AI Models Reach New Heights",
        "summary": "Recent advances in machine learning demonstrate unprecedented capabilities in natural language processing."
    },
    {
        "title": "Tech Companies Report Strong Earnings",
        "summary": "Major tech firms announce record profits driven by increased cloud adoption and AI integration."
    }
]

@app.route("/")
def home():
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
