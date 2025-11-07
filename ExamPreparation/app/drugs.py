"""
This module holds Drug class which represents medicine.
"""
from pathlib import Path
from typing import List, Dict

import pandas as pd

class Drug:
    """docstring"""
    def __init__(
            self,
            id_: int,
            name: str,
            category: str
    ) -> None:
        """docstring"""
        self.id_: int = id_
        self.name: str = name
        self.category: str = category
        self.price: float|None = None
        self.discount: float|None = None


    def __str__(self):
        return f"{self.name} {self.category}"


    def apply_discount(self):
        self.price *= self.discount


def read_drugs_csv(path: Path) -> List[Drug]:
    df = pd.read_csv(path)
    drugs: List[Drug] = []
    for index, row in df.iterrows():
        drug = Drug(
            id_=row['id'],
            name=row['name'],
            category=row['category']
        )
        drugs.append(drug)
    print(f"All drugs have been read from csv")
    return drugs


def read_prices(path: Path, drugs: Dict[int,Drug]) -> None:
    """Docstring"""
    # drugs: {drug_id: Drug(), ..}
    df = pd.read_csv(path)
    for index, row in df.iterrows():
        drug = drugs.get(row['id'])
        if drug:
            drug.price = row["price"]
            drug.discount = row["discount"]
