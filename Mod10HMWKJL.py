import pyodbc
from flask import Flask, g, render_template, abort, request
import json


CONNECTION_STRING = 'Driver={ODBC Driver 17 for SQL Server};Server=,1433;Database=;Uid=;Pwd=;'


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


@app.route('/api/v1/PlayerData01/<string:PlayerID>', methods=['GET'])
def get_playerid(PlayerID):
    curs = g.sql_conn.cursor()
    curs.execute('Select * from justinlarson.dbo.PlayerData01 where PlayerID = ?', PlayerID)

    columns = [column[0] for column in curs.description]
    data = []

    for row in curs.fetchall():
        data.append(dict(zip(columns, row)))

    return json.dumps(data, indent=5, sort_keys=True, default=str)


@app.route('/api/v1/PlayerData01/<string:PlayerID>', methods=['DELETE'])
def delete_single_id(PlayerID):
    curs = g.sql_conn.cursor()
    curs.execute("DELETE from justinlarson.dbo.PlayerData01 where PlayerID = ?", PlayerID)

    curs.commit()
    return 'success', 200


@app.route('/api/v1/PlayerData01', methods = ['POST'])
def adding_items():
    data = request.get_json()

    curs = g.sql_conn.cursor()

    query = 'insert into justinlarson.dbo.PlayerData01 (PlayerID, FirstName, LastName) VALUES (?,?,?)'

    if isinstance(data, dict):
        curs.execute(query, data['PlayerID'], data['FirstName'], data['LastName'])


    if isinstance(data, list):
        for row in data:
            curs.execute(query, row['PlayerID'], row['FirstName'], row['LastName'])

    return 'success', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
