from twilio.rest import Client 
 
account_sid = 'AC4a4e3b1f97a09184b674c170aad715bc' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Heyy...the bot is ready',      
                              to='whatsapp:+919048223801' 
                          ) 
 
print(message.sid)