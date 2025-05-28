# 4.9)

Za određenu rijetku bolest poznato je da oboli jedna osoba od 500. Test za bolest postoji ali naravno nije pouzdan. Tačan pozitivan rezultat (osoba jeste oboljela) se dešava u 95% slučajeva dok pogrešan pozitivan rezultat (osoba nije oboljela) se dešava u 1% slučajeva. Ako se slučajno izabere osoba i testira za određenu bolest, pri čemu se dobije pozitivan rezultat, koja je vjerovatnoća da je osoba zaista oboljela?

---
Jedna od 500 osoba oboli, dakle vjerovatnoca da je osoba oboljela 
$$p(O) = \frac{1}{500}.$$
Oznacimo sa $P$ dogadjaj da je test pozitivan. Test ce biti tacan ako je osoba oboljela i test je pozitivan. Vjerovatnoca da je test pozitivan ako je osoba oboljela je
$$p(P|O) = 0.95.$$
Test je pozitivan ako osoba nije oboljela (tad je test netacan) sa vjerovatnocom
$$p(P|\overline{O}) = 0.01.$$]Trazi nam se vjerovatnoca da je osoba oboljela ako je test pozitivan tj. $p(O|P)$. Po formuli to bi bilo
$$p(O|P) = \frac{p(PO)}{p(P)}.$$
Vjerovatnocu $p(PO)$ bismo mogli odrediti iz
$$p(P|O) = \frac{p(PO)}{p(O)} \Rightarrow p(PO) = p(O)p(P|O) = \frac{1}{500}\cdot 0.95.$$
Jos nam ostane da odredimo vjerovatnocu da je test pozitivan $p(P)$. Pa test ce biti pozitivan u dva slucaja:
1. Ako je pozitivan a osoba oboljela 
2. Ako je pozitivan a osoba nije oboljela
Prema tome,
$$p(P) = p(P|O)p(O) + p(P|\overline{O})p(\overline{O}),$$
a $p(\overline{O})$ lako dobijamo kao $1-p(O).$

# 4.10)

