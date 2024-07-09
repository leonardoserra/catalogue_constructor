class Prodotto:
  def __init__(self, id:str, name:str, year:int, price:int|float):
    self.id = id
    self.name = name
    self.year = year
    self.price = price
  
  def __repr__(self):
    return F" {self.id} | {self.name} | {self.year} | {self.price}"