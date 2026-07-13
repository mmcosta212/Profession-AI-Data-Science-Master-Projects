# 🥬 Vegan Warehouse Manager
Un'applicazione da terminale scritta in Python per la gestione di un piccolo magazzino di prodotti vegani.

Il programma permette di:

- aggiungere prodotti al magazzino;
- registrare le vendite;
- visualizzare l'inventario;
- calcolare profitti lordi e netti;
- salvare automaticamente i dati tra un'esecuzione e l'altra tramite un file JSON.

---

## Requisiti
- Python 3.10 o superiore

Non sono richieste librerie esterne.

---

## Avvio

Eseguire il notebook. Alla prima esecuzione verrà creato automaticamente il file:

```
storage.json
```

che contiene:

- inventario
- storico dei profitti lordi
- storico dei profitti netti

---

## Comandi disponibili

| Comando | Descrizione |
|----------|-------------|
| `aggiungi` | Inserisce un nuovo prodotto |
| `vendita` | Registra una vendita |
| `elenca` | Visualizza il magazzino |
| `profitti` | Mostra i profitti |
| `aiuto` | Elenca i comandi disponibili |
| `chiudi` | Salva i dati ed esce |

---

## Persistenza dei dati
I dati vengono salvati automaticamente nel file `storage.json` alla chiusura del programma. Alla riapertura del programma il contenuto del magazzino viene ricaricato automaticamente.

---

## Architettura

Il progetto è costituito dal notebook principale che richiama il modulo **vegan_functions.py**
contenente tutta la logica dell'applicazione (funzioni per inventario, vendite e calcolo dei profitti).

---

## Possibili sviluppi

- ricerca prodotti
- modifica prodotti
- eliminazione prodotti
- gestione tramite interfaccia grafica
- esportazione in Excel/CSV
- database SQLite
- gestione utenti