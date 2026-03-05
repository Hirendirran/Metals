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

git clone https://github.com/Hirendirrrran/Metals.git
## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/MetalRate-Tracker.git
cd MetalRate-Tracker
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Open in Browser

```
http://127.0.0.1:8000/
```

http://127.0.0.1:8000/Trade/home/
