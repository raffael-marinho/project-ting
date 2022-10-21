import sys


from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    if data not in instance._file:
        instance.enqueue(data)
    return sys.stdout.write(str(data))


def remove(instance):
    file_details = instance.dequeue()

    if not file_details:
        return sys.stdout.write("Não há elementos\n")

    return sys.stdout.write(
        f'Arquivo {file_details["nome_do_arquivo"]} removido com sucesso\n'
        )


def file_metadata(instance, position):
    try:
        file_details = instance.search(position)
        return sys.stdout.write(str(file_details))
    except IndexError:
        err = "Posição inválida\n"
        sys.stderr.write(err)
