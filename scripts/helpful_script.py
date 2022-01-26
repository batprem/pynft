import brownie
from brownie import (
    accounts,
    config,
    network,
    Contract,
)
from web3 import Web3


OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev", "cronos-mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "ganache-local-2"]


DECIMALS = 18
INITIAL_PRICE_FEED_VALUE = 2e21
BREED_MAPPING = ["PUG", "SHIBA_INU", "ST_BERNARD"]


def get_account(index=None, account_id=None):
    active_network = network.show_active()
    if index:
        return accounts[index]
    if account_id:
        return accounts.load(account_id)
    if (
        active_network in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or active_network in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])
