from twilio.rest import Client

# Twilio Account SID and Auth Token
account_sid = 'AC039900ce6781a375e025469fc298148d'  # Replace with your Account SID
auth_token = '3046a9655c704f0145d86f22ed7e5105'    # Replace with your Auth Token

# Initialize Twilio client
client = Client(account_sid, auth_token)

def send_whatsapp_message(to, body):
    from_whatsapp = 'whatsapp:+14155238886'  # Twilio Sandbox number (your WhatsApp sandbox number)
    to_whatsapp = f'whatsapp:{to}'  # The recipient's WhatsApp number

    message = client.messages.create(
        body=body,
        from_=from_whatsapp,
        to=to_whatsapp
    )
    
    print(f"Message sent successfully! SID: {message.sid}")

# Example usage
send_whatsapp_message("+917599830625", "Hello this is shreya this side! 🚀")
