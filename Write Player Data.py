import requests
import base64
import json
data_request = requests.get(
            url="https://api.mysportsfeeds.com/v1.2/pull/nba/2017" + "-" + "2018" + "-" + "regular/cumulative_player_stats.json",
            headers={
                "Authorization": "Basic "  + base64.b64encode("{}:{}".format("","").encode("utf-8")).decode("ascii")
            }
        )
data = data_request.json()
with open('playerdata20172018.json', 'w') as outfile:
    json.dump(data, outfile)

