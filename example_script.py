from sybricks.legos import WalletIsVerifiedUniswapTwitter, WalletGaveCharityUkraine, WalletSpentLessThanXInFeesLego
from sybricks import LegosComposer

def main():
    legos = [WalletIsVerifiedUniswapTwitter(), WalletGaveCharityUkraine(), WalletSpentLessThanXInFeesLego(0.5)]
    composer = LegosComposer(legos)

    address = '0x3EeBf6ddC589CD30660B3bC6b11b5c7Fd9E224Ea'
    results = composer.compute_all(address)

    print(f'Signal computed for address {address}')
    print(results)

if __name__ == "__main__":
    main()