# Sybricks

This package contains several function which could
Also, it offers a framework for defining those Lego and the user is free to create their own.

## Use Existing Legos

Please not that in order to use Legos retrieving data from etherscan, one should have a `.env` file at the root of the project with `ETHERSCAN_API_KEY` set up.

```{python}
from sybricks.legos import WalletIsVerifiedUniswapTwitter, WalletGaveCharityUkraine, WalletSpentLessThanXInFeesLego
from sybricks import LegosComposer


legos = [WalletIsVerifiedUniswapTwitter(), WalletGaveCharityUkraine(), WalletSpentLessThanXInFeesLego(0.5)]
composer = LegosComposer(legos)

results = composer.compute_all('0x3EeBf6ddC589CD30660B3bC6b11b5c7Fd9E224Ea')
results
>>> {'WalletIsVerifiedUniswapTwitter': False, 'WalletGaveCharityUkraine': True, 'WalletSpentLessThanXInFeesLego': False}
```

## Create Own Lego

A Lego can easily be created - the only requirement is for the class to have a `.compute()` function which returns a boolean.

```{python}
from sybricks.base import BaseLego

class CustomLego(BaseLego):  # Custom Lego inherits from `BaseLego`

    def compute(self, address: str) -> bool:
        # add your logic here
        # Here is a dummy one
        if address.str.startswith('0x0000'):
            return False
        else:
            return True
```