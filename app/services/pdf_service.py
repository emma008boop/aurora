import os

import pypdf


def mvr_analizer(file: str):
    reader = pypdf.PdfReader(file)
    page = reader.pages[0]
    text = page.extract_text()

    print(text)
