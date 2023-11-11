import glob
from pathlib import Path
from fpdf import FPDF

filepaths = glob.glob("Files/*.txt")
pdf = FPDF(orientation="P", format="A4", unit="mm")
for filepath in filepaths:
    titles = Path(filepath).stem.title()
    pdf.add_page()
    pdf.set_font(family="Arial", style="B", size=20)
    pdf.cell(txt=titles, w=20, h=10, ln=1)

pdf.output('output.pdf')