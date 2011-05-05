\* Problem mesanja pasje hrane *\
Minimize
Skupna_cena_sestavin_na_plocevinko: 0.02 KokosjeDelez + 0.015 SvinskoDelez
Subject To
Kolicina_soli: 0.002 KokosjeDelez + 0.005 SvinskoDelez <= 0.4
Mascobne_zahteve: 0.08 KokosjeDelez + 0.1 SvinskoDelez >= 6
Proteinske_zahteve: 0.1 KokosjeDelez + 0.2 SvinskoDelez >= 8
Skupni_delez: KokosjeDelez + SvinskoDelez = 100
Vlakninske_zahteve: 0.001 KokosjeDelez + 0.005 SvinskoDelez <= 2
Bounds
0 <= KokosjeDelez
Generals
KokosjeDelez
End
