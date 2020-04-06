from flask import Flask, url_for   


app = Flask(__name__)     

@app.route("/")           
def hello():              
	return "Welcome !" 

@app.route("/hello")           
def hello():              
	return "Hello World!"

if __name__ == "__main__":
	app.run()             
