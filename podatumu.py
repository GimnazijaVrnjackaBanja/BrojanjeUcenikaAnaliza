import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter, HourLocator

# Učitavanje CSV fajla
df = pd.read_csv('tabela2.csv')

# Pretvaranje kolone 'datumvreme' u datetime format
df['datumvreme'] = pd.to_datetime(df['datumvreme'])

# Unos korisničkih podataka
ime_brojaca = input("Unesite odeljenje: ")
datum = input("Unesite datum (YYYY-MM-DD): ")
horizontalna_linija = float(input("Unesite broj učenika u odeljenju: "))

# Filtriranje podataka za odabrani brojač i datum
filtered_df = df[(df['imebrojaca'] == ime_brojaca) & (df['datumvreme'].dt.date <= pd.to_datetime(datum).date())].copy()

# Izračunavanje kumulativne sume vrednosti brojača
filtered_df['kumulativna_suma'] = filtered_df['vrednostbrojaca'].cumsum()

# Crtanje grafika
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_df, x='datumvreme', y='kumulativna_suma')
plt.axhline(y=horizontalna_linija, color='r', linestyle='--', label='Horizontalna linija')  # Dodavanje horizontalne linije
plt.title(f'Prisutnost učenika odeljenja {ime_brojaca} na dan {datum}')
plt.xlabel('Vreme')
plt.ylabel('Broj učenika')

# Postavljanje formata za prikaz datuma i vremena
plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))  

# Postavljanje oznaka na x osi na svakih pola sata
plt.gca().xaxis.set_major_locator(HourLocator(interval=1))

plt.xticks(rotation=90)  # Rotacija oznaka na x osi za bolju čitljivost
plt.tight_layout()
plt.show()
