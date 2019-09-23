from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello, World!"
  
if __name__ == "__main__":
    app.run(host='0.0.0.0')
	
# Use it to run: 
# python app.py
# 
# After that will output:
#  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
