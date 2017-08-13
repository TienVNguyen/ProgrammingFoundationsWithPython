from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "ACcfe182a2172a227a901ee77666501606"
# Your Auth Token from twilio.com/console
auth_token  = "6cfbf6a7dc48d8a6e2206125afd15db1"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    to="+16269883765", 
    from_="+12243728400",
    body="Hello from Python!")

print(message.sid)
