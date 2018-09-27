import sqlite3

# make a connection
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS manufacturers (
                        name text,
                        link text,
                        logo text,
                        product_categories
                    )"""


cursor.execute(create_table)

connection.commit()
connection.close()
