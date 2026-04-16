# ✈️ Flight Deal Finder

A Python-based automation project that searches for cheap flights and notifies users when prices drop below a defined threshold.

---

## 🚀 Overview

This project integrates multiple APIs to build a real-world flight price monitoring system. It retrieves destination data, searches for flights, compares prices, and sends alerts automatically.

---

## ✨ Features

* 📊 Fetches destination data from Google Sheets using Sheety API
* 🔍 Searches flights using SerpAPI (Google Flights engine)
* 💰 Compares live prices with user-defined target prices
* 🔔 Sends alerts via Twilio (SMS / WhatsApp)
* 🔐 Uses environment variables for secure API key management
* ⚡ Includes request caching to optimize API usage

---

## 🧠 How It Works

1. Destination data is stored in a Google Sheet
2. The app fetches this data via Sheety API
3. For each destination:

   * Searches flights using SerpAPI
   * Finds the cheapest available option
   * Compares with stored "lowest price"
4. If a cheaper flight is found:

   * Updates the sheet
   * Sends a notification

---

## 🛠 Tech Stack

* **Python**
* **Requests / Requests-Cache**
* **SerpAPI (Google Flights)**
* **Sheety API (Google Sheets integration)**
* **Twilio API (Notifications)**

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flight-deal-finder.git
cd flight-deal-finder
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create `.env` file

Add the following:

```
SERPAPI_API_KEY=your_serpapi_key
SHEETY_ENDPOINT=your_sheety_endpoint

TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_VIRTUAL_NUMBER=your_twilio_number
TWILIO_VERIFIED_NUMBER=your_number
TWILIO_WHATSAPP_NUMBER=+14155238886
```

---

### 4. Run the project

```bash
python main.py
```

---

## ⚠️ Limitations

* Flight data depends on SerpAPI and may occasionally return no results for certain routes or dates
* Best results are achieved with near-term travel dates and common routes

---

## 📸 Example Output

```
Getting flights for Paris...
Paris: GBP 120

Lower price flight found!
Sending notification...
```

---

## 🔮 Future Improvements

* Add GUI or web dashboard
* Use more reliable flight APIs (Amadeus / Kiwi)
* Add email notifications
* Add user input for routes

---

## 👨‍💻 Author

Lakshay

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to fork it!
