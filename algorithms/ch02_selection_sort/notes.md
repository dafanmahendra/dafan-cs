# Selection Sort — Catatan Belajar

## Inti Algoritma
Selection sort mengurutkan list dengan cara mencari elemen terkecil dari sisa list, lalu memindahkannya ke list hasil. Proses ini diulang sampai semua elemen habis.

## Struktur Kode
Ada 2 fungsi utama:
- `findSmallest(arr)`
- `selection_sort(arr)`

`findSmallest()` adalah helper. `selection_sort()` adalah fungsi utama yang memanggil helper tersebut berulang kali.

## Penjelasan `findSmallest(arr)`
Fungsi ini mencari indeks elemen terkecil di dalam list.

### Kenapa `smallest = arr[0]`
Kita butuh titik awal pembanding. Elemen pertama dipakai sebagai kandidat awal yang paling aman karena selalu ada selama list tidak kosong.

### Kenapa `if arr[i] < smallest`
Baris ini membandingkan elemen yang sedang dicek dengan kandidat terkecil sementara. Kalau elemen baru lebih kecil, kandidat diganti.

### Kenapa `smallest_index = i`
Karena nanti yang dibutuhkan bukan cuma nilai terkecil, tetapi juga posisi elemen itu di list. Indeks ini dipakai oleh fungsi utama untuk melakukan `pop()`.

### Alur Singkat
Misal list:
```python
[5, 2, 8, 1]
```

Langkahnya:
- awal: `smallest = 5`, `smallest_index = 0`
- lihat `2` → lebih kecil dari `5`, jadi update
- lihat `8` → tidak lebih kecil
- lihat `1` → lebih kecil dari `2`, jadi update lagi

Hasilnya:
- nilai terkecil = `1`
- indeks terkecil = `3`

## Penjelasan `selection_sort(arr)`
Fungsi ini menyusun ulang list dari yang terkecil ke terbesar.

### Kenapa `copiedArr = list(arr)`
`list(arr)` membuat salinan baru dari list asli. Ini penting karena `pop()` akan menghapus elemen dari list kerja. Kalau langsung memakai `arr`, data original ikut berubah.

### Kenapa Ada `newArr`
`newArr` dipakai sebagai tempat hasil akhir yang sudah terurut. Setiap elemen terkecil diambil dari `copiedArr`, lalu dimasukkan ke `newArr`.

### Kenapa Loop Memanggil `findSmallest(copiedArr)`
Karena setiap putaran kita ingin mencari elemen terkecil dari sisa list yang masih ada. Setelah elemen itu diambil, list kerja menjadi lebih pendek, lalu proses diulang.

## Contoh Step-by-Step
Misal:
```python
[5, 2, 8, 1]
```

### Awal
```python
copiedArr = [5, 2, 8, 1]
newArr = []
```

### Iterasi 1
- terkecil = `1`
- `pop(3)`
- `newArr = [1]`
- `copiedArr = [5, 2, 8]`

### Iterasi 2
- terkecil = `2`
- `pop(1)`
- `newArr = [1, 2]`
- `copiedArr = [5, 8]`

### Iterasi 3
- terkecil = `5`
- `pop(0)`
- `newArr = [1, 2, 5]`
- `copiedArr = [8]`

### Iterasi 4
- terkecil = `8`
- `pop(0)`
- `newArr = [1, 2, 5, 8]`
- `copiedArr = []`

Hasil akhir:
```python
[1, 2, 5, 8]
```

## Relasi Antar Fungsi
`findSmallest()` dan `selection_sort()` saling berkaitan.
- `findSmallest()` mencari posisi elemen terkecil.
- `selection_sort()` memakai posisi itu untuk menghapus elemen dan membangun hasil terurut.

Jadi fungsi utama tidak bekerja sendirian. Ia bergantung pada helper untuk menentukan elemen mana yang harus diambil lebih dulu.

## Complexity
- Time: O(n^2)
- Space: O(n)

## Penjelasan
Selection sort itu seperti memilih kartu paling kecil dari tumpukan, lalu memindahkannya ke tumpukan hasil. Ulangi terus sampai tumpukan awal habis.
