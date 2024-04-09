import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

ABIS_DIR = os.path.join(ROOT_DIR, 'abis')

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
WOOFI_ABI = os.path.join(ABIS_DIR, 'woofi.json')

private_key = 'address'
seed = '12 words'
eth_rpc = 'https://chainlist.org/chain/2000'
arb_rpc = 'https://rpc.ankr.com/arbitrum'
