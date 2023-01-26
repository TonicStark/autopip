# Autopip
**Autopip** è uno **strumento eseguibile**, che fornisce aiuto per *aggiornare* i pacchetti di un progetto python quando si passa a una *nuova versione*.

## Set Up
### Compilare da Te
Scarica la cartella ZIP o clona il repository con:
```
git clone  https://github.com/TonicStark/autopip.git
```
Quindi installa le dipendenze in un virtualenv, puoi crearne una tramite `python -m venv <nome del virtualenv>`, con:
```
pip install -r requirements.txt
```
Nel *virtualenv*, esegui il seguente comando:
```
pyinstaller --onefile .\autopip.py
```
questo **compilerà** il file `autopip.py`, come un **singolo** *eseguibile*.
Quando finisci il processo di compilazione, dovresti avere un *repo* come questo:
```
.
└── autopip/
    ├── dist
    ├── build
    ├── venv
    ├── .gitignore
    ├── autopip.py
    ├── autopip.spec
    ├── README.md
    └── requirements.txt
```
All'interno di `dist/` dovresti avere un **file**, `autopip.exe` che puoi **eseguire** come un singolo programma, senza dover *attivare* il *virtualenv* ogni volta.

Per usarlo in **ogni** percorso del tuo sistema, devi aggiungere la cartella `.\autopip\dist\` al tuo *Percorso di sistema*: [qui](https://chlee.co/how-to-setup-environment-variables-for-windows-mac-and-linux/) c'è una **guida** su come farlo.
## Scarica (solo Windows)
Altrimenti, puoi *scaricare* nella sezione **Release**, il file già *compilato*, pronto per essere aggiunto al tuo *Percorso di sistema* per **usarlo!**