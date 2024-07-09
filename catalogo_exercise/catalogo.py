import re
from prodotto import Prodotto

class Catalogo:

  
  def __init__(self, name:str):
    self.name:str = name
    self.products:list[Prodotto] = list()

  def validate_product_id(self,id:str)->bool:
    if re.match("[A-Z]{1}[0-9]{3}$", id) == None:
      return False
    return True

  def aggiungi(self, product:Prodotto):
    if self.validate_product_id(product.id):
      if product.id in [p.id for p in self.products]:
        print("-------------------------")
        print(F"Id {product.id} è già presente nel catalogo!")
        return
      else:
        self.products.append(product)
    else:
      print("-------------------------")
      print(F"Il prodotto '{product.name}' deve essere composto da 1 una Lettera maiuscola iniziale seguita da tre cifre\nId inserito: {product.id}")
    

  def find_item_by_id(self, id:str):
    return [p for p in self.products if p.id == id]
  
  def search_by_id(self, id:str):
    result = self.find_item_by_id(id)
    if result: 
      print("-------------------------")
      print("Prodotto Trovato:", result[0], end="\n-----------------------") if result else print(F"Nessun Risultato Trovato con la ricerca '{id}'")

  def mostra(self, year:int|None = None):
    if year:
      print("-------------------------")
      print(F"Catalogo {self.name} {year}\n")
      [print(p) for p in self.products if p.year == year ]
    else:
      print("-------------------------")
      print(F"Catalogo {self.name}\n")
      [print(p) for p in self.products]

  def remove_by_id(self, id:str):
    item = self.find_item_by_id(id)
    if item:
      self.products.remove(item[0])
      print("-------------------------")
      print(F"Rimosso: {item}")
