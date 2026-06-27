# Chapter 3 — Recursion

Recursion adalah teknik saat sebuah function memanggil dirinya sendiri. Biasanya dipakai untuk memecah masalah besar jadi versi yang lebih kecil sampai ketemu kondisi berhenti.

## Inti Recursion
- `base case`: kondisi berhenti supaya function tidak jalan terus.
- `recursive case`: bagian yang memanggil function itu sendiri dengan nilai yang lebih kecil.
- Kalau base case tidak ada, program bisa masuk infinite recursion.

## Contoh `countdown`
- `print(time)` menampilkan angka sekarang.
- `if time <= 1` adalah base case.
- `countdown(time - 1)` adalah recursive case.
- Alurnya: 5 -> 4 -> 3 -> 2 -> 1 -> berhenti.

## Call Stack
Call stack adalah urutan function yang sedang aktif diproses Python.
- Function yang dipanggil akan masuk ke stack.
- Kalau function lain dipanggil dari dalamnya, function baru masuk ke atas stack.
- Setelah function selesai, Python balik ke function sebelumnya.

## Contoh `greet`
```python
def greet(name):
	print("hello, " + name + "!")
	greet2(name)
	print("getting ready to say bye!")
	bye()

def bye():
	print("ok, goodbye!")

def greet2(name):
	print("hello again, " + name)

greet("mario")
```

Urutan jalan program:
1. `greet("mario")`
2. print `hello, mario!`
3. panggil `greet2("mario")`
4. print `hello again, mario`
5. balik ke `greet`
6. print `getting ready to say bye!`
7. panggil `bye()`
8. print `ok, goodbye!`

## Soal Urutan Function
- Posisi `def` di file tidak harus urut sesuai alur panggilan.
- Yang penting function sudah didefinisikan saat dipanggil oleh program.
- Jadi `bye()` boleh ditaruh di bawah `greet()`.
- `greet2()` juga boleh di bawah, selama belum dipanggil sebelum definisinya ada.

## Poin Penting
- Recursion butuh base case.
- Recursive call harus membuat masalah makin kecil.
- Call stack membantu menjelaskan kenapa program bisa balik ke baris sebelumnya setelah function selesai.

