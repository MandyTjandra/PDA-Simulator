# Simulasi Mesin PDA (Pushdown Automata) dengan GUI

Repositori ini berisi program simulasi mesin Pushdown Automaton (PDA) berbasis antarmuka grafis (GUI) yang dikembangkan menggunakan Python. Program ini dibuat untuk memenuhi **Tugas Praktikum #3** dan mendemonstrasikan bagaimana mesin state dengan memori *stack* bekerja.

Secara bawaan (*default*), mesin PDA dalam program ini dirancang untuk membaca dan mengenali bahasa formal **aⁿbⁿ** (jumlah string `a` diikuti oleh `b` dengan jumlah yang persis sama, di mana n ≥ 1).

## ✨ Fitur Utama

* **Antarmuka Grafis (GUI):** Dibangun menggunakan pustaka bawaan Python, `Tkinter`, sehingga mudah digunakan tanpa perlu konfigurasi tambahan.
* **Validasi *Real-time*:** Menampilkan status **ACCEPTED ✅** atau **REJECTED ❌** secara instan setelah string diinputkan.
* **Jejak Langkah (Trace Log):** Fitur pelacakan *stack* yang menampilkan langkah demi langkah perubahan *state* dan isi *stack* saat karakter dibaca. Ini sangat membantu untuk proses *debugging* dan pemahaman logika PDA.
* **Keamanan Input:** Validasi bawaan untuk menolak karakter selain alfabet (mencegah *error* akibat input angka atau simbol).
* **Algoritma DFS:** Mendukung penelusuran *Nondeterministic* PDA menggunakan simulasi *stack array* pada Python.

## 💻 Prasyarat

Program ini sangat ringan dan tidak memerlukan instalasi *library* eksternal pihak ketiga (seperti PyQt atau Kivy). Anda hanya membutuhkan:

* **Python 3.x** terinstal di sistem Anda.
* Pustaka `Tkinter` (sudah termasuk secara *default* di sebagian besar instalasi Python standar).

## 🚀 Cara Menjalankan Program

1. *Clone* repositori ini ke komputer lokal Anda:
```bash
git clone [https://github.com/username-anda/nama-repo-anda.git](https://github.com/username-anda/nama-repo-anda.git)

```

2. Buka terminal atau *command prompt* dan arahkan ke direktori proyek:
```bash
cd nama-repo-anda

```


3. Jalankan file Python:
```bash
python pda_simulator.py

```



*(Catatan: Gunakan `python3` jika Anda menggunakan macOS atau Linux).*

## 🧪 Kasus Uji (Test Cases)

Berikut adalah beberapa contoh input untuk menguji fungsionalitas mesin PDA bahasa **aⁿbⁿ**:

| Input String | Status | Alasan |
| --- | --- | --- |
| `ab` | **ACCEPTED** | Kasus minimal (n=1). Memenuhi aturan bahasa. |
| `aaabbb` | **ACCEPTED** | Memenuhi aturan bahasa (n=3). |
| `a` | **REJECTED** | Kekurangan 'b'. *Stack* tidak mencapai *Final State*. |
| `aabbb` | **REJECTED** | Kelebihan 'b'. Terjadi *crash* pada *stack*. |
| `aba` | **REJECTED** | Urutan salah. Mesin tidak bisa membaca 'a' setelah 'b'. |
