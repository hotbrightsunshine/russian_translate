# Documentazione RussianTranslate
RussianTranslate è uno script Python 3.10 che transcodifica i file in un formato compatibile con i server russi e li sposta, in ordine, nelle cartelle specificate nel file di configurazione. 

## Descrizione
RussianTranslate è stato scritto in Python, ed è stato successivamente convertito in eseguibile Windows con la libreria `pyinstaller`, disponibile nel [repostory PIP](https://pypi.org/project/pyinstaller/ "repostory PIP"). 
### File eseguibili
Il software è composto da due componenti principali. Nella cartella dei file binari, è presente un file eseguibile `translate.exe` che serve ad eseguire il programma di traduzione, e `configure` che è il collegamento al file eseguibile `configure\configure.exe`. 

### File di supporto
Oltre ai file eseguibili, la cartella principale (root) contiene alcuni file importanti per il funzionamento del software, quali:
- `settings.json` - il file di configurazione,
- `table.csv` - la tabella di conversione dei caratteri.
- `log.txt` - il file di log, dove viene scritto tutto ciò che appare a schermo all'utente. (Se non presente, questo file viene generato automaticamente)

Il file `settings.json` è l'unico file che non è possibile rinominare. E' possibile modificare il nome degli altri file utilizzando il programma di configurazione o modificando manualmente il file `.json`. 

**Attenzione:** I file devono necessariamente avere la estensione e il formato indicato!

## Funzionamento del software
### Translate
Il software di traduzione dei caratteri è uno script autonomo che può funzionare in background, in quanto non richiede l'input dell'utente. Una volta impostati correttamente i parametri nel file, il software è capace di tradurre ogni file posto nella cartella sorgente, copiarlo, spostare la versione tradotta nella cartella di destinazione e farne una copia. Una volta lanciato il programma continua a funzionare fino a che non lo si interrompe con `ctrl+c`.

**Attezione:** Traslate legge i parametri inseriti nei file di configurazione e le tabelle di traduzioe soltanto all'avvio. Per una modifica delle impostazioni, è necessario interrompere la sua esecuzione e riavviarla.

### Configure
Configure non imposta automaticamente i valori indicati dall'utente. Al contrario, crea un file `.json` nella sua directory e lo elabora con i dati disposti dall'utente, che può decidere di salvare eventualmente la configurazione. 
Il software di configurazione ha tre modalità nelle quali può chiedere o inviare informazioni all'utente:
- `>` richiede all'utente un comando,
- `!` richiede un valore per impostare una variabile nel file `settings.json`,
- `-` mostra all'utente una variabile.


#### Comandi Configure
I comandi disponibili all'utente sono i seguenti:
- `?` per mostrare questa lista di comandi,
- `create` per creare un nuovo file di configurazione vergine, 
- `set KEY VALUE` per impostare la variabile `KEY` al valore `VALUE`,
- `reset` per reinserire tutti i valori da capo (esecuzione del set per tutte le variabili nel file di configurazione)
- `show` per visualizzare tutte le varibili e il valore loro assegnato,
- `save PATH` per salvare la configurazione attuale. Prende in ingresso la stringa `PATH`: questa può essere un percorso relativo o assoluto. 
Nella configurazione di default, dove lo script di configurazione è nella cartella dentro il programma di traduzione, è sufficiente digitare `save ..` per salvare il file nella cartella padre. 
- `quit` per uscire dal programma.

#### Variabili di configurazione
All'interno del programma di configurazione, viene chiesto di associare ad ogni variabile un valore. Di seguito, vengono elencati i nomi di ognuna e del suo significato.
- `source_folder` indica la cartella dove i file arrivano,
- `source_copy_folder` indica la cartella dove i file appena arrivati vengono copiati,
- `destin_folder` indica la cartella dove vengono trasferiti i file una volta elaborati dal traduttore,
- `destin_copy_folder` indica la cartella dove i file elaborati dal traduttore vengono copiati,
- `parsing_table` indica il percorso dove si trova la tabella di traduzione. Questa deve essere una tabella CSV. 
- `log_file` indica il percorso dove si trova il file di log, 
- `delay` indica il tempo di attesa dopo ogni trasferimento file in secondi.

Il funzionamento del programma è stato testato con variabili che contenevano *solamente* percorsi assoluti per le cartelle, e percorsi relativi per i file. 

## Installazione
L'installazione del software consta nell'estrazione dell'archivio `.zip` in una cartella a scelta dell'utente. Questo programma non richiede un setup: è quindi portatile e trasportabile su ogni macchina Windows 10 e Windows 2016 Server. La compatibilità con altri sistemi operativi Microsoft **non** è testata. 
























