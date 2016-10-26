from pymongo import MongoClient
from flask import Flask,render_template,request, 

client = MongoClient("localhost",27017)
db = client.plugin2710
student = db.students

app = Flask(__name__)

@app.route("/")
def home():
	return "Welcome!!!!!"

@app.route("/read")
def tasks():
	return render_template('Read_record.html',details=student.find())

@app.route("/create")
def create():
	return render_template('Create_record.html')

@app.route("/create_record",methods=['POST'])
def create_record():
	name = request.values.get("name")
	age = request.values.get("sem")
	print "----------Record created!!!!----------"
	student.insert({"name":name,"sem":sem})
	return redirect("/")

@app.route("/delete")
def delete():
	return render_template('Delete_record.html')

@app.route("/delete_record", methods=['POST'])
def delete_record():
	key = request.values.get("key")
	value = request.values.get("value")
	print "----------Record deleted!!!!----------"
	student.remove({key:value})
	return redirect("/")


@app.route("/update")
def update():
	return render_template('Update_record.html')

@app.route("/update_record")
def update_record():
	print ("------------------")
	print request.values

	ID = request.values.get("id")
	key = request.values.get("key")
	value = request.values.get("value")
	student.update({"_id":ObjectId(ID)}, {'$set':{key:value}})
	return 


if __name__ == "__main__":
	app.run(debug=True)