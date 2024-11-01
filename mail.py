import pymysql
import smtplib
from email.mime.text import MIMEText

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='pass123',
                             db='data')
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT Email FROM plate_detection WHERE result='violation' ")
results = cursor.fetchall()

# Close the database connection
# Retrieve email addresses from the database
cursor.execute("SELECT email FROM plate_detection")
emails = [row[0] for row in cursor.fetchall()]

# Format the email
subject = "fine"
body = "you have violated the traffic rule"
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = "tamanamsharonkumari@gmail.com"
msg['To'] = ", ".join(emails)

# Send the email
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login('tamanamsharonkumari@gmail.com', 'cbknowcordieqmoj')
smtp_server.sendmail('tamanamsharonkumari@gmail.com', emails, msg.as_string())
smtp_server.quit()

# Close the database connection
connection.close()