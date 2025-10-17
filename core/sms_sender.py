from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC35393a14e05c17adb95a5c60e0c0093e'
auth_token = 'c325aad61929d0d5bb951de492c07a53      '
client = Client(account_sid, auth_token)

def send_sms(to, body):
    message = client.messages.create(
        body=body,
        from_='your_twilio_number',
        to=to
    )
    print(f"Sent message SID: {message.sid}")