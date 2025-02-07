from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account.signers.local import LocalAccount

from data.config import private_key, seed, arb_rpc, eth_rpc


def get_private_from_seed(seed: str) -> str:
    web3 = Web3(provider=Web3.HTTPProvider(endpoint_uri=arb_rpc))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.account.enable_unaudited_hdwallet_features()
    web3_account: LocalAccount = web3.eth.account.from_mnemonic(seed)

    private_key = web3_account._private_key.hex()
    address = web3_account.address
    return private_key


#Подключение
web3 = Web3(Web3.HTTPProvider(endpoint_uri='https://bsc-dataseed1.bnbchain.org'))
print(f'Is connected: {web3.is_connected()}')

# Получение параметров из блокчейна
print(f'gas price: {web3.eth.gas_price} BNB')
print(f'current block number: {web3.eth.block_number}')
print(f'number of current chain is {web3.eth.chain_id}')
#
# Проверка баланса
wallet_address = Web3.to_checksum_address('0x6ba4644463dc53a227653f35c86e8aca64fdebaa')
balance = web3.eth.get_balance(wallet_address)
print(f'balance of {wallet_address} = {balance}')

# # перевод в разные системы измерения
# ether_balance = Web3.from_wei(balance, 'ether')
# print(ether_balance)
# print(Web3.from_wei(balance, 'qwei'))
# print(Web3.to_wei(ether_balance, 'ether'))

# получение приватного ключа из сид фразы
private_key = get_private_from_seed(seed=seed)
print(private_key)
