import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('brussban1@gmail.com',password="bveq pnfw qtsq eprv")
otp = ''.join([str(random.randint(0,9)) for i in range(4)])
msg = 'Hello,Your OTP is '+str(otp)
server.sendmail('brussban1@gmail.com','prajotawale1@gmail.com', msg)
server.quit()
print(otp)
print(msg)
print(server)


