from flask import Flask,request,redirect,render_template

app=Flask(__name__)

## there are mainly 4 type of the api command and these commands are --
# 1. post    2. get    3.put(Update)    4.delete



details=[
    {"name":"Sanju","age":23},
    {"name":"Fateh","age":22},
    {"name":"virat","age":35}
    ]
## start with post 
@app.get("/")
def home():
    data=details
    return data



## get the data using the some key
@app.get("/get-player/<string:name>")
def get_name(name):
    for player in details:
        # name=name.lower()
        if player["name"].lower()==name.lower():
            return  player

        
    return {"message":"This player name is not exis't...."}



## Now its time for the data get from the postman....

@app.post("/add-player")
def add_player():
    data=request.get_json()
    details.append(data)
    return {f"{data}":"added sucessfully"}



### as we added the data successfully we need to update the data as well....
@app.put("/update-player")
def update_player():
    data=request.get_json()

    for player in details:
        if player["name"].lower()==data["name"].lower():
            player["name"]=data["name"]
            player["age"]=data["age"]
            return {"message":"player updated Sucessfully...."}
    return {"message":"No player exist for the updatation...."}, 404



## Delete-data in API
@app.delete("/delete-player/<string:name>")
def delete_player(name):
    for player in details:
        if player["name"].lower()==name.lower():
            details.remove(player)

            return {"message":f"{name} is deleted Sucessfully...."}
        
    return {"Alert":f"{name} is not exist..."}, 404





if __name__=="__main__":
    app.run(debug=True)