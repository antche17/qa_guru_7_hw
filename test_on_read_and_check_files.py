import csv
import io
import zipfile
from io import TextIOWrapper
from openpyxl import load_workbook
from pypdf import PdfReader

with zipfile.ZipFile("/Users/antche/PycharmProjects/qa_guru/qa_guru_7_hw/archive.zip") as zip_file: # открываем архив
    print(zip_file.namelist()) # печатаем названия файлов в архиве


def test_csv():
    with zipfile.ZipFile("/Users/antche/PycharmProjects/qa_guru/qa_guru_7_hw/archive.zip") as zip_file:
        with zip_file.open('example.csv') as csv_file:
            csvreader = list(csv.reader(TextIOWrapper(csv_file, 'utf-8-sig')))
            second_row = csvreader[1]
            print("Вторая строка:", second_row)
            assert second_row == ["12", "30", "23"]
            print("CSV проверен")
test_csv()

def test_xlsx():
    with zipfile.ZipFile("/Users/antche/PycharmProjects/qa_guru/qa_guru_7_hw/archive.zip") as zip_file:
        with zip_file.open('example.xlsx') as xlsx_file:
            in_memory_xlsx = io.BytesIO(xlsx_file.read())
            workbook = load_workbook(in_memory_xlsx)
            sheet = workbook.active
            cell_value = sheet['A1'].value
            print("Значение в ячейке A1:", cell_value)
            assert cell_value == "1"
            print("XLSX проверен")
test_xlsx()

def test_pdf():
    with zipfile.ZipFile("/Users/antche/PycharmProjects/qa_guru/qa_guru_7_hw/archive.zip") as zip_file:
        with zip_file.open('example.pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            text = reader.pages[0].extract_text()
            print(text)
            assert "Python" in text
            print("PDF проверен")
test_pdf()


