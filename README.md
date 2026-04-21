# Sistem Manajemen Resep Makanan

Proyek ini adalah tugas UTS mata kuliah Pemrograman Web Lanjutan. 
Saya membuat RESTful API sederhana untuk mengelola resep masakan 
pribadi menggunakan FastAPI dan SQLite.

---

## Teknologi yang Digunakan

-Python 3.14
-FastAPI
-SQLAlchemy (ORM)
-SQLite (database)
-JWT (autentikasi)
-Uvicorn (server)

## Cara Menjalankan

1.Install dependencies:
2.Jalankan server;
3.Buka Swagger Ui di browser:
    http://127.0.0.1:8000/docs  

## Struktur Folder
resep_makanan/
├── main.py
├── database.py
├── models/
│   ├── user.py
│   └── resep.py
├── schemas/
│   ├── user.py
│   └── resep.py
├── routers/
│   ├── auth.py
│   ├── user.py
│   └── resep.py
├── auth/
│   └── jwt.py
├── requirements.txt
└── README.md

## Endpoint API

| Method | Endpoint | Deskripsi | Auth |
|--------|----------|-----------|------|
| POST | /auth/register | Register user baru | Tidak |
| POST | /auth/login | Login dan dapat token JWT | Tidak |
| GET | /users/ | Lihat semua user | Tidak |
| POST | /users/ | Buat user baru | Tidak |
| GET | /users/{id} | Lihat user by ID | Tidak |
| PUT | /users/{id} | Update user | Tidak |
| DELETE | /users/{id} | Hapus user | Tidak |
| GET | /resep/ | Lihat semua resep | Tidak |
| POST | /resep/ | Buat resep baru | Ya (JWT) |
| GET | /resep/{id} | Lihat resep by ID | Tidak |
| PUT | /resep/{id} | Update resep | Tidak |
| DELETE | /resep/{id} | Hapus resep | Tidak |


Dibuat oleh: Suci Sri Aulia — H071241067_kelasA 
Prodi: Sistem Informasi, Universitas Hasanuddin


