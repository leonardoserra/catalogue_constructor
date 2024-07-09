from prodotto import Prodotto

class Accessorio(Prodotto):
  def __init__(self, id:str, name:str, year:int, price:int|float, material:str):
    super().__init__(id, name, year, price)
    self.material = material

  def __repr__(self):
    return F" {self.id} | {self.name} | {self.year} | {self.price} | {self.material}"