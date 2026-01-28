# Empirische Analyse des Einflusses makroökonomischer Variablen auf Kryptopreise

Dieses Repository enthält den vollständigen Quellcode, die Daten sowie das LaTeX-Projekt zur Seminararbeit  
**„Empirische Analyse des Einflusses makroökonomischer Variablen auf Kryptopreise“**.

## 📌 Projektbeschreibung
Ziel der Arbeit ist die empirische Untersuchung des Zusammenhangs zwischen ausgewählten US-amerikanischen makroökonomischen Variablen und den Renditen von Kryptowährungen. Der Fokus liegt auf **Bitcoin**, **Ethereum** wird ergänzend als Robustheitstest betrachtet.  
Die Analyse basiert auf monatlichen Zeitreihendaten für den Zeitraum **2015–2025**.

## 📊 Datenquellen
- Makroökonomische Daten: Federal Reserve Economic Data (FRED)  
- Finanzmarktdaten: Yahoo Finance  

## 🛠 Verwendete Tools
- Python  
- pandas  
- numpy  
- statsmodels  
- matplotlib  
- Jupyter Notebook  
- LaTeX  

## 📈 Methodik
- Deskriptive Statistik  
- Zeitreihenanalyse  
- Augmented-Dickey-Fuller-Tests (ADF)  
- Lineare Regressionsmodelle (OLS)  
- VAR-Analyse und Robustheitsprüfung mit Ethereum  

## 📂 Projektstruktur
### `src/`
- `src/data/` – Rohdaten (CSV)  
- `src/processed/` – aufbereitete Datensätze  
- `src/notebooks/` – Analyse-Notebooks (Data Prep, Deskriptiv, Zeitreihen, Regression)  
- `src/figures/` – exportierte Grafiken (PDF)  
- `src/tables/` – exportierte LaTeX-Tabellen (ADF, Deskriptivstatistik, Regressionen)  
- `src/python_scripts/` – Hilfsskripte (z. B. Datendownload via `fetch_data.py`)  
- `src/requirements.txt` – Python-Abhängigkeiten

### `TeX/`
- `TeX/main.tex` – Hauptdokument
- `TeX/*.tex` – Kapiteldateien
- `TeX/main.pdf` – kompilierte Seminararbeit

## 📄 Seminararbeit
Die finale Version der Seminararbeit befindet sich unter  
`TeX/main.pdf`.
