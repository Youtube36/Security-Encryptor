# Security-Encryptor
# 🛡️ CipherHub Lite | encrizh Security Suite
**Advanced Cryptography & Steganography Dashboard (v2.0)**

CipherHub Lite adalah aplikasi web sekuriti yang menggabungkan teknik kriptografi klasik dan moden dengan elemen forensik digital. Projek ini direka di bawah identiti **encrizh** untuk mendemonstrasikan integriti data, kerahsiaan, dan ketelusan rangkaian.

---

## 🚀 Ciri-Ciri Utama
* **Multi-Layer Encryption:** Menyokong Shift Cipher, Vigenère Cipher (Polyalphabetic), dan RSA-2048 (Asymmetric).
* **Digital Signature:** Suntikan automatik signature `encrizh` untuk pengesahan identiti (Authenticity).
* **Steganography Support:** Keupayaan menyembunyikan mesej terenkripsi ke dalam piksel imej (LSB).
* **Live Network Intelligence:** Paparan alamat IP, ISP, dan Geolokasi pengguna secara real-time.
* **Interactive GPS Mapping:** Integrasi peta Leaflet.js untuk memaparkan koordinat "Node" aktif.
* **Forensic Audit:** Pengiraan masa pemprosesan (ms) dan penjanaan SHA-256 Hash untuk integriti data.
* **Cyber-Glass UI:** Antaramuka futuristik dengan animasi Laser Scan dan log terminal interaktif.

---

## 🛠️ Teknologi yang Digunakan
* **Backend:** Python 3.x (Flask Framework)
* **Cryptography:** `cryptography` (RSA), `hashlib` (SHA-256)
* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (ES6)
* **Mapping:** Leaflet.js API
* **Image Processing:** Pillow, Stepic (LSB Steganography)
* **Network:** Requests (IP Geolocation API)

---

## 📦 Pemasangan (Setup)

1.  **Klon Repositori:**
    ```bash
    git clone [https://github.com/username/cipherhub-lite.git](https://github.com/username/cipherhub-lite.git)
    cd cipherhub-lite
    ```

2.  **Pasang Library Diperlukan:**
    ```bash
    pip install flask cryptography stepic pillow requests
    ```

3.  **Jalankan Aplikasi:**
    ```bash
    python app.py
    ```
4.  Akses di browser melalui: `http://127.0.0.1:5000`

---

## 📜 Logik Algoritma

### 1. RSA-2048 (Moden)
Menggunakan sepasang kunci (Public & Private). Data dikunci menggunakan kunci awam dan hanya boleh dibuka oleh kunci peribadi yang sepadan.



### 2. Vigenère Cipher (Klasik)
Menggunakan kata kunci `encrizh` untuk anjakan huruf yang dinamik bagi setiap aksara dalam mesej.



### 3. SHA-256 Integrity
Setiap mesej dijana "Digital Fingerprint" unik. Jika data diubah suai walaupun 1-bit, hash akan berubah sepenuhnya.



---

## 🛡️ Analisis Forensik & Geolocation
Sistem ini menjejaki lokasi fizikal pengguna untuk tujuan akauntabiliti. Penggunaan IP Geolocation memberikan data lokasi kasar, manakala Browser GPS memberikan koordinat tepat peranti.



---

## 👨‍💻 Pembangun
Projek ini dibangunkan oleh **encrizh** untuk tujuan pendidikan dan kesedaran keselamatan siber.

**Contact Support:** [WhatsApp](https://wa.me/601163903915)
