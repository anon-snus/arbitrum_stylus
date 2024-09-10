import random

from config import logger
from web3.types import TxParams
from data.models import Contracts
from tasks.base import Base
import config

from withdrawal.main import okx_withdraw


class MintTask(Base):

	async def mint(self):
		my_addr= self.client.account.address
		nft_amount = random.randint(config.nft_per_wallet['from'], config.nft_per_wallet['to'])
		failed_text = f'{my_addr} did not mint nft :( '
		contract = await self.client.contracts.get(contract_address=Contracts.Mint)
		data =f'0xfb9d09c8000000000000000000000000000000000000000000000000000000000000000{nft_amount}'

		tx_params = TxParams(
			to = contract.address,
			data = data
			)

		if await self.check_balance() and await self.wait_for_gwei(max_gas_price=config.max_gwei):
			try:
				tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
				receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
				if receipt:
					logger.info(f'{my_addr}  successfully minted {nft_amount} nfts : {tx.hash.hex()}')
				else:
					logger.error(f'{failed_text}!')
			except Exception as e:
				logger.error(e)


	async def check_balance(self):
		balance = await self.client.wallet.balance()
		if balance.Ether >= 0.00002:
			return True
		else:
			try:
				await okx_withdraw(self.client.account.address)
				return True
			except Exception as e:
				logger.error(e)