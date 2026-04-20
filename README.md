# 🚀 FastAPI URL Shortener (Advanced Version)

## 📌 Deskripsi Project

Project ini adalah sebuah **URL Shortener API modern** yang dibangun menggunakan:

* ⚡ FastAPI (High-performance backend framework)
* 🐘 PostgreSQL (Relational Database)
* 🧠 SQLAlchemy (ORM)

Aplikasi ini tidak hanya mempersingkat URL, tetapi juga dilengkapi dengan fitur **analytics, keamanan, dan manajemen link** sehingga mendekati sistem yang digunakan di dunia nyata.

---

## 🎯 Tujuan Project

Project ini dibuat untuk:

* Memahami cara kerja **REST API secara real-world**
* Mengintegrasikan backend dengan **database production-ready**
* Membangun sistem dengan **arsitektur scalable**
* Membuat project **portfolio backend level advanced**

---

## ✨ Fitur Utama

### 🔗 Core Features

* Shorten URL dari link panjang
* Redirect otomatis ke URL asli
* Custom alias (custom short link)
* Duplicate URL detection (hindari data ganda)

---

### 🛡️ Validation & Security

* Validasi URL menggunakan Pydantic
* Input filtering (mencegah data invalid)
* Rate limiting (anti spam request)

---

### 📊 Analytics System

* Hit counter (jumlah klik)
* Tracking waktu akses
* Logging IP Address (optional)
* Data analytics per URL

---

### ⏳ Link Management

* Expired link (link kadaluarsa)
* Delete / manage URL
* Ownership system (jika pakai login)

---

### 🔐 Authentication (Optional)

* User login system
* Setiap link memiliki owner
* Dashboard personal user

---

### 📱 Additional Features

* QR Code generator untuk setiap link
* API documentation otomatis (Swagger)
* Siap integrasi frontend

---

## 🧠 Cara Kerja Sistem

### 🔄 Flow Utama

1. User mengirim URL:

   ```
   POST /shorten
   ```

2. Backend melakukan:

   * Validasi URL
   * Cek apakah URL sudah ada (duplicate check)

3. Sistem membuat short code unik:

   ```
   abc123
   ```

4. Data disimpan ke database:

   ```
   abc123 → https://example.com
   ```

5. Saat user mengakses:

   ```
   GET /abc123
   ```

6. Backend:

   * Cek apakah link expired
   * Simpan data analytics (klik, waktu, dll)
   * Redirect ke URL asli

---

## 🛠️ Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Uvicorn
* Pydantic

---

## 📂 Struktur Project

```
url-shortener/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   │   └── url.py
│   ├── services/
│   │   └── url_service.py
│
├── requirements.txt
└── README.md
```

---

## 🗄️ Struktur Database

### 📌 Table: urls

```
id
original_url
short_code
created_at
expires_at
click_count
user_id (optional)
```

### 📌 Table: clicks (analytics)

```
id
url_id
timestamp
ip_address
```

---

## 🔌 API Endpoints

### 🔹 Create Short URL

```
POST /shorten
```

### 🔹 Redirect URL

```
GET /{code}
```

### 🔹 Delete URL

```
DELETE /url/{id}
```

### 🔹 Get Analytics

```
GET /analytics/{code}
```

### 🔹 Generate QR Code

```
GET /qr/{code}
```

---

## 🧪 Testing

Checklist:

* [✔] URL validasi berjalan
* [✔] Short link berhasil dibuat
* [✔] Redirect berjalan
* [✔] Duplicate URL tidak dibuat ulang
* [✔] Expired link terblokir
* [✔] Analytics tercatat

---

## 🌐 Cara Menjalankan Project (Local)

### 1. Jalankan server

```
uvicorn app.main:app --reload
```

### 2. Akses API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🌍 Testing Online (Ngrok)

Untuk testing bersama teman:

### 1. Jalankan server

```
uvicorn app.main:app --reload
```

### 2. Jalankan ngrok

```
ngrok http 8000
```

### 3. Gunakan URL dari ngrok

```
https://xxxxx.ngrok.io
```

---

## ⚠️ Catatan Ngrok

* URL akan berubah setiap restart
* Gunakan hanya untuk testing
* Pastikan BASE_URL mengikuti URL ngrok

---

## 🚀 Deployment (Next Step)

Platform yang bisa digunakan:

* Railway
* Render
* VPS / Cloud Server

---

## 📈 Future Development

* Custom domain (contoh: fauzan.my.id)
* Advanced analytics dashboard (grafik)
* Geo location tracking
* API key system
* Link password protection

---

## 👨‍💻 Author

Fauzan

---

## ⭐ Kesimpulan

Project ini bukan sekadar URL shortener biasa, tetapi sudah mencakup:

> ✅ Backend architecture
> ✅ Database design
> ✅ Real-world feature
> ✅ Production-ready mindset

Sehingga cocok digunakan sebagai **portfolio backend developer**.

---
