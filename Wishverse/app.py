from flask import Flask, request, jsonify
import json
from twilio.rest import Client

app = Flask(__name__)

# Twilio setup
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

def send_whatsapp_message(to, body):
    from_whatsapp = 'whatsapp:+14155238886'  # Twilio Sandbox number
    to_whatsapp = f'whatsapp:{to}'
    
    message = client.messages.create(
        body=body,
        from_=from_whatsapp,
        to=to_whatsapp
    )
    return message.sid  # Return SID of the sent message

@app.route('/schedule', methods=['POST'])
def schedule_message():
    data = request.json
    message = data['message']
    phone = data['phone']
    time = data['time']

    new_entry = {
        "message": message,
        "phone": phone,
        "time": time
    }

    with open('messages.json', 'r+') as file:
        current = json.load(file)
        current.append(new_entry)
        file.seek(0)
        json.dump(current, file, indent=4)

    # Call Twilio to send message
    send_whatsapp_message(phone, message)

    return jsonify({"status": "Message scheduled and sent!"})

if __name__ == '__main__':
    app.run(debug=True)
