## *Praktikum 4*

Program pertama yang akan dibuat adalah Program untuk menampilkan angka pertama dan kedua dan masukan operator dan mendapat hasil dari input

Berikut flowchartnya

![Diagram Tanpa Judul drawio](https://github.com/user-attachments/assets/20e05071-5a47-4586-a532-1e6268dd0fbb)

*Program akan meminta kita untuk memasukkan nama, nim, nilai tugas, nilai uts, nilai uas dan tambah data :*

![Diagram Tanpa Judul drawio](https://github.com/user-attachments/assets/8bff8aea-6919-4f3d-8fea-5ca57de7a7f3)

**Penjelasan Code**

**1.**

```
def hitung_nilai_akhir(tugas, uts, uas):
    """Hitung nilai akhir berdasarkan bobot tugas, UTS, dan UAS."""
    bobot_tugas = 0.3
    bobot_uts = 0.35
    bobot_uas = 0.35
    return (tugas * bobot_tugas) + (uts * bobot_uts) + (uas * bobot_uas)

data_mahasiswa = []
while True:
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = int(input("Nilai Tugas: "))
    uts = int(input("Nilai UTS: "))
    uas = int(input("Nilai UAS: "))

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa.append([nama, nim, tugas, uts, uas, nilai_akhir])

    tambah_data = input("Tambah data (ya/tidak)? ")
    if tambah_data.lower() != 'ya':
        break

# Menampilkan data dalam bentuk tabel
print("=" * 71)
print("| No | Nama            | NIM        | Tugas | UTS   | UAS   | Akhir   |")
print("=" * 71)
for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"| {i:<2} | {mahasiswa[0]:<15} | {mahasiswa[1]:<10} | {mahasiswa[2]:<5} | {mahasiswa[3]:<5} | {mahasiswa[4]:<5} | {mahasiswa[5]:<7.2f} |")
print("=" * 71)
```

**Penjelasan**
1.	Menerima input: Fungsi ini menerima tiga argumen, yaitu nilai tugas, nilai UTS, dan nilai UAS.
2.	Mendefinisikan bobot: Bobot masing-masing komponen (tugas, UTS, dan UAS) telah ditentukan.
3.	Perhitungan: Nilai akhir dihitung dengan mengalikan nilai masing-masing komponen dengan bobotnya, lalu dijumlahkan.
4.	Mengembalikan hasil: Fungsi ini mengembalikan nilai akhir yang telah dihitung.
Bagian Input Data Mahasiswa
List data_mahasiswa: Digunakan untuk menyimpan data setiap mahasiswa dalam bentuk list. Setiap elemen dalam list adalah sebuah list yang berisi nama, NIM, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir.
Perulangan while True: Perulangan ini akan terus berjalan hingga pengguna memilih untuk berhenti.
Input data: Pada setiap iterasi, pengguna diminta untuk memasukkan nama, NIM, nilai tugas, nilai UTS, dan nilai UAS.
Panggilan fungsi: Nilai akhir dihitung menggunakan fungsi hitung_nilai_akhir dan hasilnya ditambahkan ke dalam list data_mahasiswa.
Kondisi berhenti: Perulangan akan berhenti jika pengguna memasukkan "tidak" atau kata lain yang bukan "ya" ketika ditanya apakah ingin menambahkan data lagi.
Menampilkan Data dalam Bentuk Tabel
Pembatas: Garis sama dengan (=) digunakan untuk membuat pembatas tabel agar tampilan lebih rapi.
Judul kolom: Dicetak judul kolom untuk setiap data yang telah dimasukkan (No, Nama, NIM, Tugas, UTS, UAS, Akhir).
Perulangan: Setiap data mahasiswa dalam list data_mahasiswa akan diakses dan dicetak dalam format tabel.
Format cetak: Menggunakan format string (f-string) untuk mengatur tampilan data, termasuk lebar kolom dan jumlah desimal untuk nilai akhir.
