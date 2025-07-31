import os
import zipfile


def create_archive():
    with zipfile.ZipFile('/Users/antche/PycharmProjects/qa_guru/qa_guru_7_hw/archive.zip', 'w') as zf:
        for file in ('example.csv', 'example.xlsx', 'example.pdf'):
            add_file = os.path.join('/Users/antche/PycharmProjects/qa_guru/qa_guru_7_hw/FILES',file)
            zf.write(add_file, os.path.basename(add_file))
            print("Архив создан!")

create_archive()


