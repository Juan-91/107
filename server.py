from flask import Flask
import json

app=Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask"

@app.get("/about")
def about():
    me={"me":"Juan Montiel Herrera"}
    return json.dumps(me)

@app.get("/footer")
def footer():
    pageName={"pageName":"Organika"}
    return json.dumps(pageName)
# create an API to footer that contains the name of the page (organika)

app.run(debug=True)