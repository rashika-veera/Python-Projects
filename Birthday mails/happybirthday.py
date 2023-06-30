import csv, smtplib, ssl
from datetime import date


today = date.today().strftime('%B %d, %Y')
todays=date.today().strftime('%m-%d')
# print(todays)


message = '''Subject: Happiest Birthday!!!
Hi {name}, 

    I count myself lucky to 
    Have found a buddy like you
    Because the truth is simply 
    That there are very few.

    I would even go as far as
    To say you're one-of-a-kind
    A friend you should hold on to
    If you're fortunate enough to find.

    I'm wishing the happiest birthday
    Possible to you today, best bud.


Thanks
Rashika
'''

from_address = 'rashikaveera@gmail.com'
# You may need to create an app password for Gmail here: https://myaccount.google.com/apppasswords
password = 'dtexbpdxwcjazkdj'
context = ssl.create_default_context()



with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(from_address, password)
    with open('customers.csv') as file:
        reader = csv.reader(file)
        for name, email, bday_date in reader:
            # print(bday_date,todays)
            if bday_date==todays:
                server.sendmail(
                    from_address,
                    email,
                    message.format(name=name).encode("UTF-8"),
                )

