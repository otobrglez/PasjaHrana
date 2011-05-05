#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Avtor: Oto Brglez - <oto.brglez@opalab.com> - Maj 2011

# Uvoz pulp modelirnika
from pulp import *

# Ustvarjanje 'prob' spremenljivke, ki vsebuje podatke problema
prob = LpProblem("Problem mesanja pasje hrane",LpMinimize)

# 2 spremenljivki - delez kokosjega in svinskega z spodnjo limito 0
x1 = LpVariable("KokosjeDelez",0,None,LpInteger)
x2 = LpVariable("SvinskoDelez",0)

# Funkcija, ki doloca ceno sestavin v plocevinki, je dodana na 'prob'
prob += 0.02*x1 + 0.015*x2, "Skupna cena sestavin na plocevinko"

# Vnos petih omejitev
prob += x1 + x2 == 100, "Skupni delez"

prob += 0.100*x1 + 0.200*x2 >= 8.0, "Proteinske zahteve"
prob += 0.080*x1 + 0.100*x2 >= 6.0, "Mascobne zahteve"
prob += 0.001*x1 + 0.005*x2 <= 2.0, "Vlakninske zahteve"
prob += 0.002*x1 + 0.005*x2 <= 0.4, "Kolicina soli"

# Izpis podatkov modela v .lp datoteko
prob.writeLP("PasjaHrana.lp")

# Prozenje resevanja
prob.solve()

# The status of the solution is printed to the screen
print "Resitev:", LpStatus[prob.status]

# Izpis spremenljivk
for v in prob.variables():
    print v.name, "=", v.varValue
    
# Izpis optimizirane vrednosti funkcije
print "Skupna cena sestavin na plocevinko = ", value(prob.objective)
