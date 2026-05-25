import os

from services.pdf_service import mvr_analizer

ACTUAL_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.abspath(os.path.join(ACTUAL_DIRECTORY, "..", "data", "input_pdf"))

hola = "mvr jose.pdf"
rute = os.path.join(pdf_folder, hola)

mvr_analizer(rute)
