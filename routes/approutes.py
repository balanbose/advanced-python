from config import app

@app.get("/hello")
def hello():
    return "Flass app is running now !!!"

@app.get("/hi")
def hi():
    return "Hi, How are you"