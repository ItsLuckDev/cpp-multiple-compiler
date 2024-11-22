
**README_IT.md (Italiano)**

# Script Batch per la Compilazione di File C++

Questo script Python è progettato per automatizzare il processo di compilazione di tutti i file `.cpp` nella directory corrente utilizzando `g++`. Inoltre, esegue la pulizia dei file `.exe` compilati dopo l'esecuzione, utile quando si vuole verificare semplicemente la riuscita della compilazione senza conservare gli eseguibili.

## Caratteristiche

- **Compilazione Batch**: Rileva e compila automaticamente tutti i file `.cpp` nella directory corrente.
- **Colori Cross-Platform**: Utilizza `colorama` per fornire un output colorato, compatibile sia con Windows che con sistemi Unix-like.
- **Pulizia Automatica**: Dopo la compilazione, elimina i file eseguibili generati.

## Requisiti

- Python 3
- `g++` (GNU Compiler Collection) installato e accessibile dal terminale
- Libreria Python `colorama`

Puoi installare `colorama` con il seguente comando:

```sh
pip install colorama
```

## Come Utilizzare

1. Assicurati di avere Python 3 e `g++` installati nel tuo sistema.
2. Posiziona questo script nella directory dove si trovano i tuoi file `.cpp`.
3. Esegui lo script utilizzando Python:

   ```sh
   python compile_and_cleanup.py
   ```

Lo script farà quanto segue:

- Rileverà tutti i file `.cpp` nella directory.
- Proverà a compilare ogni file usando il comando `g++`.
- Stamperà un output colorato per indicare il successo o il fallimento.
- Cancellerà i file `.exe` generati dopo la compilazione.

## Output Esempio

- I file compilati correttamente sono mostrati in **verde**.
- Gli errori durante la compilazione sono mostrati in **magenta**.
- Le cancellazioni dei file vengono riportate dopo la compilazione.

## Note

- Questo script utilizza `g++` con le opzioni `-Wall` e `-std=c++14` per la compilazione, attivando tutti gli avvisi e imponendo lo standard C++14.
- Lo script è utile per scopi di testing per garantire che tutti i file `.cpp` siano privi di errori.

---

Feel free to customize the information in these README files further to fit the context of your application or environment!
