from flask import Flask, request
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

products=[]

@app.get("/api/products")
def read_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    item=request.get_json()
    products.append(item)
    print(item)
    return json.dumps(item)

app.run(debug=True)