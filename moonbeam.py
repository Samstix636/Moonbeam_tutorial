import config
from web3 import Web3

provider_rpc = {
    "development": "http://localhost:9933",
    "alphanet": "https://rpc.testnet.moonbeam.network",
}

# Connect web3 to provider
web3 = Web3(Web3.HTTPProvider(provider_rpc["alphanet"]))
print(web3.isConnected())


# Variables
account_from = {
    "private_key": config.private,
    "address": config.wallet_address,
}
address_to = "0x29c98d169B64Bf66B0C997eb55cC693f92190f79"

# Getting the balance of our wallet
balanceinWei = web3.eth.get_balance(account_from['address'])
balanceinDev= web3.fromWei(balanceinWei, 'ether')


print(
    f'Attempting to send transaction from { account_from["address"] } to { address_to }'
)

# Sign Tx with PK
txn = web3.eth.account.signTransaction(
    {
        "nonce": web3.eth.getTransactionCount(account_from["address"]),
        "gasPrice": web3.toWei('5', 'gwei'),
        "gas": 21000,
        "to": address_to,
        "value": web3.toWei("0.5", "ether")
    },
    account_from["private_key"],
)

# Send signed Txn
tx_hash = web3.eth.sendRawTransaction(txn.rawTransaction)
# receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print('Successful. Txn Hash: ', web3.toHex(tx_hash))