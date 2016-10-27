from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('Home.html')

@app.route('/language/<lang>')
def hello_user(lang):
   if lang =='python':
    	return redirect(url_for('python_func'))
   elif lang == 'java':
    	return redirect(url_for('java_func'))
   else:
   		return redirect(url_for('home'))

@app.route('/python')
def python_func():
	return render_template('Python.html')

@app.route('/java')
def java_func():
	return render_template('Java.html')

if __name__ == '__main__':
   app.run(debug = True)
