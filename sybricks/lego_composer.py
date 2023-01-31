from typing import List, Dict
import logging

from .base import BaseLego

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LegosComposer():

    def __init__(self, legos: List[BaseLego]):
        self.legos = legos

    def compute_all(self, address: str) -> Dict[str, bool]:
        logger.info(f"Computing signal for {self.legos}")
        return {lego.__class__.__name__: lego.compute(address) for lego in self.legos}
