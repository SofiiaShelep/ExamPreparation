from pathlib import Path
from typing import List, Dict

import pandas as pd

class Sales:
    def __init__(
            self,
            id_: int,
            count: int,
            client_type: bool
    ) -> None:
        self.id_: int = id_
        self.count: int= count
        self.client_type: bool = client_type

def read_sales_csv(path: Path) -> List[Sales]:
    df = pd.read_csv(path)
    sales_list = []
    for index, row in df.iterrows():
        sale = Sales(
            id_=row['id'],
            count=row['count'],
            client_type=row['client type']
        )
        sales_list.append(sale)

    print(f"All sales have been read from csv")
    return sales_list


