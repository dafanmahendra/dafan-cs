
# CS Journey — Dafan Mahendra

## Active Roadmap (4 Weeks)
- [x] Grokking Algorithms — Binary Search
- [x] Grokking Algorithms — Selection Sort
- [ ] Go backend fundamentals

## Progress
| Date | Topic | Status |
|------|-------|--------|
| 2026-06-21 | Binary Search | Done |
| 2026-06-26 | Selection Sort | Done |

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

