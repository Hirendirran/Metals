# 🪙 MetalRate Tracker

**MetalRate Tracker** is a Django-based web application that allows users to view **historical and date-wise prices** of precious metals such as **Gold, Silver, Platinum, and Diamond**.  
The application uses a **calendar-based date selector**, **REST-style APIs**, and a **clean card-based UI** to efficiently fetch and visualize metal price data.

---

## 📌 Project Overview

MetalRate Tracker helps users quickly check metal prices for a selected date.  
It is designed to handle **large datasets (10+ years of data)** and presents the information in a simple, user-friendly dashboard.

---

## 🚀 Features

- 📅 **Date-wise metal price lookup**
- 🪙 **Supports Gold, Silver, Platinum, and Diamond**
- 📊 **Efficient handling of large datasets (10+ years)**
- ⚡ **REST-style backend APIs**
- 🎨 **Clean, responsive card-based dashboard UI**
- ❌ **Graceful handling of missing dates**
- 🗄 **SQLite database with indexed date field**

---

## 🛠 Tech Stack

### Backend
- Python  
- Django  
- Django ORM  
- SQLite  

### Frontend
- HTML  
- CSS (Grid & Card Layout)  
- JavaScript (Fetch API)  

---

## 📂 Project Structure

text
MetalRate-Tracker/
├── Trade/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── Templates/
│   └── Trade/
│       └── home.html
├── static/
├── db.sqlite3
├── manage.py
└── README.md

⚙️ Setup Instructions

Clone the repository

git clone https://github.com/your-username/MetalRate-Tracker.git
cd MetalRate-Tracker

Create and activate virtual environment

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux

Install dependencies

pip install django

Run migrations

python manage.py makemigrations
python manage.py migrate

Create superuser (optional)

python manage.py createsuperuser

Run the server

python manage.py runserver

Open in browser

http://127.0.0.1:8000/Trade/home/
