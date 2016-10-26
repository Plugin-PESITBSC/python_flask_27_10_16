# python_flask_27_10_16


Installation Guildelines : 

1) Install python 2 or 3 according to your system

2) Flask 

Install flask as guided here -- http://flask.pocoo.org/docs/0.11/installation/

3) Install and set up Mongo DB

* Windows 
 
 * Visit  https://www.mongodb.org/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-3.2.4-signed.msi/download and follow the instructions 
 
* Ubuntu 
    a.  Run the following commands : 
    1)sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
    2)
     a)For Ubuntu 16.04:
     echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

    		b)For Ubuntu 14.04:
    		echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

    		c)For Ubuntu 12.04:
    		echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
    		
        3) sudo apt-get update 
        4) sudo apt-get install -y mongodb-org   (This will install the latest version ) 
        5) sudo service mongo start   ( Start the mongodb service)
        
* Final step : 
 Check your mongodb version 
 1) mongo --version 
 2) mongod --version 
