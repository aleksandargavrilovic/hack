import smtplib 
from email.message import EmailMessage
email = EmailMessage() ## EMAIL poruka
email['from'] = 'xyz name'   ## ko salje
email['to'] = 'xyz id'       ## kome
email['subject'] = 'xyz subject'  ## predmet e-pošte
email.set_content("Xyz content of email") ## sadržaj e-pošte
with smtlib.SMTP(host='smtp.gmail.com',port=587)as smtp:
## slanje zahtjeva serveru     
    smtp.ehlo()          ## server
smtp.starttls()      ## koristi se za slanje podataka između servera i klijenta
smtop.login("email_id","Password") ## ID za prijavu i lozinku za Gmail
smtp.send_message(email)   ## posalji email
print("email send")    ## Ispis poruke o uspesnosti slanja
