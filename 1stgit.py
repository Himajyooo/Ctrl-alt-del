import os
import requests
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from PIL import Image
from twilio.rest import Client

load_dotenv()

Client = Client("AC4a4e3b1f97a09184b674c170aad715bc","ed386c0a50cc47cb530c5592430940f3")

app = Flask(__name__)

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)


@app.route('/sms', methods=['POST'])
def reply():
    sender = request.form.get('From')
    message = request.form.get('Body')
    media_url = request.form.get('MediaUrl0')
    fro = 'whatsapp:+14155238886'
    print(f'{sender} sent {message}')
    if media_url:
        r = requests.get(media_url)
        content_type = r.headers['Content-Type']
        username = sender.split(':')[1]  # remove the whatsapp: prefix from the number
        if content_type == 'image/jpeg':
            filename = f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}/{message}.jpg'
        elif content_type == 'image/png':
            filename = f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}/{message}.png'
        elif content_type == 'image/gif':
            filename = f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}/{message}.gif'
        else:
            filename = None
        response = MessagingResponse()
        if filename:
            if not os.path.exists(f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}'):
                os.mkdir(f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}')
            with open(filename, 'wb') as f:
                f.write(r.content)

            image_1 = Image.open(filename)
            im_1 = image_1.convert('RGB')
            im_1.save(r'H:\XAMPP\htdocs\CtrlAltDel.pdf')
            
            message = Client.messages.create(body='take this',media_url='https://4f2a-103-85-204-218.in.ngrok.io/CtrlAltDel.pdf',from_=fro,to=sender)
            return str(response)

        else:
            return respond('The file that you submitted is not a supported image type.')
    else:
        return respond('Please send an image!')


if __name__ == "__main__":
    app.run(debug=True)
