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
    fro = 'whatsapp:+14155238886'
    im=[]
    sender = request.form.get('From')
    message = request.form.get('Body')
    media_url = request.form.get('MediaUrl0')
    print(f'{sender} sent {message}')
    if 'Start' in message:
        f=open("count.txt","w")
        f.write('0')
        if not media_url:
            response = MessagingResponse()
            msg = response.message("send the image one by one.")
            return str(response)
    if media_url:
        f=open("count.txt","r")
        i=f.read()
        r = requests.get(media_url)
        content_type = r.headers['Content-Type']
        username = sender.split(':')[1]  # remove the whatsapp: prefix from the number
        if content_type == 'image/jpeg':
            filename = f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}/{i}.jpg'
        elif content_type == 'image/png':
            filename = f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}/{i}.png'
        elif content_type == 'image/gif':
            filename = f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}/{i}.gif'
        else:
            filename = None
        response = MessagingResponse()
        if filename:
            if not os.path.exists(f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}'):
                os.mkdir(f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}')
            with open(filename, 'wb') as f:
                f.write(r.content)
        else:
            return respond('The file that you submitted is not a supported image type.')
        c=int(i)
        c+=1
        f=open("count.txt","w")
        f.write(f'{c}')
        msg = response.message("ok next")
        return str(response)
    if 'End' in message:
        username = sender.split(':')[1]  # remove the whatsapp: pr
        f=open("count.txt","r")
        n=int(f.read())
        im=[]
        for i in range(1,n):
            image_1 = Image.open(f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}/{i}.jpg')
            im_1 = image_1.convert('RGB')
            im.append(im_1)
        image_0 = Image.open(f'C:/Users/himaj/Ctrl-alt-del/uploads/{username}/0.jpg')
        im_0 = image_0.convert('RGB')
        im_1.save(r'H:\XAMPP\htdocs\CtrlAltDel.pdf',save_all=True,append_images=im)
        message = Client.messages.create(body='take this',media_url='https://b040-103-85-204-218.in.ngrok.io/CtrlAltDel.pdf',from_=fro,to=sender)
        response = MessagingResponse()
        msg = response.message("here is the pdf")
        return str(response)
    else:
        return respond('Please send an image!')


if __name__ == "__main__":
    app.run(debug=True)