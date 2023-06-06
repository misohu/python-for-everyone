is_old = False
is_cool = True

# bool mozes pouzit na  porovnavacie operacie 
3 < 4 
5 > 6
5 == 7  # Pozor porovnanie rovnosti je ce dve znamienka rovna sa nie jedno
4 <= 8
8 == 8.0
9 != 10

x = 1   # Tento prikaz priradi hodnotu 1 premennej x
x == 1  # Tento prikaz porovna hodnotu x s hodnoou jedna 

# Porovnanie premennych 
michals_age = 27
andrews_age = 26 

michals_age < andrews_age   # Co bude vysledok?
michals_age >= andrews_age  # Co bude vysledok? 

# V skutocnosti sa vzdy vyhodnoti cela lava strana a potom prava 
x = 10 
x + 1 < x + 2
x + 1 < x + 0
(x + 1) < (x + 0)   # Niekedy je uzitocne pouzit zatvorky

# Negacia hodnoty bool
x = True 
not(x)