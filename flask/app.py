from flask import Flask, render_template, request,url_for,redirect

app=Flask(__name__,template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/food")
def food():
    return render_template("food.html")
    

if __name__=='__main__':
    app.run(debug=True)