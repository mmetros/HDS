from flask import Flask, render_template, request, jsonify
from flask_restful import Api
import sqlite3



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


@app.route('/_background_process')
def _background_process():
    name = request.args.get('name')
    link = request.args.get('link')
    logo = request.args.get('logo')
    if find_by_name(name, link, logo):
        update(name, link, logo)
        return jsonify(result = "{} has been updated with the following info: Name: {}, Link: {}, Logo: {}".format(name, name,link,logo))
    else:
        if None:
            return
        else:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "INSERT INTO manufacturers VALUES (?,?,?)"
            result = cursor.execute(query, (name, link, logo))
            connection.commit()
            connection.close()
            return jsonify(result = "The following has been added: Name: {}, Link: {}, Logo: {}".format(name,link,logo))


def find_by_name(name, link, logo):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "SELECT * FROM manufacturers WHERE name=?"
    result = cursor.execute(query, (name,))
    row = cursor.fetchone()
    # Row will return a tuple

    connection.close()
    if row:
        if row[0] == name and row[1] == link and row[2] == logo:
            return True
    else:
        return False

def update(name, link, logo):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "UPDATE manufacturers SET link=?, logo=? WHERE name=?"
    result = cursor.execute(query,(link,logo, name))
    connection.commit()
    connection.close()


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

if __name__ == "__main__":
    app.run(port=5000, debug=True)
