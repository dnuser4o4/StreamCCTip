import time

import bin

networks = bin.configRead.networks

oldLatestTx = None

def checkLatest(response, oldLatestTx):
    if oldLatestTx == response:
        return 1
    

while True:
    for network in networks:
        # Native coin
        response = bin.apiRequest.apiRequest(network)
        print(response)
        if checkLatest(response, oldLatestTx) != 1:
            latestTx = response[0]["hash"]
            value_eth = int(response[0]["value"]) / 1e18
            print(f"[{network}] New donation: {value_eth} native coin from {response[0]['from']}")
            oldLatestTx = response
#
#        # ERC20 tokens
#        token_txs = get_token_txs(name, chain_id)
#        if token_txs:
#            latest = token_txs[0]["hash"]
#            if latest != last_token_tx[name]:
#                token = token_txs[0]["tokenSymbol"]
#                decimals = int(token_txs[0]["tokenDecimal"])
#                value_token = int(token_txs[0]["value"]) / (10 ** decimals)
#                print(f"[{name}] New token donation: {value_token} {token} from {token_txs[0]['from']}")
#                last_token_tx[name] = latest

#    time.sleep(10)  # poll every 10 seconds
