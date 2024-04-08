from web3 import Web3
from typing import Optional
import requests

from models import DefaultABIs, TokenAmount
from utills import read_json
from data.config import TOKEN_ABI


class Client:
    default_abi = read_json(TOKEN_ABI)


    def __init__(
            self,
            private_key: str,
            rpc: str
    ):
        self.private_key = private_key
        self.rpc = rpc
        self.w3 = Web3(Web3.HTTPProvider(endpoint_uri=self.rpc))
        self.address = Web3.to_checksum_address(self.w3.eth.account.from_key(private_key=private_key).address)


    def get_decimals(self, contrack_address: str):
        return int(self.w3.eth.contract(
            address=Web3.to_checksum_address(contrack_address),
            abi = Client.default_abi
        ).functions.decimals().call

