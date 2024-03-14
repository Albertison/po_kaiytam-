from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def requi():
    params = {}
    params['title'] = 'По каютам!'
    return render_template('first.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')