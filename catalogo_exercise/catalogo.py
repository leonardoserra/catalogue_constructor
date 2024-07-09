from prodotto import Prodotto
class Catalogo:

  def __init__(self, name:str):
    self.name:str = name
    self.products:list[Prodotto] = list()
  
  def aggiungi(self, product:Prodotto):
    if product.id in [p.id for p in self.products]:
      print("-------------------------")
      print(F"Id {product.id} è già presente nel catalogo!")
      return
    else:
      self.products.append(product)

  def search_by_id(self, id:str):
    result = [p for p in self.products if p.id == id]
    print("-------------------------")
    print(result[0]) if result else print(F"Nessun Risultato Trovato con la ricerca '{id}'")

  def mostra(self, year:int|None = None):
    if year:
      print("-------------------------")
      print(F"Catalogo {self.name} {year}")
      [print(p) for p in self.products if p.year == year ]
    else:
      print("-------------------------")
      print(F"Catalogo  {self.name}")
      [print(p) for p in self.products]
