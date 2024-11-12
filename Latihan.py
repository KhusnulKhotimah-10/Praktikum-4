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