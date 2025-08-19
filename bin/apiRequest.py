import requests
import bin

def apiRequest(network):
    apiData = bin.configRead.apiData(network)
    if apiData == 1:
        return 1
    
    if network == "etherscan":
        params = {
            "chainid": apiData["chainID"],
            "module": "account",
            "action": "txlist",
            "address": apiData["watchAddress"],
            "sort": "desc",
            "apikey": apiData["apiKey"]
        }
    
    else:
        return 1

    response = requests.get(apiData["apiUrl"], params=params).json()
    if response["status"] == "1" and response["result"]:
        return response["result"]
    return []