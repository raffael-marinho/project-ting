
import sys


def txt_importer(path_file):
    txt_imported = []
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            for text in file:
                txt_imported.append(text.strip())
        return txt_imported
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
