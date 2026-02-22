from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample news articles
articles = [
    {
        "id": 1,
        "title": "Python 3.13 Released",
        "summary": "The latest version of Python brings improved performance and new features for developers worldwide.",
        "content": "Python 3.13 has been officially released with groundbreaking improvements to performance and functionality. The release includes enhanced error messages that make debugging easier for developers, a new performance monitoring framework, and significant improvements to the type system. The new version is approximately 10% faster than Python 3.12, making it an ideal choice for performance-critical applications. Key features include improved asyncio capabilities, better support for type annotations, and a completely redesigned error handling system that provides clearer, more actionable error messages. The community has already begun migrating their projects to take advantage of these improvements.",
        "date": "February 20, 2026"
    },
    {
        "id": 2,
        "title": "AI Models Reach New Heights",
        "summary": "Recent advances in machine learning demonstrate unprecedented capabilities in natural language processing.",
        "content": "Recent breakthroughs in artificial intelligence have pushed the boundaries of what's possible with machine learning. New models demonstrate unprecedented capabilities in understanding context, nuance, and complex reasoning across multiple languages and domains. Researchers have achieved state-of-the-art performance on benchmark tests, with models showing remarkable improvement in zero-shot learning and transfer learning scenarios. The latest developments include multimodal models that can seamlessly process text, images, and audio, opening new possibilities for applications in healthcare, education, and scientific research. Industry experts believe these advances will accelerate the adoption of AI across various sectors in the coming years.",
        "date": "February 21, 2026"
    },
    {
        "id": 3,
        "title": "Tech Companies Report Strong Earnings",
        "summary": "Major tech firms announce record profits driven by increased cloud adoption and AI integration.",
        "content": "Leading technology companies have reported record-breaking financial results for the latest quarter, driven primarily by strong cloud services revenue and increased adoption of AI solutions. Cloud computing platforms continue to experience explosive growth as businesses accelerate their digital transformation initiatives. The surge in demand for artificial intelligence services has become a major revenue driver, with companies investing heavily in AI infrastructure and research. Market analysts predict continued growth in the coming quarters as more enterprises embrace cloud-native architectures and integrate AI into their core business operations. The report indicates that cybersecurity and data analytics remain critical focus areas for technology investments.",
        "date": "February 22, 2026"
    }
]

@app.route("/")
def home():
    return render_template("index.html", articles=articles)

@app.route("/article/<int:article_id>")
def article(article_id):
    article = next((a for a in articles if a["id"] == article_id), None)
    if article is None:
        abort(404)
    return render_template("article.html", article=article)

if __name__ == "__main__":
    app.run(debug=True)
