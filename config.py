import os
import sys
from pathlib import Path
from loguru import logger
from py_okx_async.models import OKXCredentials

max_gwei = 10
shuffle_wallets = True
ethereum_rpc = 'https://eth.drpc.org'
arbitrum_rpc = 'https://arbitrum-one.public.blastapi.io'

sleep = {"from": 1000, "to": 1400}
nft_per_wallet = {'from': 4, 'to': 5}  # максимально возможно 5 на акк

# OKX data
okx_api_key = ''
okx_secret_key = ''
okx_passphrase = ''
withdraw_amount = {'from': 0.001, 'to': 0.002, 'step': 5}






################################
# не трогать
################################
okx_credentials = OKXCredentials(
    api_key=okx_api_key,
    secret_key=okx_secret_key,
    passphrase=okx_passphrase
)

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.absolute()

# Ищем директорию 'stylus_arbitrum' в пути до ROOT_DIR
parent_dir = ROOT_DIR
while parent_dir.name != 'stylus_arbitrum':
    parent_dir = parent_dir.parent

# Формируем пути
ADDRESSES_PATH = os.path.join(parent_dir, 'privatekeys.txt')
ABIS_DIR = os.path.join(parent_dir, 'data', 'abis')
FILES_DIR = os.path.join(parent_dir, 'files')

LOG_FILE = os.path.join(FILES_DIR, 'log.log')
ERRORS_FILE = os.path.join(FILES_DIR, 'errors.log')

logger.add(ERRORS_FILE, level='ERROR')
logger.add(LOG_FILE, level='INFO')

print(ABIS_DIR)
