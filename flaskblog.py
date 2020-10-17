from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Noah Perry',
        'title': 'Title Test!',
        'content': 'content boi',
        'date_posted': 'April 1, 2020'
    },
    {
        'author': 'Kayla Perry',
        'title': 'Content2',
        'content': 'More content!',
        'date_posted': 'April 2, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/legal/license")
def license():
    return render_template('license.html')



if __name__ == "__main__":
    app.run(debug=True)
