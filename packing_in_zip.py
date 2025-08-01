import os
import zipfile
from pathlib import Path

BASE_DIR = Path(__file__).parent
FILES_DIR = BASE_DIR / "FILES"
ARCHIVE_PATH = BASE_DIR / "archive.zip"

def create_archive():
    with zipfile.ZipFile(ARCHIVE_PATH, 'w') as zf:
        for file in ('example.csv', 'example.xlsx', 'example.pdf'):
            add_file = FILES_DIR / file
            zf.write(add_file, os.path.basename(add_file))
            print("Архив создан!")

create_archive()


