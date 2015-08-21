from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "We are clear. It is clearstride!"

if __name__ == '__main__':
    app.run()
