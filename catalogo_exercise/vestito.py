from prodotto import Prodotto

class Vestito(Prodotto):
  def __init__(self, id: str, name: str, year: int, price: int | float, sizes:list[str]):
    super().__init__(id, name, year, price)
    self.sizes = sizes
  
  def __repr__(self):
    return F" {self.id} | {self.name} | {self.year} | {self.price} | {self.sizes}"