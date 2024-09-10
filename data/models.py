from libs.eth_async.models import RawContract, DefaultABIs
from libs.eth_async.utils.files import read_json
from libs.eth_async.classes import Singleton

from config import ABIS_DIR

class Contracts(Singleton):
	Mint = RawContract(
		title='mint',
		address='0x78072889Ee4D7Fe1A100C25296AABBEA32e92Bea',
		abi=read_json(path=(ABIS_DIR, 'stylus_abi.json'))
	)