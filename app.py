from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello World!</h1>
    <p>This is my first website.</p>
    <p>Created by Krishnaraj.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)