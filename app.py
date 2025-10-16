print("hil")
from flask import Flask
#app da object mn Flask class
# w klmt __name__ btshow the particular script was invoked
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hellxo,d!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)