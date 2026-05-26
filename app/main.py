import os

from services.mvr_parser import text_processing_mvr
from services.pdf_service import mvr_analizer

ACTUAL_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.abspath(os.path.join(ACTUAL_DIRECTORY, "..", "data", "input_pdf"))

hola = "mvr jose.pdf"
rute = os.path.join(pdf_folder, hola)

mvr_text = mvr_analizer(rute)
mvr_processed = text_processing_mvr(mvr_text)

print(mvr_processed)
