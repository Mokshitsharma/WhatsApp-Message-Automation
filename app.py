import pandas as pd
import pywhatkit as kit
import pyautogui
import time
import webbrowser
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

file_path = r"C:\Users\dell\OneDrive\Desktop\contacts.xlsx"
df = pd.read_excel(file_path)

name_column = "Name"
phone_column = "Phone"

assert name_column in df.columns, "Name column not found in Excel"
assert phone_column in df.columns, "Phone column not found in Excel"

def format_phone_number(phone):
    phone = str(phone).strip().replace(" ", "").replace("-", "")
    if not phone.startswith("+"):
        phone = "+91" + phone
    return phone

def get_first_name(full_name):
    return full_name.split()[0] if pd.notna(full_name) else "Friend"
logging.info("Opening WhatsApp Web...")
webbrowser.open("https://web.whatsapp.com")
time.sleep(20)  

for index, row in df.iterrows():
    phone_number = format_phone_number(row[phone_column])
    first_name = get_first_name(row[name_column])


    if not phone_number[1:].isdigit() or len(phone_number) < 12:
        logging.warning(f"Skipping invalid number: {phone_number}")
        continue

    message = f"Hello {first_name}, this is a test message!"

    try:
        logging.info(f"Sending message to {first_name} at {phone_number}")
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True)
        time.sleep(7)
        pyautogui.press("enter")
        time.sleep(2)
    except Exception as e:
        logging.error(f"Failed to send message to {phone_number}: {e}")

logging.info("✅ All messages sent (or attempted) successfully!")
