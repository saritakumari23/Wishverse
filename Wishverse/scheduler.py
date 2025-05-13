import schedule
import time
import json
import pywhatkit
from datetime import datetime

def send_scheduled_messages():
    with open('messages.json', 'r+') as file:
        messages = json.load(file)
        remaining = []

        for entry in messages:
            now = datetime.now().strftime("%H:%M")
            if now == entry['time']:
                try:
                    pywhatkit.sendwhatmsg_instantly(entry['phone'], entry['message'], wait_time=10)
                    print(f"✅ Message sent to {entry['phone']}")
                except Exception as e:
                    print("❌ Failed:", e)
            else:
                remaining.append(entry)

        file.seek(0)
        file.truncate()
        json.dump(remaining, file, indent=4)

schedule.every(1).minutes.do(send_scheduled_messages)

while True:
    schedule.run_pending()
    time.sleep(1)
