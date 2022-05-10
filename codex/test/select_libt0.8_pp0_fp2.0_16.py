import select_file

# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'PetGallery_Greeting_Card'

# Assume we know that the image files are all in PNG format
from email.mime.image import MIMEImage

# Open the files in binary mode.  Let the MIMEImage class automatically
# guess the specific image type.
select_file = select_file.SelectFiles()
select_file.file_to_img()

files = [os.path.join(select_file.pet_path, f) for f in os.listdir(select_file.pet_path) if f.endswith('.png')]
