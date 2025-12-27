from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    """Class to represent an ecommerce product"""

    name: str
    price: float
    rating: Optional[float] = None
    url: str = ""
