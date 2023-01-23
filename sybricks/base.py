import abc
from typing import List, Any

from dotenv import dotenv_values

config = dotenv_values(".env")

class BaseLego(metaclass=abc.ABCMeta):
    """Abstract base class for Legos.
    This obviates the need to declare a `compute` function
    """

    @abc.abstractmethod
    def compute(self, address: str) -> bool:
        pass

class EtherscanLego(BaseLego):

    def __init__(self):
        self.ETHERSCAN_API_KEY = config.ETHERSCAN_API_KEY
        self.MAX_ATTEMPT = 0
        self.PREFIX = 'api'

    def retrieve_transactions(self, address: str) -> Dict[str, Any]:
        """Given an eth address, extract its transaction from etherscan
        """

        result = {}
        transactions_base = requests.get(
                f"https://{self.PREFIX}.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page=1&offset={self.MAX_ATTEMPT}&sort=desc&apikey={self.ETHERSCAN_API_KEY}"
            ).json()
        
        transactions_erc20 = requests.get(
                f"https://{self.PREFIX}.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=99999999&page=1&offset={self.MAX_ATTEMPT}&sort=desc&apikey={ETHERSCAN_API_KEY}"
            ).json()

        # Aggregate "base" and "erc20" transactions
        if transactions_base['status'] == '1':
        transactions = transactions_base['result']
        if transactions_erc20['status'] == '1':
            transactions += transactions_erc20['result']

        return transactions