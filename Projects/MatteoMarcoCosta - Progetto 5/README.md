# Credit Scoring Prediction

## Descrizione del progetto
Questo progetto ha l'obiettivo di sviluppare un modello di Machine Learning in grado di prevedere l'affidabilità creditizia di un cliente, supportando il processo decisionale per il rilascio di una carta di credito.

Il modello utilizza dati anonimizzati relativi ai clienti della **Pro National Bank** e restituisce una previsione della variabile **TARGET**, dove:

- **1** → cliente affidabile (pagamento regolare delle rate);
- **0** → cliente non affidabile.

---

## Obiettivi
- Analizzare il dataset.
- Effettuare la pulizia e la preparazione dei dati.
- Addestrare uno o più modelli di classificazione.
- Valutare le prestazioni mediante metriche appropriate.
- Interpretare le decisioni del modello per fornire motivazioni in caso di rifiuto della richiesta di credito (punto bonus).

---

## Dataset
Il dataset è disponibile al seguente indirizzo:

https://proai-datasets.s3.eu-west-3.amazonaws.com/credit_scoring.csv

Le principali variabili disponibili sono:

| Variabile | Descrizione |
|-----------|-------------|
| CODE_GENDER | Sesso del cliente |
| FLAG_OWN_CAR | Possesso automobile |
| FLAG_OWN_REALTY | Possesso immobile |
| CNT_CHILDREN | Numero di figli |
| AMT_INCOME_TOTAL | Reddito annuale |
| NAME_INCOME_TYPE | Tipo di reddito |
| NAME_EDUCATION_TYPE | Livello di istruzione |
| NAME_FAMILY_STATUS | Stato civile |
| NAME_HOUSING_TYPE | Tipo di abitazione |
| DAYS_BIRTH | Età espressa in giorni |
| DAYS_EMPLOYED | Giorni di impiego/disoccupazione |
| OCCUPATION_TYPE | Occupazione |
| CNT_FAM_MEMBERS | Numero di componenti familiari |
| TARGET | Variabile da prevedere |

---

## Tecnologie utilizzate
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Workflow
Il progetto segue le principali fasi di una pipeline di Machine Learning:

1. Caricamento del dataset.
2. Analisi esplorativa dei dati (EDA).
3. Pulizia dei dati.
4. Gestione dei valori mancanti.
5. Encoding delle variabili categoriche.
6. Feature Engineering.
7. Suddivisione in Training e Test Set.
8. Addestramento del modello.
9. Valutazione delle prestazioni.
10. Interpretazione dei risultati.

---

## Modelli valutati
Durante lo sviluppo sono stati applicati diversi algoritmi di regressione logistica:

- Logistic Regression
- Logistic Regression with gradient descend
- Gradient Boosting classifier
- Decisione Tree

Il modello finale viene selezionato in base alle migliori prestazioni sul test set.

---

## Metriche di valutazione
Per valutare il classificatore vengono considerate:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Poiché il problema riguarda il rischio creditizio, particolare attenzione viene posta ai falsi positivi e ai falsi negativi.

---

## Interpretabilità del modello (Bonus)
Per soddisfare il requisito di interpretabilità sono state analizzate le variabili che maggiormente influenzano la previsione.

A seconda del modello utilizzato è possibile ricorrere a:

- Feature Importance
- Coefficienti della Regressione Logistica
- Path analysis

In questo modo è possibile spiegare al cliente quali caratteristiche hanno inciso maggiormente sulla decisione.

---

## Possibili sviluppi futuri
- Ottimizzazione degli iperparametri.
- Bilanciamento delle classi.
- Cross Validation.
- Deploy tramite API (FastAPI o Flask).
- Dashboard interattiva per la consultazione dei risultati.
- Monitoraggio delle prestazioni del modello nel tempo.