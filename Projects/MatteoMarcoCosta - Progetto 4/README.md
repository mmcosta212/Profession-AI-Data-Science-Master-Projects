# Cross Sell Prediction

## Descrizione del progetto

Questo progetto ha l'obiettivo di sviluppare un modello di Machine Learning in grado di prevedere se un cliente già in possesso di un'assicurazione sanitaria sia interessato ad acquistare anche un'assicurazione per il proprio veicolo.

Si tratta di un problema di **classificazione binaria**, in cui la variabile target si chiama **Response**.

---

## Obiettivi
- Analizzare il dataset e comprenderne le caratteristiche.
- Effettuare la pulizia e la preparazione dei dati.
- Gestire l'eventuale sbilanciamento delle classi.
- Addestrare e confrontare diversi modelli di classificazione.
- Valutare le prestazioni del modello migliore mediante metriche appropriate.

---

## Dataset
Il dataset contiene informazioni anagrafiche e assicurative dei clienti. Le principali variabili sono:

| Variabile | Descrizione |
|-----------|-------------|
| Gender | Sesso del cliente |
| Age | Età |
| Driving_License | Possesso della patente |
| Previously_Insured | Cliente già assicurato per il veicolo |
| Vehicle_Age | Età del veicolo |
| Vehicle_Damage | Danni al veicolo in passato |
| Annual_Premium | Premio assicurativo annuo |
| Policy_Sales_Channel | Canale di vendita |
| Vintage | Giorni come cliente |
| Response | Variabile target |

---

## Workflow
Il progetto segue le seguenti fasi:

1. Esplorazione del dataset (EDA)
2. Analisi dei valori mancanti
3. Analisi della distribuzione delle variabili
4. Feature Engineering e codifica delle variabili categoriche
5. Gestione dello sbilanciamento delle classi (Class Weight / Oversampling)
6. Addestramento del modello
7. Valutazione tramite opportune metriche di classificazione

---

## Modelli utilizzati
Applicazione di modelli di regressione logistica.

---

## Tecnologie utilizzate
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn

---

## Risultati
Il modello finale è stato valutato utilizzando diverse metriche di classificazione per individuare la soluzione più adatta al problema, prestando particolare attenzione allo sbilanciamento della variabile target.