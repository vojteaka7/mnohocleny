# mnohočleny
Toto je kalkulačka na [mnohočleny](https://www.matweb.cz/mnohocleny/)

## Jak používat

Spusťe `operace s mnohocleny.py` a pokračujte podle pokynů.

### Přehled operací

+ pro sčítání
- pro odčítání
* pro násboení
/ pro dělení
= pro zjednodušení mnohočlenu
e pro opuštění programu

### Zápis mnohočlenů

Mnohočleny se zapisují normálně.
Před znaménkem je mezera, ale za ním ne.
Mocnina se zapíše jako normální číslo.
Nikde jinde se mezera nepíše.
Je možně že se někde vyskytne ".0" navíc.
Desetinnou čárku je možné zapsat i jako čárku

Příklad:
-6a2 +3a -12

## Používání funkcí

V souboru `main.py` jsou uloženy všechny funkce pro sčítání, odčítání, násobení, dělení, zjednodušování a obracení mnohočlenů.

### Ukládání mnohočlenů a členů

Mnohočlen je seznam členů.

Člen je dvojice, první prvek je koeficient členu a druhý je seznam proměnných a jejich stupňů. Proměnné jsou uloženy jako seznam dvojic pro jednotlivé proměnné. První prvek dvojice je stupeň a druhý je `string` dlouhý jeden znak udávající proměnnou. Každé číslo je buď `int` nebo `float`

```python
[(12, [(0, 'a')]), (-6, [(2, 'a')]), (3, [(1, 'a')])] 
```
znamená
![-6a²+3a+12](https://latex2png.com/pngs/2efb4d31555c719fa351ab702762286f.png)
