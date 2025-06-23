- U telekomunikacijama se cesto susrecemo sa *slucajnim (stohastickim) procesima*.
- Oni su prosirenje koncepta slucajne promjenjive jer uvode i vremensku dimenziju.
- Primjer jednog slucajnog procesa je sum koji postoji kod komunikacijskog kanala i koji mu se dodaje pa se zove aditivni sum.
- Rekli smo da je slucajna promjenjiva u sustini preslikavanje prostora uzoraka u skup realnih brojeva.
- Slucajni proces je skup vremenskih funkcija koje se dodjeluju razlicitim ishodima slucajnog eksperimenta. U tom smislu, slucajni proces mozemo definisati kao preslikavanje prostora uzoraka u skup funkcija koje zavise od vremena.

---
>[!abstract] Sta je slucajni proces u sustini?
>**Slucajna promjenjiva** $X$:
>To je funkcija koja svakom mogucem ishodu slucajnog eksperimenta dodijeli neki broj npr.
>- $X =$ temepratura u podne sutra.
>
>**Slucajni proces** $X(t)$:
>To je skup (familija) slucajnih promjenjivih zavisnih od vremena npr.
>- $X(t) =$ temperatura u toku sutrasnjeg dana.
>  - za svaki trenutak $t$, $X(t)$ je slucajna promjenjiva jer zavisi od ishoda.
>  - za neko fiksno $t = t_0$, $X(t_0)$ je slucajna promjenjiva.

Formalno, slucajni proces bismo onda mogli definisati ovako:

>[!definition] Slucajni proces
>Slucajni (stohasticki) proces je preslikavanje
>$$X: T\times S \to \mathbb{R},$$
>gdje je $T$ vremenski skup a $S$ skup svih mogucih ishoda slucajnog eksperimenta. Mozemo reci da je slucajni proces dakle familija funkcija $X(t, \xi)$.
>
>Ako je vremenski skup $T$ diskretan, tada se radi o diskretnom slucajnom proecsu a ako je kontinualan onda se radi o kontinualnom slucajnom procesu.

>[!definition] Realizacija slucajnog procesa
>Neka je dat ishod $\xi\in S$. Preslikavanje
>$$t\to X(t, \xi)$$
>nazivamo realizacija ili trajektorija slucajnog procesa za fiksno $\xi$. Primijetimo da je to funkcija koja zavisi samo od vremena. Skup svih realizacija slucajnog procesa zovemo **ansambl**.
>
>Ako fiksiramo jos i vrijeme, tada dobijamo slucajnu promjenjivu $X(t_j, \xi_i)\in \mathbb{R}.$

- Npr ako imamo slucajni proces $X(t, \xi)$ tada bi funkcije
	- $X(t, \xi_1) = x_1(t)$
	- $X(t, \xi_2) = x_2(t)$
predstavljale dvije realizacije datog slucajnog procesa.

>[!definition] Poptuni opis slucajnog procesa
>Slucajni proces $X(t, \xi)$ je potpuno opisan ako je poznata funkcija raspodjele vjerovatnoce slucajne promjenjive $X(t)$ za svako proizvoljno $t$ tj. ako je poznato $F_{X(t)}(x)$. Osim toga, potrebno je da i za proizvoljno odabran broj razlicitih trenutaka $t_1, t_2, ..., t_n$ bude poznata zdruzena funkcija raspodjele vjerovatnoce
>$$F_{X(t_1), X(t_2), ..., X(t_n)}(x_1, x_2, ..., x_n).$$

- Ovo je ocigledno prekomplikovano da se poznaje za sve moguce kombinacije trenutaka i ishoda $\xi$. Zbog toga se u praksi koristi djelimicni opis slucajnog procesa. Za karakterizaciju slucajnog procesa drugog reda kljucna su tri parametra:
	- srednja vrijednost slucajnog procesa
	- autokorelaciona funkcija
	- kovarijansa

>[!definition] Srednja vrijednost slucajnog procesa
>Srednja vrijednost slucajnog procesa $X(t)$ je deterministicka funkcija vremena
>$$m_X(t) = E[X(t)] = \int_{-\infty}^{\infty} xf_{X(t)}(x)dx.$$
>
>Za konkretno $t = t_0$ dobijamo slucajnu promjenjivu $X(t_0)$ cija ce srednja vrijednost biti $m_X(t_0)$. Ovako usrednjavanje zovemo usrednjavanje po ansamblu.

>[!definition] Autokorelaciona funkcija
>Autokoleraciona funkcija slucajnog proces $X(t)$ se definise kao funkcija
>$$R_{XX}(t_1, t_2) = E[X(t_1)X(t_2)] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}x_1x_2f_{X(t_1), X(t_2)}(x_1, x_2)dx_1dx_2.$$

>[!definition] Kovarijansa
>Kovarijansa opisuje vezu izmedju slucajnih promjenjivih dobijenih uzorkovanjem slucajnog procesa u dva trenutka vremena $t_1$ i $t_2$:
>$$R_{X}(t_1, t_2) =  \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}(x_1-m_X(t_1))(x_2-m_X(t_2)f_{X(t_1), X(t_2)}(x_1, x_2)dx_1dx_2.$$


