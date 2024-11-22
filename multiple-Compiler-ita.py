import os
import subprocess
from colorama import Fore, Style, init

# Inizializza colorama per supportare colori anche su Windows
init(autoreset=True)

def compile_and_cleanup_cpp_files():
    # Ottieni la lista dei file nella directory corrente
    files_in_directory = os.listdir('.')
    
    # Lista per tenere traccia dei file compilati
    compiled_files = []

    # Itera su tutti i file della directory
    for file_name in files_in_directory:
        # Controlla se il file ha l'estensione .cpp
        if file_name.endswith('.cpp'):
            # Costruisci il nome del file compilato
            compiled_file_name = 'compiled_' + os.path.splitext(file_name)[0] + '.exe'

            # Comando g++ da eseguire
            command = f"g++ -Wall -std=c++14 {file_name} -o {compiled_file_name}"
            print(f"{Fore.YELLOW}File compilato: {file_name}")

            # Esegui il comando usando subprocess
            try:
                subprocess.run(command, shell=True, check=True)
                print(f"{Fore.GREEN}Compilato con successo: {compiled_file_name}")
                # Aggiungi il file compilato alla lista
                compiled_files.append(compiled_file_name)
            except subprocess.CalledProcessError as e:
                print(f"{Fore.MAGENTA}Errore nella compilazione del file {file_name}: {e}")

    # Cancella i file compilati dopo la compilazione
    for compiled_file in compiled_files:
        try:
            os.remove(compiled_file)
            print(f"File compilato cancellato: {compiled_file}")
        except OSError as e:
            print(f"{Fore.RED}Errore durante la cancellazione del file {compiled_file}: {e}")

if __name__ == "__main__":
    compile_and_cleanup_cpp_files()