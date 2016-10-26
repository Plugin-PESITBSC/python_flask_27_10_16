
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return "<html><body><h1>Hello World!</h1></body></html>"

@app.route("/using_render_template/")
def template():
   return render_template('Hello.html')

if __name__ == '__main__':
   app.run(debug = True)