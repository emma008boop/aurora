import os

import pypdf


def pdf_reader(file: str):
    reader = pypdf.PdfReader(file)
    page = reader.pages[0]
    text = page.extract_text()

    return text
