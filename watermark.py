import pypdf
import os

from pypdf import PdfReader, PdfWriter

watermark = PdfReader("wtr.pdf").pages[0]

writer = PdfWriter(clone_from="super.pdf")

for page in writer.pages:
    page.merge_page(watermark, over=False)

writer.write("super-wtr.pdf")