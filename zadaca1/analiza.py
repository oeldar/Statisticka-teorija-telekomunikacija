import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

podaci = pd.read_csv("student-mat.csv");

podaci = podaci[["absences", "G3"]];

print("---------- ANALIZA PRIJE FILTRIRANJA: -----------");

najcesci_broj_izostanaka = podaci["absences"].mode()[0];
print(f"Najcesci broj izostanaka je {najcesci_broj_izostanaka}, prazna polja ce se popuniti tim brojem.");
podaci["absences"] = podaci["absences"].fillna(najcesci_broj_izostanaka);

srednja = podaci["absences"].mean();
std_dev = podaci["absences"].std();
print(f"Srednja vrijednost broja izostanaka je {srednja}");
print(f"Standardna devijacija broja izostanaka je {std_dev}");

donja_granica = srednja - std_dev
gornja_granica = srednja + std_dev

print("\n---------- ANALIZA NAKON FILTRIRANJA: -----------");

print(f"Zadrzat cemo samo one redove u kojima je broj izostanaka u segmentu [{donja_granica}, {gornja_granica}]");

podaci = podaci[(podaci["absences"] >= donja_granica) & (podaci["absences"] <= gornja_granica)]

srednja = podaci["absences"].mean();
std_dev = podaci["absences"].std();
print(f"Srednja vrijednost broja izostanaka je {srednja}");
print(f"Standardna devijacija broja izostanaka je {std_dev}");

# U koloni "Polozeno" ce biti:
# 1 - ako je student polozio
# 0 - ako studnent nije polozio
# (Student je polozio ako je ostvario bar 55% ukupnog broja bodova)
max_points = podaci["G3"].max()*0.55;
podaci["Polozeno"] = np.where(podaci["G3"] >= max_points, 1 , 0);

# Broj studenata koji su izostali sa 15 ili više sati
ukupno_izostali_15plus = podaci[podaci["absences"] >= 15]

# Broj koji su i izostali ≥15 i položili
polozili_izostali_15plus = ukupno_izostali_15plus[ukupno_izostali_15plus["Polozeno"] == 1]

# Vjerovatnoća
vjerovatnoca = len(polozili_izostali_15plus) / len(ukupno_izostali_15plus)

print(f"Vjerovatnoća da je student položio ako je izostao ≥15 puta: {vjerovatnoca:.4f}")

print("\n---------- GRAFICKA REPREZENTACIJA REZULTATA: -----------");
plt.figure(figsize=(10,6))
plt.hist(
    [podaci[podaci["Polozeno"] == 1]["absences"], podaci[podaci["Polozeno"] == 0]["absences"]],
    bins=range(int(podaci["absences"].min()), int(podaci["absences"].max()) + 2),
    stacked=True,
    color=['green', 'red'],
    label=['Položili', 'Nisu položili'],
    edgecolor='black',
    alpha=0.7
)
plt.title("Histogram broja izostanaka (zasebno za one koji su položili i one koji nisu)")
plt.xlabel("Broj izostanaka")
plt.ylabel("Broj studenata")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
