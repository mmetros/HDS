import sqlite3
from flask import render_template, make_response,request
from flask_restful import Resource



class Manufacturer(Resource):

    @classmethod
    def find_by_name(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM manufacturers WHERE name=?",(name,))
        row = cursor.fetchone()
        if row:
            return row
        else:
            return None

    @classmethod
    def update(self, manufacturer):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()


        cursor.execute("UPDATE manufacturers SET link=?,logo=?  WHERE name=?",(name,link,logo))
        row = cursor.fetchone()
        if row:
            return row
        else:
            return "Manufacturer Not Found"

    def get(self, name):
        row = self.find_by_name(name)
        if row:
            return row

        else:
            return "Manufacturer Not Found"

    def post(self, name):
         request.form

class Manufacturers(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM manufacturers")
        rows = cursor.fetchall()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('manufacturers.html', rows=rows), 200, headers)
