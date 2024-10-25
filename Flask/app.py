from flask import Flask,json

app=Flask(__name__)

## there are mainly 4 type of the api command and these commands are --
# 1. post    2. get    3.update    4.delete

## start with post 
@app.route("/",methods=["GET"])
def home():
    return "This si home page...."




if __name__=="__main__":
    app.run(debug=True)