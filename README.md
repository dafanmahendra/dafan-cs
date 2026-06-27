
# CS Journey — Dafan Mahendra

## Active Roadmap (4 Weeks)
- [x] Grokking Algorithms — Binary Search
- [x] Grokking Algorithms — Selection Sort
- [x] Grokking Algorithms — Recursion
- [ ] Go backend fundamentals

## Progress
| Date | Topic | Status |
|------|-------|--------|
| 2026-06-21 | Binary Search | Done |
| 2026-06-26 | Selection Sort | Done |
| 2026-06-27 | Recursion | Done |

## Chapter 2 — Selection Sort
Selection sort adalah algoritma sorting yang bekerja dengan cara memilih elemen terkecil dari list, lalu memindahkannya ke list hasil. Proses ini diulang sampai semua elemen habis. Intinya, kita selalu mengambil elemen yang paling kecil dari sisa list.

### Cara Kerja
1. Buat list hasil kosong.
2. Copy list asli supaya data awal tidak berubah.
3. Cari elemen terkecil di list kerja.
4. Hapus elemen terkecil dari list kerja.
5. Masukkan elemen itu ke list hasil.
6. Ulangi sampai list kerja habis.

### Kenapa Ada `findSmallest()`
`findSmallest()` adalah fungsi helper. Tugasnya cuma satu: cari indeks elemen terkecil di list saat ini. Fungsi utama `selection_sort()` memanggil helper ini berkali-kali untuk mengambil elemen terkecil satu per satu.

### Kenapa Pakai `copiedArr = list(arr)`
`copiedArr` dibuat sebagai salinan list asli supaya proses `pop()` tidak mengubah data original. Dengan begitu, `arr` tetap aman dan `selection_sort()` bekerja di list kerja sementara.

### Logic
- `arr[0]` dipakai sebagai titik awal pembanding.
- `if arr[i] < smallest` dipakai untuk membandingkan elemen yang sedang dicek.
- `smallest_index = i` dipakai untuk menyimpan posisi elemen terkecil.
- `copiedArr = list(arr)` dipakai agar list asli tidak ikut berubah.

### Complexity
- Time: O(n^2)
- Space: O(n) karena ada salinan list kerja

### File Referensi
- [Selection sort code](algorithms/ch02_selection_sort/selection_sort.py)
- [Selection sort notes](algorithms/ch02_selection_sort/notes.md)

## Chapter 3 — Recursion
Recursion adalah teknik saat sebuah function memanggil dirinya sendiri. Kuncinya ada di base case supaya function berhenti, dan recursive case supaya masalahnya diperkecil sedikit demi sedikit.

### Cara Kerja
1. Tentukan base case, yaitu kondisi berhenti.
2. Tentukan recursive case, yaitu pemanggilan function dengan input yang lebih kecil.
3. Pastikan setiap pemanggilan makin mendekat ke base case.
4. Kalau base case tercapai, function berhenti dan program balik ke call stack sebelumnya.

### Call Stack
Call stack adalah urutan function yang sedang aktif dijalankan Python.
- Function yang dipanggil akan masuk ke stack.
- Function lain yang dipanggil dari dalamnya akan masuk di atasnya.
- Setelah function selesai, Python balik ke function sebelumnya.

### Contoh `greet`
`greet(name)` menunjukkan alur function yang saling memanggil:
- `greet()` print salam awal.
- `greet2()` dipanggil dari dalam `greet()`.
- Setelah `greet2()` selesai, program balik lagi ke `greet()`.
- Lalu `bye()` dipanggil.

### Soal Urutan Function
- Urutan `def` di file tidak harus sama dengan urutan alur panggilannya.
- Yang penting function sudah didefinisikan saat dipanggil oleh program.
- Jadi `bye()` boleh ditaruh di bawah `greet()`.
- `greet2()` juga boleh ditaruh di bawah selama belum dipanggil sebelum definisinya ada.

### File Referensi
- [Recursion code](algorithms/ch03_recursion/recursion.py)
- [Recursion notes](algorithms/ch03_recursion/notes.md)

