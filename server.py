
from flask import Flask, render_template

#Flask instance
app = Flask(__name__)

#routes
@app.route('/')
def index():
    obj = [1,5,6,"hello"]
    return render_template("index.html",obj = obj)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name = name)

#ERROR PAGES

#invalid url

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500


#NOTES
"""
Note if generally when we give html to jinja it wont work but we can make it work
using safe
Strip tags will just remove the tags

Jinja Docs 
"""