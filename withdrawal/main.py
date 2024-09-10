import asyncio
from decimal import Decimal

from sympy.physics.units import amount

import config
from libs.eth_async.models import Networks
from withdrawal.okx_actions import OKXActions
from withdrawal import currencies
from config import logger
from libs.eth_async.utils.utils import randfloat

async def okx_withdraw(wallet: str):
	amount = randfloat(from_= config.withdraw_amount['from'], to_= config.withdraw_amount['to'], step=Decimal(0.1)**config.withdraw_amount['step'])
	okx_actions = OKXActions(credentials=config.okx_credentials)
	await okx_actions.collect_funds_from_subaccounts()
	network = await currencies.curr(dict=True)
	chain = ('arbitrum one').upper()
	chain = network[chain]
	try:
		id = await okx_actions.withdraw(to_address=wallet, amount=amount, token_symbol='ETH', chain=chain)
		await okx_actions.try_to_get_tx_hash(wd_id=id)

	except Exception as e:
		logger.error(f'cannot withdraw to {wallet}, {e}')
