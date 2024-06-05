Wichtige Befehle

1. Importieren der Bibliotheken:

   import pandas as pd
   import matplotlib.pyplot as plt

2. CSV-Datei lesen:

   df = pd.read_csv('datensatz.csv')

3. Daten gruppieren und aggregieren

   daten_gruppiert = df.groupby('Produkt')['Verkäufe'].sum()

4. Ergebnisse ausgeben

   print(daten_gruppiert)

5. Daten visualisieren

   daten_gruppiert.plot(kind='bar', title='Titel')

   plt.xlabel('x-Achsen Beschriftung')
   plt.ylabel('Y-Achsen Beschriftung')
   plt.show()