# Transposition Midi Era

## Introduzione

Questa applicazione web utilizza il framework **Flask** e la libreria **music21** per generare composizioni musicali in formato MIDI. L'utente può scegliere tra tre generi musicali (Classico, Jazz, Blues) e generare automaticamente una melodia in uno di questi stili. Il sistema crea sia una versione originale della melodia che una versione modificata secondo il genere scelto, fornendo infine un link per scaricare i file MIDI generati.

L'applicazione permette di esplorare come la musica possa essere trasformata attraverso algoritmi di composizione automatica, con la possibilità di ascoltare e scaricare i risultati in formato MIDI.

---

## Obiettivo del Progetto

L'obiettivo principale di questo progetto è creare un sistema web che permetta di generare e manipolare composizioni musicali utilizzando la tecnologia, offrendo agli utenti la possibilità di scegliere un genere musicale e ascoltare i risultati. I principali scopi includono:

1. **Generazione di una melodia di base**: Una melodia casuale viene creata in Do maggiore con note scelte casualmente.
2. **Trasformazione in vari generi musicali**: La melodia di base viene elaborata per adattarsi ai generi musicali Classico, Jazz e Blues, attraverso modifiche al ritmo, alle dinamiche e alla tonalità.
3. **Esportazione in formato MIDI**: I file generati vengono esportati come file MIDI, che possono essere scaricati e utilizzati in altri software musicali.

---

## Contenuto del Repository

Il repository contiene i seguenti componenti principali:

- **Implementazione del codice**:
    - `app.py`: Il file principale dell'applicazione che gestisce le richieste web e l'elaborazione della musica.
    - `presets/genre_presets.py`: Contiene le funzioni che applicano le trasformazioni musicali in base ai generi selezionati.
    - `templates/`: La cartella che contiene i file HTML per la visualizzazione dell'interfaccia utente (come il modulo per selezionare il genere musicale e il player per ascoltare i file generati).
    - `static/`: La cartella per i file statici (eventualmente per loghi, stili CSS, o script JavaScript).

- **Progetto ZIP**: Un file compresso contenente il progetto pronto per essere eseguito localmente.

- **Logo**: 

- **Documentazione**: fornisce tutte le informazioni necessarie per capire il progetto.

---

## Requisiti

Per eseguire questa applicazione, è necessario avere Python 3.x installato sul proprio sistema e alcune librerie Python. Assicurati di avere i seguenti pacchetti:

- **Flask**: Framework web leggero per Python.
- **music21**: Libreria per la generazione e l'analisi della musica.
- **random**: Modulo Python standard per generare numeri casuali.
- **os**: Modulo Python standard per interagire con il sistema operativo.

Questi requisiti sono elencati nel file `requirements.txt`.

---

## Installazione delle librerie

Per installare le librerie necessarie, è possibile utilizzare **pip** per installare tutti i pacchetti richiesti da `requirements.txt`.

1. **Clona il repository**:
    ```bash
    git clone https://github.com/RedMulaCrackIn/TranspositionMidiEra.git
    ```

2. **Naviga nella cartella del progetto**:
    ```bash
    cd Implementazione
    ```

3. **Installa le librerie**:
    Assicurati di avere un ambiente Python attivo (ad esempio, un ambiente virtuale) e poi esegui il seguente comando per installare le dipendenze:

    ```bash
    pip install music21
    ```

---

## Come Riprodurre il Lavoro

Per eseguire il progetto localmente, segui i passaggi descritti qui sotto:

1. **Avvia il server Flask**:
    Dopo aver installato le librerie, esegui il seguente comando per avviare il server Flask:

    ```bash
    python app.py
    ```

2. **Accedi all'applicazione**:
    Apri il browser e visita l'URL:

    ```
    http://127.0.0.1:5001
    ```

3. **Interagisci con l'app**:
    - Seleziona un genere musicale (Classico, Jazz, Blues) dal menu.
    - Fai clic su "Genera" per creare una melodia di base trasformata nel genere selezionato.
    - Riproduci e confronta le versioni. 
    - Scarica i file MIDI generati direttamente dal browser.
---
