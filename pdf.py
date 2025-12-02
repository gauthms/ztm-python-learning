import pypdf
import sys
from pypdf import PdfWriter

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")

pdf_combiner(inputs)