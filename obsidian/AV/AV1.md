>[!abstract] Zadatak 1
>Proizvođač automobila nudi različite dodatne usluge koji se mogu ugraditi u automobil. Svako vozilo
se može naručiti sa automatskim ili sa manuelnim mjenjačem, sa 3 različita stereo sistema, sa ili bez
klime i u tri različite boje. Ako se prostor uzoraka sastoji od svih mogućih kombinacija automobila,
odrediti broj ishoda u prostoru uzoraka?

Svaki automobil ima 4 razlicite karakteristike:
- vrsta mjenjaca - $m$ - 2 vrste
- stereo sistema - $s$ - 3 vrste
- klima - $k$ - 2 vrste
- boja - $b$ - 3 vrste
Prema tome, svaki automobil je jedinstvena uredjena cetvorka $(m, s, k, b)$ s tim da na prvom mjestu mogu 2 mogucnosti, na drugom 3, na trecem dvije i na cetvrtom tri. Prema tome, broj razlicitih automobila je $2\times 3\times 2\times 3$.

---

>[!abstract] Zadatak 2
>Registracijska tablica se sastoji od 2 slova i 3 cifre. Koliko različitih kombinacija je moguće definisati
ako nisu dozvoljena ponavljanja istih slova i istih cifara? Koliko ima kombinacija ako su dozvoljena
ponavljanja? Pretpostaviti da se ne uzimaju u obzir slova č,ć,š,dž,đ,lj,nj.

Dakle, registarska tablica je oblika
$$\texttt{s}_1\texttt{s}_2\texttt{c}_1\texttt{c}_2\texttt{c}_3$$
Slova u engleskom alfabetu ima 26. Ako nam je dozvoljeno ponavljanje slova i deset cifara onda je broj razlicitih tablica
$$26^2\times 10^3.$$
Ako nije dozvoljeno onda
$$26\cdot 25\cdot 10\cdot 9\cdot 8.$$
---
>[!abstract] Zadatak 3
>Koliko četverocifrenih parnih brojeva se može formirati korištenjem cifara 0, 1, 2, 5, 6 i 9 ako je svaku
cifru moguće koristiti samo jednom?

Da bi cetverocifren broj bio paran i sadrzavao samo date cifre, on mora biti oblika
- `abc0`
- `abc2`
- `abc6`

Neka brojeva prvog oblika ima $N_1$, brojeva drugog oblika $N_2$ i treceg $N_3$. Broj koji trazimo ce biti zbir ovih brojeva.

Odgovorimo prvo koliko je $N_1$. Na mjestu `a` moze biti ukupno 5 cifara, na mjestu `b` onda 4 i na mjestu `c` 3. Dakle 
$$N_1 = 5\cdot 4\ \cdot 3.$$
Za brojeve oblika `abc2` imamo sljedeci rezon. Na mjestu `a` moze biti svaki osim 0 i 2, dakle imamo 4 mogucnosti. Na mjestu `b` moze biti neka od 3 preostale cifre a na mjestu `c` neka od 2 cifre, dakle
$$N_2 = 4\cdot 3 \cdot 2.$$
Isto tako je i $N_3$. Konacan odgovor je $N_1+N_2+N_3.$

---

>[!abstract] Zadatak 4
>Na koliko načina se mogu postaviti 3 osobe u redu za snimanje fotografije ako se biraju iz grupe od 5
osoba? Koliko je mogućih kombinacija ako redoslijed nije bitan?

