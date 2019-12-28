import PIL
from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import math
def Email(e,f):
	
	#s.login("clashrc377@gmail.com","Knayse@123")
	msg=MIMEMultipart()
	body="""Dear Participant, 
			Please find attached herewith your certificate for Pulzion'19. We hope you had a great experience at Pulzion'19. Wish to see you again next year.
			We are extremely sorry for the delay.
			Cheers PICT ACM STUDENT CHAPTER"""
	msg.attach(MIMEText(body,'plain'))
	s=sm.SMTP('smtp.gmail.com',587)
	s.starttls()
	p=MIMEBase('application','pdf')
	s.login("acm5.pict@gmail.com","PascPune@2019")
	msg['From']="acm5.pict@gmail.com"
	msg['To']=e
	msg['Subject']="Pulzion Participation Certificate"
	
	
	filename=f+".PDF";
	#x="/home/yash/Certificate"+f
	# cover_letter = MIMEApplication(open(filename, "rb").read())
 #    cover_letter.add_header('Content-Disposition', 'attachment', filename="file2.pdf")
 #    msg.attach(cover_letter)
	attachment=open(f,"rb")
	
	p.set_payload((attachment).read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s"%filename)
	msg.attach(p)
	
	
	text=msg.as_string()
	s.sendmail("acm5.pict@gmail.com",e,text)
	s.quit()

# draw.text((760,615),"Yash Agarwal",(0,0,0),font=fontt)
# img.save('yash.pdf',"PDF",resolution=100.0)
data=pd.read_csv("resend.csv")
# data=data[0:]
name=data['Name']
name2=data['Name2']
college=data['College']
event=data['Event']
email=data['Email']
# print(college)
cert='certi'
# img=Image.open("template.jpg")
# draw=ImageDraw.Draw(img)
# fontt=ImageFont.truetype("Font.otf",size=40)
# draw.text((760,615),"Yash Agarwal",(0,0,0),font=fontt);
# draw.text((600,675),"Just Coding",(0,0,0),font=fontt);
# draw.text((960,675),"23rd August",(0,0,0),font=fontt);
# draw.text((1300,675),"PICT",(0,0,0),font=fontt);
# img.save(cert,"PDF",resolution=100.0)
x=1800
y=1070
z=0
j=0
m=0;



x1=1800
y1=1063
z1=0
z2=0
z3=0
# print(name2)
bb=float('nan')
for i,k,l,c,n in zip(name,email,event,college,name2):
	img=Image.open("participation.jpg")
	draw=ImageDraw.Draw(img)
	fontt1=ImageFont.truetype("Font.TTF",size=100)
	fontt=ImageFont.truetype("Font.TTF",size=100)
	i=i.upper()
	l=l.upper()
	c=c.upper()
	if(len(i)>25):
		fontt=ImageFont.truetype("Font.TTF",size=70)
		z2=5
		
	draw.text((x1+z1,y1+z2),i,(0,0,0),font=fontt);
	draw.text((1100,1330),l,(0,0,0),font=fontt1);
	if(len(c)<16):
		z3=600
	draw.text((651+z3,1200),c,(0,0,0),font=fontt1);
	#draw.text((1600,675+z),,(0,0,0),font=fontt);
	cert=cert+str(m)
	m+=1
	x1=1800
	y1=1063
	z1=0
	z2=0
	img.save(cert,"PDF",resolution=100.0)
	Email(k,cert)
	
	# n=str(n)
	print(n);
	if(not n=="XXX"):
		img1=Image.open("participation.jpg")
		draw=ImageDraw.Draw(img1)
		n=n.upper()
		l=l.upper()
		c=c.upper()
		if(len(i)>25):
			fontt=ImageFont.truetype("Font.TTF",size=70)
			z2=5
		fontt1=ImageFont.truetype("Font.TTF",size=100)
		fontt=ImageFont.truetype("Font.TTF",size=100)
		draw.text((x1+z1,y1+z2),n,(0,0,0),font=fontt);
		draw.text((1100,1330),l,(0,0,0),font=fontt1);
		if(len(c)<16):
			z3=600
		draw.text((651+z3,1200),c,(0,0,0),font=fontt1);
		cert1="certificate"
		cert1=cert1+str(m)
		m+=1
		img1.save(cert1,"PDF",resolution=100.0)
		Email(k,cert1)
	cert="certi"
	x1=1800
	y1=1063
	z1=0
	z2=0
	z3=0
	j+=1
