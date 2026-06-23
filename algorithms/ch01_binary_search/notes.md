# Binary Search — Catatan Belajar

## Ide Dasar
Binary search = algoritma pencarian yang **buang setengah ruang pencarian setiap langkah**.
- Syarat: array **harus sudah terurut**.
- Waktu: O(log n) — jauh lebih cepat dari linear search O(n).

## Cara Kerja
1. Tentukan batas kiri (`low`) dan kanan (`high`).
2. Hitung indeks tengah: `mid = (low + high) // 2`.
3. Bandingkan elemen tengah dengan target:
   - Jika sama → ketemu, return indeks.
   - Jika elemen tengah > target → buang setengah kanan, geser `high = mid - 1`.
   - Jika elemen tengah < target → buang setengah kiri, geser `low = mid + 1`.
4. Ulangi sampai ketemu atau `low > high` (tidak ada).

## Contoh: Cari `7` di `[1, 3, 5, 7, 9, 11, 13]`

### Iterasi 1
```
Array:  [1, 3, 5, 7, 9, 11, 13]
         0  1  2  3  4   5   6

low = 0, high = 6
mid = (0 + 6) // 2 = 3
guess = arr[3] = 7

7 == 7? YA → return 3 ✓ KETEMU
```

## Contoh: Cari `11` di `[1, 3, 5, 7, 9, 11, 13]`

### Iterasi 1
```
low = 0, high = 6
mid = 3
guess = arr[3] = 7

7 > 11? Tidak. 7 < 11? YA.
→ low = 3 + 1 = 4 (buang kiri, fokus ke [9, 11, 13])
```

### Iterasi 2
```
low = 4, high = 6
mid = (4 + 6) // 2 = 5
guess = arr[5] = 11

11 == 11? YA → return 5 ✓ KETEMU
```

## Contoh: Cari `2` (tidak ada) di `[1, 3, 5, 7, 9, 11, 13]`

### Iterasi 1
```
low = 0, high = 6
mid = 3, guess = 7
7 > 2? YA → high = 2 (buang kanan)
```

### Iterasi 2
```
low = 0, high = 2
mid = 1, guess = 3
3 > 2? YA → high = 0 (buang kanan)
```

### Iterasi 3
```
low = 0, high = 0
mid = 0, guess = 1
1 < 2? YA → low = 1 (buang kiri)
```

### Iterasi 4
```
low = 1, high = 0
low > high? YA → KELUAR LOOP
return None ✗ TIDAK ADA
```

## Analisis Waktu
- Array 7 elemen → max 3 iterasi
- Array 1000 elemen → max 10 iterasi
- Array 1 juta elemen → max 20 iterasi

Rumusnya: `log₂(n)` — sangat efisien untuk data besar.

## Kesalahan Umum
1. ❌ Pakai binary search ke array yang belum terurut.
2. ❌ `return None` di dalam loop (berhenti terlalu cepat).
3. ❌ Lupa kondisi `low > high`.
4. ❌ Salah hitung `mid` (pakai pembagian biasa, bukan bulat).

## Kode Python (Benar)
```python
def binary_search(arr, item):
    low = 0  
    high = len(arr) - 1

    while low <= high: 
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None  # ← HARUS di luar loop!
```

## Key Takeaway (Grokking Algorithms Style)
Binary search bekerja dengan **membagi dan menaklukkan**: setiap iterasi, separuh data sudah pasti bukan jawaban, jadi dibuang. Ini seperti mencari halaman di kamus — buka tengah, lihat abjad, langsung tahu harus ke kiri atau kanan.
