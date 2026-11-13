<!-- readme-refresh 2026-11 -->
<div align="center">

# 💌 WhatsApp Message Automation

**Personalised greetings to an Excel contact list**

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/pywhatkit-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="pywhatkit" /> <img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" alt="Excel" />

</div>

## ✨ Highlights

- Reads names and numbers from Excel
- Sends a personalised message to each

<!-- body -->
Here is a README file for your WhatsApp bulk messaging automation project:

***

# WhatsApp Bulk Message Sender

A Python script that automates sending personalized WhatsApp messages to a list of contacts imported from an Excel file using `pywhatkit` and `pyautogui`.

## Features

- Reads contact data (name and phone number) from an Excel file
- Automatically formats phone numbers (adds +91 for Indian numbers)
- Extracts first name for personalization
- Sends customized WhatsApp messages via WhatsApp Web
- Logs message status and errors
- Handles invalid numbers gracefully

## Requirements

- Python 3.x
- pandas
- pywhatkit
- pyautogui
- openpyxl (for reading `.xlsx` files)

Install dependencies:

```bash
pip install pandas pywhatkit pyautogui openpyxl
```

## Setup

1. Prepare an Excel file (`contacts.xlsx`) with columns:
   - `Name`: Full name of the contact
   - `Phone`: Phone number (with or without country code)

2. Update the `file_path` in the script to point to your Excel file.

3. Ensure WhatsApp Web is accessible and you're logged in via browser.

## Usage

1. Run the script:

```bash
python whatsapp_sender.py
```

2. The script will:
   - Open WhatsApp Web in your default browser
   - Wait 20 seconds for you to scan the QR code (if not already logged in)
   - Iterate through each contact
   - Send a personalized message using WhatsApp Web

3. Example message sent:
   ```
   Hello Ravi, this is a test message!
   ```

## How It Works

- Uses `pandas` to read contact data from Excel.
- Formats phone numbers to international format (e.g., +91XXXXXXXXXX).
- Uses `pywhatkit` to open WhatsApp Web and pre-fill the message.
- Uses `pyautogui.press("enter")` to send the message instantly.
- Includes error handling and logging for robust execution.

## Notes

- Make sure your internet connection is stable.
- Do not minimize the browser during execution — WhatsApp Web must stay active.
- Sending too many messages quickly may trigger WhatsApp rate limits.
- Always respect privacy and use responsibly.

## License

This project is open-source under the MIT License.

***

This README provides a clear, professional overview of your automation script. Let me know if you'd like to add features like message templates, delay control, or screenshot handling!Here is a README file for your WhatsApp bulk messaging automation script:

***

# WhatsApp Bulk Message Sender

A Python-based automation tool that sends personalized WhatsApp messages to multiple contacts using data from an Excel file. The script leverages `pywhatkit` and `pyautogui` to interact with WhatsApp Web.

## Features

- Imports contact list from Excel (name and phone number)
- Automatically formats Indian phone numbers with +91
- Personalizes messages using the recipient’s first name
- Opens WhatsApp Web and sends messages instantly
- Logs operations and errors for monitoring
- Skips invalid phone numbers gracefully

## Requirements

- Python 3.x
- pandas
- pywhatkit
- pyautogui
- openpyxl (for `.xlsx` support)

Install dependencies:

```bash
pip install pandas pywhatkit pyautogui openpyxl
```

## Setup

1. Prepare an Excel file (`contacts.xlsx`) with two columns:
   - `Name`: Full name of the contact
   - `Phone`: Phone number (can be in any format)

2. Update the `file_path` in the script to match your file location.

## Usage

1. Run the script:

```bash
python whatsapp_sender.py
```

2. The script will:
   - Open WhatsApp Web in your browser
   - Wait 20 seconds for QR code scan (if not already logged in)
   - Send a message to each contact in the list

3. Example message:
   ```
   Hello Amit, this is a test message!
   ```

## How It Works

- Reads the Excel file using `pandas`.
- Formats phone numbers to international standard.
- Uses `pywhatkit.sendwhatmsg_instantly()` to open WhatsApp Web with the message pre-filled.
- Simulates pressing Enter via `pyautogui` to send the message.
- Logs each step and handles exceptions to prevent crashes.

## Important Notes

- Ensure WhatsApp Web is accessible and your phone is connected.
- Do not close or minimize the browser during execution.
- Avoid sending too many messages rapidly to prevent account flags.
- Use responsibly and with recipient consent.

## License

MIT License — free for personal and educational use.

***

This README clearly explains your script’s functionality, setup, and usage. Let me know if you'd like to enhance it with features like message templates or scheduling!

---

<div align="center"><sub>Built by <a href="https://github.com/Mokshitsharma">Mokshit Sharma</a> · <a href="https://mokshitsharma27.vercel.app/">Portfolio</a> · <a href="https://www.linkedin.com/in/mokshit-sharma-75b5ab305">LinkedIn</a></sub></div>
