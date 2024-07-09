# Un catalogo ha:
# - Nome azienda
# - Un elenco di prodotti

# Ogni prodotto ha:
# - Codice
# - Nome
# - Anno
# - Prezzo di listino

# In particolare sono prodotti anche i vestiti e gli accessori
# I vestiti hanno:
# - Taglie disponibili
# Gli accessori hanno:
# - Materiale

from catalogo import Catalogo
from prodotto import Prodotto
from accessorio import Accessorio
from vestito import Vestito

c = Catalogo("MaxMara")
p1 = Prodotto("P123", "Scarpe da uomo", 2023, 150)
c.aggiungi(p1)
p2 = Vestito("V456", "Maglia", 2023, 200, ["S", "M", "L"])
c.aggiungi(p2)
p3 = Accessorio("B123", "Borsa bellissima", 2023, 1500, "Pelle")
c.aggiungi(p3)
p4 = Prodotto("P123", "Scarpe ultimo modello", 2024, 250)
# EXTRA: Dà errore perché il codice P123 c'è già
c.aggiungi(p4)
p4 = Prodotto("P124", "Scarpe ultimo modello", 2024, 250)
c.aggiungi(p4)
p5 = Vestito("V458", "Maglia nuovissima", 2024, 300, ["XS", "S", "M", "L", "XL"])
c.aggiungi(p5)
p6 = Accessorio("B127", "Borsa economica", 2024, 50, "Plastica")
c.aggiungi(p6)
c.mostra()
# Mi aspetto questo output:
# Catalogo MaxMara
# P123 | Scarpe da uomo | 2023 | 150
# V456 | Maglia | 2023 | 200 | ["S", "M", "L"]
# B123 | Borsa bellissima | 2023 | 1500 | Pelle
# P124 | Scarpe ultimo modello | 2024 | 250
# V458 | Maglia nuovissima | 2024 | 300 | ["XS", "S", "M", "L", "XL"]
# B127 | Borsa economica | 2024 | 50 | Plastica
c.mostra(2024)
# Mi aspetto questo output:
# Catalogo MaxMara anno 2024
# P124 | Scarpe ultimo modello | 2024 | 250
# V458 | Maglia nuovissima | 2024 | 300 | ["XS", "S", "M", "L", "XL"]
# B127 | Borsa economica | 2024 | 50 | Plastica
c.search_by_id("P134", print_result = True)
c.search_by_id("P124", print_result = True)

c.remove_by_id("V458")

c.mostra(2024)
