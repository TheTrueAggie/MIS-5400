import pyodbc
import json

connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=,1433;Database=;Uid=;Pwd='
conn = pyodbc.connect(connection_string, autocommit=True)

curs = conn.cursor()
curs.execute(
    '''
    create table Standings (
    TeamID INT,
    Abbreviation CHAR(3),
    Rank INT,
    Wins INT,
    Losses INT 
    )

    '''
    )
insert_query = 'insert into Standings (TeamID,' \
               'Abbreviation,' \
               'Rank,' \
               'Wins,' \
               'Losses) VALUES(?,?,?,?,?)'
with open(r'C:\Users\jl9de\PycharmProjects\MIS5400\FinalProject\teamstandings20172018.json', 'r') as data_file:
    data = json.load(data_file)
    data_list = data['overallteamstandings']['teamstandingsentry']
    rows_to_insert = []
    for item in data_list:
        rows_to_insert.append(tuple([item['team']['ID'],
                                     item['team']['Abbreviation'],
                                     item['rank'],
                                     item['stats']['Wins']['#text'],
                                     item['stats']['Losses']['#text']]))
    curs.executemany(insert_query, rows_to_insert)