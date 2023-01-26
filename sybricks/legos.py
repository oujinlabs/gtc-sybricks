import requests
import urllib.request, json

from bs4 import BeautifulSoup

from .base import BaseLego


class WalletHasEnsLego(BaseLego):
    """Access etherscan's ens lookup page and returns whether the address has an ENS
    """

    def __init__(self):
        self.base_url = f'https://etherscan.io/enslookup-search?search={address}'

    def compute(self, address: str) -> bool:
        try:
            result = requests.get(self.base_url, headers={'User-Agent': 'Mozilla/6.0'})
        except:
            logger.error('Error while accessing the page.')
            return False
                
        if result.status_code == 200:
            soup = BeautifulSoup(result.content, 'html.parser')
            for s in soup.find("div", {"class": "col-md-9 d-flex mb-n1"}):
                if str(s.find("span")).split('/>')[-1][:-7]:
                    return True

        elif result.status_code == 404:
            logger.error('404 error.')
            return False


class WalletSpentLessThanXInFeesLego(EtherscanLego):

    def __init__(self, fees_limit: float):
        super().__init__()
        self.fees_limit = fees_limit

    def compute(self, address: str) -> bool:
        transactions = self.retrieve_transactions(address)
        fees = sum([float(r['gasUsed']) * float(r['gasPrice']) * 1e-9**2 for r in transactions])

        return self.fees_limit <= self.fees_limit


class WalletIsVerifiedUniswapTwitter(BaseLego):

    def __init__(self):
        with urllib.request.urlopen("https://raw.githubusercontent.com/Uniswap/sybil-list/master/verified.json") as url:
            self.verified_accounts = json.load(url)

    def compute(self, address: str) -> bool:
        try:
            self.verified_accounts[address]
            return True
        except:
            return False


class WalletGaveCharityUkraine(EtherscanLego):

    def __init__(self, fees_limit: float):
        super().__init__()
        self.ukraine_crypto_wallet = '0x165cd37b4c644c2921454429e7f9358d18a45e14'
    
    def compute(self, address: str) -> bool:
        transactions = self.retrieve_transactions(address)
        _to = self.get_transactions_counterparts(transactions)

        return self.ukraine_crypto_wallet in _to
