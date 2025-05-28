1. U kutiji se nalazi $n$ loptica oznacenih brojevima od $1$ do $n$. Iz kutije izvlacimo $r$ loptica pri cemu kad neku lopticu izvucemo, vracamo je nazad. Neka je $X$ najveci izvuceni broj. Odrediti funkciju raspodjele slucajne promjenjive $X$ i pmf za $X$.

Neka u kutiji imamo loptice oznacene sa $1, 2, ..., n$. Izvlacimo $r$ loptica pri cemu ih vracamo nazad u kutiju. Dakle, par mogucih izvlacenja bi bilo
$$\begin{align*}
(1,1,1, ..., 1)&,\\
(1, 2, 1, ...,4)&,\\
(2, 4, 2, ..., n)&.\\
(n, n, n, ..., 2)&, ...
\end{align*}$$
Skup svih ovih $r$-torki brojeva od $1$ do $n$ bi dakle bio prostor uzoraka $S$. Skup $S$ je prema tome skup svih varijacija klase $r$ skupa od $n$ elemenata i vrijedi da je broj razlicitih ishoda
$$|S| = n^r.$$
Slucajna promjenjiva $X$ je funkcija koja svakom ishodu $s = (x_1, x_2, ..., x_r)\in S$ dodjeljuje maksimalni izvuceni broj tj.
$$X(s) = \max \{x_1, x_2, ..., x_r\}.$$
Primijetimo da $X$ moze poprimiti vrijednosti iz skupa $\{1, 2, ..., n\}$ pa je $X$ diskretna slucajna promjenjiva. Funkcija raspodjele vjerovatnoce slucajne promjenjive $X$ je po definiciji
$$F_X(x) = p(X\leqslant x).$$
Dakle, problem se svodi na odredjivanje vjerovatnoce $p(X\leqslant x)$. Primijetimo da situacija u kojoj je maksimalni izvuceni broj neko $x$ znaci da je $r$ izvucenih brojeva iz skupa $\{1, 2, ..., x\}$. Broj svih $r$-torki skupa od ovih $x$ brojeva je $x^r$.

Prema tome,
$$p(X\leqslant x) = \frac{x^r}{n^r}$$
sto je po definiciji
$$F_X(x) = p(X\leqslant x) = \frac{x^r}{n^r}.$$
Funkciju diskretne slucajne promjenjive $X$ tj. vjerovatnocu da je najveci izvuceni broj jednak nekom $x$ dobit cemo koristeci formulu
$$p_X(x_i) = p(X = x_i) = F_X(x_i) - F_X(x_{i-1})$$
gdje su $x_1, x_2, ..., x_{i-1}, x_i, ..., x_r$ sve vrijednosti koje slucajna promjenjiva $X$ moze poprimiti. Prema tome,
$$\begin{align*}p_X(x) &= F_X(x) - F_X(x-1)\\
 &= \frac{x^r}{n^r} - \frac{(x-1)^r}{n^r}\\
 &= \left (\frac{x}{n}\right)^r - \left(\frac{x-1}{n}\right)^r.\end{align*}$$
---
2. U kutiji se nalazi $n$ loptica oznacenih brojevima od $1$ do $n$. Iz kutije izvlacimo $r$ loptica pri cemu kad neku lopticu izvucemo, ne vracamo je nazad. Neka je $X$ najveci izvuceni broj. Odrediti funkciju raspodjele slucajne promjenjive $X$ i pmf za $X$.

Ovaj ne znam.

---
