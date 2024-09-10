import asyncio
import random

import config
from tasks.mint import MintTask
from tasks.base import Base
from libs.eth_async.client import Client
from libs.eth_async.models import Networks, TokenAmount

async def main():

	if config.arbitrum_rpc:
		Networks.Arbitrum.rpc=config.arbitrum_rpc
	if config.ethereum_rpc:
		Networks.Ethereum.rpc=config.ethereum_rpc
	keys = await MintTask.get_keys(config.ADDRESSES_PATH)
	if config.shuffle_wallets:
		random.shuffle(keys)
	for PRIVATE_KEY in keys:
		client = Client(private_key=PRIVATE_KEY, network=Networks.Arbitrum)
		mint = MintTask(client=client)
		await mint.mint()
		await Base.sleep(config.sleep['from'], config.sleep['to'])

if __name__ == '__main__':
	asyncio.run(main())
