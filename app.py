from flask import Flask, render_template, request
from flask_restful import Api



app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manufacturers')
def manufacturers():
    return render_template('manufacturers.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
