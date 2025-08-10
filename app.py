import feedparser
from flask import Flask, render_template

app = Flask(__name__)

RSS_FEED = "https://www.pbs.org/newshour/feeds/rss/headlines"


@app.route("/")
def home():
    feed = feedparser.parse(RSS_FEED)
    return render_template("index.html", articles=feed.entries)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
