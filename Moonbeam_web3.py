#pip install web3
import config
from web3 import Web3

provider_rpc = {
    "development": "http://localhost:9933",
    "alphanet": "https://rpc.testnet.moonbeam.network",
    'moonriver_mainnet' : 'https://rpc.moonriver.moonbeam.network'
}

web3 = Web3(Web3.HTTPProvider(provider_rpc['alphanet']))
print(web3.isConnected())

#check balance
addy = web3.toChecksumAddress("0x39DC57cf562736D62bE25EFC1B37ce43dEaf51Bc")

balanceinwei = web3.eth.get_balance(addy)
balanceinEth = web3.fromWei(balanceinwei, 'ether')
print(balanceinEth)

#Send transaction
account_from = {
    'private_key': config.private,
    'address': web3.toChecksumAddress("0x39DC57cf562736D62bE25EFC1B37ce43dEaf51Bc")
}

account_to = web3.toChecksumAddress("0x29c98d169B64Bf66B0C997eb55cC693f92190f79")

print('Attempting to send a transaction')

transaction = web3.eth.account.sign_transaction(
    {
        'nonce': web3.eth.getTransactionCount(account_from['address']),
        'gasPrice': web3.toWei('5', 'gwei'),
        'gas': 21000,
        'to': account_to,
        'value': web3.toWei('1', 'ether')
    },
    account_from['private_key']
)

tx_hash = web3.eth.sendRawTransaction(transaction.rawTransaction)

print(f'Transaction hash: {web3.toHex(tx_hash)}')







