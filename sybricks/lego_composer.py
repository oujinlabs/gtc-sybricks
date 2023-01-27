from typing import List, Dict

from .base import BaseLego

class LegosComposer():

    def __init__(self, legos: List[BaseLego]):
        self.legos = legos

    def compute_all(self, address: str) -> Dict[str, bool]:
        return {lego.__class__.__name__: lego.compute(address) for lego in self.legos}
