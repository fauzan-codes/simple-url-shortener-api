# 🚀 FastAPI URL Shortener

## 📌 Deskripsi Project

Project ini adalah sebuah **URL Shortener API** yang dibuat menggunakan:

* ⚡ FastAPI (Backend Framework)
* 🐘 PostgreSQL (Database)

Aplikasi ini memungkinkan user untuk:

* Memasukkan URL panjang
* Mendapatkan URL pendek
* Mengakses URL pendek untuk redirect ke URL asli

Project ini dibuat sebagai **portfolio backend project** untuk memahami:

* REST API
* Database integration
* Backend architecture

---

## 🎯 Tujuan Project

* Belajar FastAPI secara praktis
* Menggunakan PostgreSQL dalam project nyata
* Memahami alur kerja backend (request → process → response)
* Membuat project yang bisa digunakan di dunia nyata

---

## 🧠 Cara Kerja Sistem

1. User mengirim URL panjang
2. Sistem membuat short code unik (contoh: `abc123`)
3. Data disimpan ke database:

   ```
   abc123 → https://example.com
   ```
4. Saat user mengakses:

   ```
   /abc123
   ```

   → sistem akan redirect ke URL asli

---

## 🛠️ Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Uvicorn

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
│
├── requirements.txt
└── README.md
```

---

## 🪜 ROADMAP PENGERJAAN PROJECT

---

### 🟢 PHASE 0 — Setup Environment

**Tujuan:** Menyiapkan semua kebutuhan project

#### ✅ Langkah:

* Install Python
* Install PostgreSQL (via Laragon)
* Install pip package:

  ```
  pip install fastapi uvicorn sqlalchemy psycopg2-binary
  ```

---

### 🟢 PHASE 1 — Belajar Basic FastAPI

**Tujuan:** Memahami API dasar

#### ✅ Yang dipelajari:

* Routing (`GET`, `POST`)
* Response JSON

#### ✅ Output:

Endpoint sederhana:

```
GET /
```

---

### 🟢 PHASE 2 — Setup Database PostgreSQL

**Tujuan:** Membuat database

#### ✅ Langkah:

* Buat database:

  ```
  url_shortener
  ```
* Setup koneksi di `database.py`

---

### 🟢 PHASE 3 — Setup SQLAlchemy

**Tujuan:** Menghubungkan Python dengan database

#### ✅ Buat:

* `database.py` → koneksi DB
* `models.py` → struktur tabel

#### ✅ Tabel utama:

```
id
original_url
short_code
created_at
```

---

### 🟢 PHASE 4 — Core Feature (INTI)

#### 🔹 1. Generate Short Code

* Random string (6 karakter)

#### 🔹 2. Endpoint: Create Short URL

```
POST /shorten
```

Body:

```
{
  "url": "https://example.com"
}
```

---

#### 🔹 3. Simpan ke Database

Mapping:

```
short_code → original_url
```

---

#### 🔹 4. Endpoint Redirect

```
GET /{code}
```

Fungsi:

* Ambil data dari DB
* Redirect ke URL asli

---

### 🟢 PHASE 5 — Testing

**Checklist:**

* [✔] Bisa input URL
* [✔] Short URL berhasil dibuat
* [✔] Redirect berjalan dengan benar

---

### 🟢 PHASE 6 — UI Sederhana (Optional)

* Form input URL
* Tampilkan hasil short link

---

### 🟢 PHASE 7 — Improvement (Next Level)

Fitur tambahan:

* Custom alias
* Hit counter
* Expired link
* Login user
* Dashboard
* Analytics

---

## ⚠️ Tantangan yang Mungkin Dihadapi

* Error koneksi PostgreSQL
* Salah konfigurasi database
* Routing tidak terbaca
* Debugging redirect

---

## 🚀 Cara Menjalankan Project

```
uvicorn app.main:app --reload
```

Buka:

```
http://127.0.0.1:8000/docs
```

---

## 📈 Future Development

* Deploy ke cloud (Railway / Render)
* Tambah authentication
* Tambah analytics dashboard

---

## 👨‍💻 Author

Fauzan

---

## ⭐ Catatan

Project ini dibuat untuk pembelajaran dan pengembangan skill backend.
Fitur akan terus ditambahkan seiring perkembangan.
