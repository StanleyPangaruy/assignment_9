from fpdf import FPDF
import json

with open('resume.json') as f:
    data = json.load(f)

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('2x2p.jpg', 160, 10, 45)
        # Line break
        self.ln(50)

pdf = PDF('P', 'mm', 'Letter')
pdf.add_page()
pdf.set_xy(10,10)
pdf.set_font('times', 'B', 16)
pdf.set_text_color(0,0,0)
pdf.cell(0, 5, 'PROFILE', ln=True)


pdf.set_font('times', '', 12)
pdf.set_text_color(0,0,0)

for details in data["resume"]:
    pdf.cell(0, 10, details['name'], ln=True)
    pdf.cell(0, 0, details['label'], ln=True)
    pdf.cell(0, 10, details['email'], ln=True)
    pdf.cell(0, 0, details['phone'], ln=True)
    pdf.cell(0, 10, details['birthday'], ln=True)
    pdf.cell(0, 0, details['address'], ln=True)
    pdf.cell(0, 10, 'Networks: ', ln=True)
    pdf.cell(0, 0, details['provider1'], ln=True)
    pdf.cell(0, 10, details['username1'], ln=True)
    pdf.cell(0, 0, details['url1'], ln=True)
    pdf.set_xy(100,50)
    pdf.cell(0, 10, details['provider2'], ln=True)
    pdf.set_xy(100,60)
    pdf.cell(0, 0, details['username2'], ln=True)
    pdf.set_xy(100,60)
    pdf.cell(0, 10, details['url2'], ln=True)
    pdf.line(10, 70, 205, 70)

pdf.output('pdf_test2.pdf')

