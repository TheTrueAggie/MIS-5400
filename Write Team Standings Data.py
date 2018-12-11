import requests
import base64
import json
data_request = requests.get(
            url="https://api.mysportsfeeds.com/v1.2/pull/nba/2017" + "-" + "2018" + "-" + "regular/overall_team_standings.json",
            headers={
                "Authorization": "Basic "  + base64.b64encode("{}:{}".format("","").encode("utf-8")).decode("ascii")
            }
        )
data = data_request.json()
with open('teamstandings20172018.json', 'w') as outfile:
    json.dump(data, outfile)

