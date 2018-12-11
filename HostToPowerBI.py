import pyodbc
from flask import Flask, g, render_template, abort, request
import json


CONNECTION_STRING = 'Driver={ODBC Driver 17 for SQL Server};Server= ,1433;Database=;Uid=justinlarson;Pwd=';


# Setup Flask
app = Flask(__name__)
app.config.from_object(__name__)

# Before / Teardown
@app.before_request
def before_request():
    try:
        g.sql_conn = pyodbc.connect(CONNECTION_STRING, autocommit=True)
    except Exception:
        abort(500, "No database connection could be established.")

@app.teardown_request
def teardown_request(exception):
    try:
        g.sql_conn.close()
    except AttributeError:
        pass

@app.route('/')
def default():
    print('Anything is Possible!!! -Kevin Garnett''\n')
    print("We're talkin about practice??? - Allen Iverson"'\n')
    print('Donovan Mitchell is the GOAT - me, probably')
    return 'Welcome to the Landing Page for Player Stats from the 2017-2018 NBA Regular Season'

@app.route('/api/v1/PlayerData01', methods = ['GET'])
def get_all_the_data():
    curs = g.sql_conn.cursor()
    query = 'select * from justinlarson.dbo.PlayerData01'
    curs.execute(query)

    columns = [column[0] for column in curs.description]
    data = []

    for row in curs.fetchall():
        data.append(dict(zip(columns, row)))

    return json.dumps(data, indent =5, sort_keys=True, default=str)

@app.route('/api/v1/standings', methods = ['GET'])
def get_all_the_standings():
    curs = g.sql_conn.cursor()
    query = 'select * from justinlarson.dbo.Standings'
    curs.execute(query)

    columns = [column[0] for column in curs.description]
    data = []

    for row in curs.fetchall():
        data.append(dict(zip(columns, row)))

    return json.dumps(data, indent =5, sort_keys=True, default=str)



if __name__ == '__main__':
    app.run(host="0.0.0.0")
