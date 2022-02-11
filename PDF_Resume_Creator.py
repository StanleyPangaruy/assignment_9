from email.mime import image
from fpdf import FPDF
import json

#opens the separate json file to read
with open('resume.json') as f:
    data = json.load(f)

#outline for creating a new object
class PDF(FPDF):
    def header(self):
        #self picture
        self.image('2x2p.jpg', 20, 10, 45)
        #facebook logo
        self.image('facebook logo.png', 70, 182, 10)
        #github logo
        self.image('githublogo.png', 70, 197, 10)
        #twitter logo
        self.image('twitterlogo.png', 70, 213, 10)

#specifies the layout, unit and format
pdf = PDF('P', 'mm', 'Letter')
#adds a page
pdf.add_page()
#creates a line
pdf.line(68,60,68,260)

#iterates over the length of the array
for details in data["resume"]:
    #specifies the font style, emphasis and size
    pdf.set_font('helvetica', '', 26)
    #specifes the text color on RGB value
    pdf.set_text_color(0,0,255)
    #specifies the location of the text
    pdf.set_xy(70,20)
    #creates a cell where a user can input texts
    #can manipulate heigh and widght, alignment, and border
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
    #line of codes mostly for subtopics
    pdf.set_font('helvetica', 'B', 12)
    pdf.set_xy(45,65)
    pdf.set_text_color(0,0,255)
    pdf.cell(0, 0, 'PROFILE', ln=True)
    pdf.set_xy(48,95)
    pdf.cell(0, 0, 'SKILLS', ln=True)
    pdf.set_xy(12,115)
    pdf.cell(0, 0, 'RELEVANT EXPERIENCE', ln=True)
    pdf.set_xy(38,160)
    pdf.cell(0, 0, 'EDUCATION', ln=True)
    pdf.set_xy(38,185)
    pdf.cell(0, 0, 'NETWORKS', ln=True)
    pdf.set_xy(39,230)
    pdf.cell(0, 0, 'INTERESTS', ln=True)
    pdf.set_xy(70,115)
    pdf.cell(0, 0, details['xp1'], ln=True)
    pdf.set_xy(70,135)
    pdf.cell(0, 0, details['xp2'], ln=True)

    #set of codes for the user's profile
    pdf.set_font('helvetica', '', 12)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(70,65)
    pdf.cell(0, 0, details['profile'], ln=True)
    pdf.set_xy(70,70)
    pdf.cell(0, 0, details['profile1'], ln=True)
    pdf.set_xy(70,75)
    pdf.cell(0, 0, details['profile2'], ln=True)
    pdf.set_xy(70,80)
    pdf.cell(0, 0, details['profile3'], ln=True)
    pdf.set_xy(70,85)
    pdf.cell(0, 0, details['profile4'], ln=True)

    #print cells for displaying skilss
    pdf.set_xy(70,95)
    pdf.cell(0, 0, details['skill'], ln=True)
    pdf.set_xy(70,100)
    pdf.cell(0, 0, details['skill1'], ln=True)
    pdf.set_xy(70,105)
    pdf.cell(0, 0, details['skill2'], ln=True)
    pdf.set_xy(140,95)
    pdf.cell(0, 0, details['skill3'], ln=True)
    pdf.set_xy(140,100)
    pdf.cell(0, 0, details['skill4'], ln=True)
    pdf.set_xy(140,105)
    pdf.cell(0, 0, details['skill5'], ln=True)

    #cell were printed for the related experiences of the user
    pdf.set_xy(70,120)
    pdf.cell(0, 0, details['xp1a'], ln=True)
    pdf.set_xy(70,125)
    pdf.cell(0, 0, details['xp1b'], ln=True)
    pdf.set_xy(70,140)
    pdf.cell(0, 0, details['xp2a'], ln=True)
    pdf.set_xy(70,145)
    pdf.cell(0, 0, details['xp2b'], ln=True)
    pdf.set_xy(70,150)
    pdf.cell(0, 0, details['xp2c'], ln=True)

    #this part shows the educational attainment as well as the school and location
    pdf.set_xy(70,160)
    pdf.cell(0, 0, details['attain'], ln=True)
    pdf.set_xy(70,165)
    pdf.cell(0, 0, details['school'], ln=True)
    pdf.set_xy(70,170)
    pdf.cell(0, 0, details['schoolp'], ln=True)
    pdf.set_xy(70,175)
    pdf.cell(0, 0, details['sy'], ln=True)

    #print cells for showing the networks of the user
    pdf.set_xy(80,185)
    pdf.cell(0, 0, details['username1'], ln=True)
    pdf.set_xy(80,190)
    pdf.cell(0, 0, details['url1'], ln=True)
    pdf.set_xy(80,200)
    pdf.cell(0, 0, details['username2'], ln=True)
    pdf.set_xy(80,205)
    pdf.cell(0, 0, details['url2'], ln=True)
    pdf.set_xy(80,215)
    pdf.cell(0, 0, details['username3'], ln=True)
    pdf.set_xy(80,220)
    pdf.cell(0, 0, details['url3'], ln=True)

    #Last part, for displaying the user's interest
    pdf.set_xy(70,230)
    pdf.cell(0, 0, details['inter1'], ln=True)
    pdf.set_xy(70,235)
    pdf.cell(0, 0, details['inter2'], ln=True)
    pdf.set_xy(70,240)
    pdf.cell(0, 0, details['inter3'], ln=True)
    pdf.set_xy(70,245)
    pdf.cell(0, 0, details['inter4'], ln=True)
    pdf.set_xy(70,250)
    pdf.cell(0, 0, details['inter5'], ln=True)   
    pdf.set_xy(70,255)
    pdf.cell(0, 0, details['inter6'], ln=True)

#sends the document to a certain destination
#standard output
#can type your own desired filename
pdf.output('PANGARUY_STANLEY.pdf')