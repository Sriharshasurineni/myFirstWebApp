from flask import Flask

app = Flask("myFirstwebApp")


@app.route('/')
def hello_world():
    return 'Sup, Subscribe'



