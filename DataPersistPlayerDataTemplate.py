import pyodbc
import json

connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=stairway.usu.edu,1433;Database=justinlarson;Uid=;Pwd=';
conn = pyodbc.connect(connection_string, autocommit=True)

curs = conn.cursor()
curs.execute(
    '''
    create table PlayerData01 (
    PlayerID INT,
    LastName CHAR(30),
    FirstName CHAR(30),
    Position CHAR(3),
    TeamID INT,
    Abbreviation CHAR(5),
    GamesPlayed INT,
    Fg2PtAtt INT,
    Fg2PtAttPerGame FLOAT,
    Fg2PtMade INT,
    Fg2PtMadePerGame FLOAT,
    Fg2PtPct FLOAT,
    Fg3PtAtt INT,
    Fg3PtAttPerGame FLOAT,
    Fg3PtMade INT,
    Fg3PtMadePerGame FLOAT,
    Fg3PtPct FLOAT,
    FgAtt INT,
    FgAttPerGame FLOAT,
    FgMade INT,
    FgMadePerGame FLOAT,
    FgPct FLOAT,
    FtAtt INT,
    FtAttPerGame FLOAT,
    FtMade INT,
    FtMadePerGame FLOAT,
    FtPct FLOAT,
    OffReb INT,
    OffRebPerGame FLOAT,
    DefReb INT,
    DefRebPerGame FLOAT,
    Reb INT,
    RebPerGame FLOAT,
    Ast INT,
    AstPerGame FLOAT,
    Pts INT,
    PtsPerGame FLOAT,
    Tov INT,
    TovPerGame FLOAT,
    Stl INT,
    StlPerGame FLOAT,
    Blk INT,
    BlkPerGame FLOAT,
    Fouls INT,
    FoulsPerGame FLOAT,
    FoulsDrawn INT,
    FoulsDrawnPerGame FLOAT,
    Ejections INT,
    PlusMinusPerGame FLOAT,
    GamesStarted INT
    )

    '''
    )
insert_query = 'insert into PlayerData01 (PlayerID,' \
               'LastName,' \
               'FirstName,' \
               'Position,' \
               'TeamID,' \
               'Abbreviation,' \
               'GamesPlayed,' \
               'Fg2PtAtt,' \
               'Fg2PtAttPerGame,' \
               'Fg2PtMade,' \
               'Fg2PtMadePerGame,' \
               'Fg2PtPct,' \
               'Fg3PtAtt,' \
               'Fg3PtAttPerGame,' \
               'Fg3PtMade,' \
               'Fg3PtMadePerGame,' \
               'Fg3PtPct,' \
               'FgAtt,' \
               'FgAttPerGame,' \
               'FgMade,' \
               'FgMadePerGame,' \
               'FgPct,' \
               'FtAtt,' \
               'FtAttPerGame,' \
               'FtMade,' \
               'FtMadePerGame,' \
               'FtPct,' \
               'OffReb,' \
               'OffRebPerGame,' \
               'DefReb,' \
               'DefRebPerGame,' \
               'Reb,' \
               'RebPerGame,' \
               'Ast,' \
               'AstPerGame,' \
               'Pts,' \
               'PtsPerGame,' \
               'Tov,' \
               'TovPerGame,' \
               'Stl,' \
               'StlPerGame,' \
               'Blk,' \
               'BlkPerGame,' \
               'Fouls,' \
               'FoulsPerGame,' \
               'FoulsDrawn,' \
               'FoulsDrawnPerGame,' \
               'Ejections,' \
               'PlusMinusPerGame,' \
               'GamesStarted) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
with open(r'C:\Users\vball\PycharmProjects\Final Project\playerdata20172018.json', 'r') as data_file:
    data = json.load(data_file)
    data_list = data['cumulativeplayerstats']['playerstatsentry']
    rows_to_insert = []
    for item in data_list:
        rows_to_insert.append(tuple([item['player']['ID'],
                                     item['player']['LastName'],
                                     item['player']['FirstName'],
                                     item['player']['Position'],
                                     item['team']['ID'],
                                     item['team']['Abbreviation'],
                                     item['stats']['GamesPlayed']['#text'],
                                     item['stats']['Fg2PtAtt']['#text'],
                                     item['stats']['Fg2PtAttPerGame']['#text'],
                                     item['stats']['Fg2PtMade']['#text'],
                                     item['stats']['Fg2PtMadePerGame']['#text'],
                                     item['stats']['Fg2PtPct']['#text'],
                                     item['stats']['Fg3PtAtt']['#text'],
                                     item['stats']['Fg3PtAttPerGame']['#text'],
                                     item['stats']['Fg3PtMade']['#text'],
                                     item['stats']['Fg3PtMadePerGame']['#text'],
                                     item['stats']['Fg3PtPct']['#text'],
                                     item['stats']['FgAtt']['#text'],
                                     item['stats']['FgAttPerGame']['#text'],
                                     item['stats']['FgMade']['#text'],
                                     item['stats']['FgMadePerGame']['#text'],
                                     item['stats']['FgPct']['#text'],
                                     item['stats']['FtAtt']['#text'],
                                     item['stats']['FtAttPerGame']['#text'],
                                     item['stats']['FtMade']['#text'],
                                     item['stats']['FtMadePerGame']['#text'],
                                     item['stats']['FtPct']['#text'],
                                     item['stats']['OffReb']['#text'],
                                     item['stats']['OffRebPerGame']['#text'],
                                     item['stats']['DefReb']['#text'],
                                     item['stats']['DefRebPerGame']['#text'],
                                     item['stats']['Reb']['#text'],
                                     item['stats']['RebPerGame']['#text'],
                                     item['stats']['Ast']['#text'],
                                     item['stats']['AstPerGame']['#text'],
                                     item['stats']['Pts']['#text'],
                                     item['stats']['PtsPerGame']['#text'],
                                     item['stats']['Tov']['#text'],
                                     item['stats']['TovPerGame']['#text'],
                                     item['stats']['Stl']['#text'],
                                     item['stats']['StlPerGame']['#text'],
                                     item['stats']['Blk']['#text'],
                                     item['stats']['BlkPerGame']['#text'],
                                     item['stats']['Fouls']['#text'],
                                     item['stats']['FoulsPerGame']['#text'],
                                     item['stats']['FoulsDrawn']['#text'],
                                     item['stats']['FoulsDrawnPerGame']['#text'],
                                     item['stats']['Ejections']['#text'],
                                     item['stats']['PlusMinusPerGame']['#text'],
                                     item['stats']['GamesStarted']['#text']]))
    curs.executemany(insert_query, rows_to_insert)