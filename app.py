
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from service.operations import mysum

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route('/hello')
def hello_world():
    return 'Hello'

@app.route('/sum')
def sum():
    return str(mysum(3, 5))

def create_app():
   return app

if __name__ == '__main__':
    app.run()
