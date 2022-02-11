from fpdf import FPDF
import json

with open('resume2.json') as f:
    data = json.load(f)

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('2x2p.jpg', 20, 10, 45)
        # Line break
        self.ln(50)

pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_font('symbol', '', 16)
pdf.set_text_color(0,0,0)
pdf.line(68,60,68,260)

for details in data["resume"]:
    pdf.set_font('helvetica', '', 26)
    pdf.set_text_color(0,0,255)
    pdf.set_xy(70,20)
    pdf.cell(0, 10, details['name'], ln=True)
    pdf.set_font('helvetica', '', 12)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(70,30)
    pdf.cell(0, 10, details['label'], ln=True)
    pdf.set_font('helvetica', '', 11)
    pdf.set_xy(70,40)
    pdf.cell(0, 0, details['phone'], ln=True)
    pdf.set_xy(102,40)
    pdf.cell(0, 0, details['email'], ln=True)
    pdf.set_xy(70,45)
    pdf.cell(0, 0, details['address'], ln=True)
    pdf.set_font('helvetica', 'B', 12)
    pdf.set_xy(45,65)
    pdf.set_text_color(0,0,255)
    pdf.cell(0, 0, 'PROFILE', ln=True)
    pdf.set_xy(48,85)
    pdf.cell(0, 0, 'SKILLS', ln=True)
    pdf.set_xy(30,105)
    pdf.cell(0, 0, 'WORK HISTORY', ln=True)
    pdf.set_xy(38,125)
    pdf.cell(0, 0, 'EDUCATION', ln=True)
    pdf.set_xy(38,150)
    pdf.cell(0, 0, 'NETWORKS', ln=True)
pdf.output('pdf_test2.pdf')