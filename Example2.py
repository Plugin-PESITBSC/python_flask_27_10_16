from flask import Flask
app = Flask(__name__)

@app.route('/plugin_27_10/<name>')
def hello_name(name):
   return 'Hello %s! Learning Flask Eh? xD ' % name

if __name__ == '__main__':
   app.run(debug = True)