# Comparatie Rezolutie DP DPLL (SAT)

Implementări comparative pentru algoritmi SAT: Rezoluție, DP, DPLL

## Compararea Algoritmilor SAT: Rezoluție, Davis–Putnam (DP) și DPLL

Acest proiect implementează și compară trei algoritmi clasici pentru rezolvarea problemei satisfiabilității (SAT):

- **Rezoluție**
- **Davis–Putnam (DP)**
- **Davis–Putnam–Logemann–Loveland (DPLL)**

Proiectul include implementări în Python, date de test reale și generate aleator, precum și o analiză comparativă a performanței algoritmilor.



## Structura proiectului

- `rezolutie.py` – Implementarea algoritmului de Rezoluție  
- `dp.py` – Implementarea algoritmului Davis–Putnam  
- `dpll.py` – Implementarea algoritmului DPLL  
- `generare_random.py` – Script pentru generarea de fișiere CNF aleatoare  
- `random_30.cnf`, `rand_80_sat.cnf`, `unsat_60.cnf` – Fișiere CNF generate  
- `satlib_aim_50_1.cnf`, `satlib_hole_8.cnf` – Fișiere CNF reale din SATLIB  
- `Comparatie_Rezolutie_DP_DPLL_SAT.pdf` – Raportul complet  
- `README.md`


## Cerințe

- Python 3.8+
- Nu sunt necesare biblioteci externe


## Rulare

Pentru a rula oricare dintre algoritmi:

```bash
python rezolutie.py random_30.cnf
python dp.py rand_80_sat.cnf
python dpll.py satlib_hole_8.cnf
```

Rezultatul va fi afișat în consolă: `SAT` sau `UNSAT`.

## Generarea de instanțe CNF

Poți genera fișiere DIMACS CNF folosind scriptul:

```bash
python generare_random.py
```

Acesta creează un fișier `random.cnf` cu parametri modificabili în cod.

## Descriere fișiere de test

- `random_30.cnf` – instanță aleatoare satisfiabilă (30 variabile)  
- `rand_80_sat.cnf` – instanță aleatoare satisfiabilă (80 variabile)  
- `unsat_60.cnf` – instanță aleatoare nesatisfiabilă (60 variabile)  
- `satlib_aim_50_1.cnf` – instanță reală SAT din SATLIB  
- `satlib_hole_8.cnf` – instanță reală UNSAT din SATLIB

## Documentație

Lucrarea completă (.pdf), cu explicații teoretice, rezultate experimentale și comparații, este disponibilă la:  
[Comparatie_Rezolutie_DP_DPLL_SAT.pdf](./Comparatie_Rezolutie_DP_DPLL_SAT.pdf)


## Licență

Acest proiect este realizat pentru cursul MPI, 2025. Codul este oferit cu scop educațional.
