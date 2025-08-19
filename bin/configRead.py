import json

with open("config.json") as conf:
    config = json.load(conf)

networks = list(config.keys())

def apiData(network):
    if network == "etherscan":
        return {
            "apiUrl": config[network]["endpoint"]["url"],
            "apiKey": config[network]["userData"]["apiKey"],
            "watchAddress": config[network]["userData"]["address"],
            "chainID": config[network]["endpoint"]["chainIDs"]
        }
    else:
        return 1
        # currently disabled
        #apiUrl = data[network]["endpoint"]["url"]
        #apiKey = data[network]["userData"]["apiKey"]
        #watchAddress = data[network]["userData"]["address"]