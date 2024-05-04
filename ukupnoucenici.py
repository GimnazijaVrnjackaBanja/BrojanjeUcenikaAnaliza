import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter, HourLocator

# Učitavanje CSV fajla
df = pd.read_csv('tabela2.csv')

# Pretvaranje kolone 'datumvreme' u datetime format
df['datumvreme'] = pd.to_datetime(df['datumvreme'])

# Unos korisničkih podataka
pocetni_datum = input("Unesite početni datum (YYYY-MM-DD): ")
krajnji_datum = input("Unesite krajnji datum (YYYY-MM-DD): ")
horizontalna_linija = float(input("Unesite ukupan broj učenika Gimnaziji: "))

# Filtriranje podataka za odabrani datumski raspon i isključivanje brojača "zaposleni" i "posetioci"
filtered_df = df[(df['datumvreme'].dt.date >= pd.to_datetime(pocetni_datum).date()) & 
                 (df['datumvreme'].dt.date <= pd.to_datetime(krajnji_datum).date()) & 
                 (~df['imebrojaca'].isin(['zaposlenih', 'posetilaca']))].copy()

# Grupisanje po datumu i izračunavanje kumulativne sume vrednosti brojača unutar svake grupe
filtered_df['kumulativna_suma'] = filtered_df.groupby(filtered_df['datumvreme'].dt.date)['vrednostbrojaca'].cumsum()

# Crtanje grafika
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_df, x='datumvreme', y='kumulativna_suma')

# Dodavanje horizontalne linije
plt.axhline(y=horizontalna_linija, color='r', linestyle='-', label='Broj upisanih učenika')

# Postavljanje oznaka na x osi na svaki drugi sat
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(HourLocator(interval=2))

plt.title(f'Prisutni učenici u Gimnaziji od {pocetni_datum} do {krajnji_datum}')
plt.xlabel('Vreme')
plt.ylabel('Broj prisutnih učenika')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()
