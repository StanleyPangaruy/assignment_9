from fpdf import FPDF
import json

with open('resume.json') as f:
    data = json.load(f)

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('2x2p.jpg', 160, 8, 45)
        # Line break
        self.ln(50)

pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()

pdf.set_font('times', 'B', 16)
pdf.set_text_color(0,0,0)
pdf.cell(0, 5, 'PROFILE', ln=True)


pdf.set_font('times', '', 12)
pdf.set_text_color(0,0,0)

for proffy in data["profile"]:
    pdf.cell(0, 10, proffy['name'], ln=True)
    pdf.cell(0, 0, proffy['label'], ln=True)
    pdf.cell(0, 10, proffy['email'], ln=True)
    pdf.cell(0, 0, proffy['phone'], ln=True)
    pdf.cell(0, 10, proffy['birthday'], ln=True)
    pdf.cell(0, 0, proffy['address'], ln=True)
    pdf.cell(0, 10, proffy['summary'], ln=True)
pdf.output('pdf_test2.pdf')
