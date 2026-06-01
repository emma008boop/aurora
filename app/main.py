import os

from services.loss_run_parser import loss_run_parser
from services.mvr_parser import text_processing_mvr
from services.pdf_service import pdf_reader

ACTUAL_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.abspath(os.path.join(ACTUAL_DIRECTORY, "..", "data", "input_pdf"))

mvr = "mvr jose.pdf"
loss_run = "loss_run_standard_draft.pdf"
mvr_rute = os.path.join(pdf_folder, mvr)
loss_run_rute = os.path.join(pdf_folder, loss_run)

mvr_text = pdf_reader(mvr_rute)
mvr_processed = text_processing_mvr(mvr_text)

loss_run_text = pdf_reader(loss_run_rute)
loss_run_processed = loss_run_parser(loss_run_text)

print(f"MVR \n{mvr_processed}")
print(f"\n Loss Run \n{loss_run_processed}")
