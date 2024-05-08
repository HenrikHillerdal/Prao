from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/fritidshem")
def fritidshem():
    return render_template("fritidshem.html")

@app.route("/kontaktaoss")
def kontaktaoss():
    return render_template("kontaktaoss.html")

@app.route("/lst")
def lst():
    return render_template("lst.html")

@app.route("/kurator")
def kurator():
    return render_template("kurator.html")

@app.route("/skolskoterska")
def skolskoterska():
    return render_template("skolskoterska.html")

@app.route("/syv")
def syv():
    return render_template("syv.html")

if __name__ == '__main__':
    app.run(debug=True)
