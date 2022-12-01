import smtplib
import csv
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ', '
# Define params
rrdpath = '/home/erick/Documentos/Redes3/RRD/'
imgpath = '/home/erick/Documentos/Redes3/IMG/'
fname = 'trend.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "dummycuenta3@gmail.com" #linea de codigo a modiciar para el correo
mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'

def send_alert_attached(subject):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    html = """\
    <html><body>
    <table style="width:80%; border: 2px solid black; border-collapse: collapse;">
    <tr style="height:35px ;">
    <th style="border: 1px solid black;">NOobre del Alumno</th>
    <th style="border: 1px solid black;">Nombre del dispositivo</th>
    <th style="border: 1px solid black;">Version del software</th>
    <th style="border: 1px solid black;">Tiempo de actividad</th>
    <th style="border: 1px solid black;">Fecha y hora del host</th>
    <th style="border: 1px solid black;">COmunidad SNMP</th>
    </tr>
    <tr style="height: 50;"  > 
    <td style="padding: 5px"> Diaz Zamora Erick 4CM14 </td>
    <td style="padding: 5px"> Ubuntu </td> 
    <td style="padding: 5px"> 22.04 </td>
    <td style="padding: 5px"> 152187 </td>
    <td style="padding: 5px"> 2022-11-30 11:32:12 </td>
    <td style="padding: 5px"> comunidadErick </td>
    </tr>

<tr style="padding: 5px;"></tr>
    </table>
</body>
</html>
    """
   

    msg = MIMEMultipart()
    msg.attach(MIMEText(html,'html'))

    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip

    fp = open(imgpath+'deteccionCPU.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()

    

    

    msg.attach(img)
    

    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()
