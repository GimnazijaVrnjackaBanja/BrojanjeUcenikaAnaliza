import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Učitavanje CSV fajla
df = pd.read_csv('tabela2.csv')

# Pretvaranje kolone 'datumvreme' u datetime format
df['datumvreme'] = pd.to_datetime(df['datumvreme'])

# Filtriranje podataka za odabrano ime brojača i datum
ime_brojaca = 'I-1'
datum = '2024-04-03'
filtered_df = df[(df['imebrojaca'] == ime_brojaca) & (df['datumvreme'].dt.date <= pd.to_datetime(datum).date())].copy()

# Izračunavanje kumulativne sume vrednosti brojača
filtered_df['kumulativna_suma'] = filtered_df['vrednostbrojaca'].cumsum()

# Crtanje grafika
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_df, x='datumvreme', y='kumulativna_suma')
plt.axhline(y=5, color='r', linestyle='--', label='Fiksna vrednost')  # Dodavanje horizontalne linije
plt.title(f'Kumulativna suma vrednosti brojača za {ime_brojaca} do {datum}')
plt.xlabel('Datum')
plt.ylabel('Kumulativna suma vrednosti brojača')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
