from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from translate import Translator

app = Flask(__name__)

translator= Translator(to_lang="German")

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    translation = translator.translate(msg)
    # Create reply
    resp = MessagingResponse()
    resp.message("In German it is: {}".format(translation))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

