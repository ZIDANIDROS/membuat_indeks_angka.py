# A. ANGKA INDEKS RELATIF SEDERHANA
def masukkan_data():
    data = {}
    banyak_tahun = int(input("Masukkan jumlah tahun: "))

    for i in range(banyak_tahun):
        tahun = int(input(f"Masukkan tahun ke-{i+1}: "))
        harga = float(input("Masukkan harga: "))
        kuantitas = float(input("Masukkan kuantitas: "))
        nilai = float(input("Masukkan nilai: "))
        data[tahun] = {'harga': harga, 'kuantitas': kuantitas, 'nilai': nilai}

    return data

#     1. Angka Indeks Harga Relatif Sederhana:
def hitung_ihr(data, tahun_referensi):
    harga_referensi = data[tahun_referensi]['harga']
    indeks_harga = {}

    for tahun, nilai in data.items():
        indeks_harga[tahun] = (nilai['harga'] / harga_referensi) * 100

    return indeks_harga

#     2. Angka Indeks Kuantitas Relatif Sederhana:
def hitung_iqr(data, tahun_referensi):
    kuantitas_referensi = data[tahun_referensi]['kuantitas']
    indeks_kuantitas = {}

    for tahun, nilai in data.items():
        indeks_kuantitas[tahun] = (nilai['kuantitas'] / kuantitas_referensi) * 100

    return indeks_kuantitas

#     3. Angka Indeks Nilai Relatif Sederhana:
def hitung_inr(data, tahun_referensi):
    nilai_referensi = data[tahun_referensi]['nilai']
    indeks_nilai = {}

    for tahun, nilai in data.items():
        indeks_nilai[tahun] = (nilai['nilai'] / nilai_referensi) * 100

    return indeks_nilai

data = masukkan_data()
tahun_referensi = int(input("Masukkan tahun referensi: "))

hasil_ihr = hitung_ihr(data, tahun_referensi)
hasil_iqr = hitung_iqr(data, tahun_referensi)
hasil_inr = hitung_inr(data, tahun_referensi)

print("\n1. Angka Indeks Harga Relatif Sederhana:")
print(hasil_ihr)

print("\n2. Angka Indeks Kuantitas Relatif Sederhana:")
print(hasil_iqr)

print("\n3. Angka Indeks Nilai Relatif Sederhana:")
print(hasil_inr)


def naik_turun_dari_tahun_dasar(indeks, tahun_referensi):
    for tahun, nilai in indeks.items():
        if tahun != tahun_referensi:
            if nilai > indeks[tahun_referensi]:
                print(f"Indeks pada tahun {tahun} naik dari tahun referensi.")
            elif nilai < indeks[tahun_referensi]:
                print(f"Indeks pada tahun {tahun} turun dari tahun referensi.")
            else:
                print(f"Indeks pada tahun {tahun} sama dengan tahun referensi.")

print("\nPerbandingan dengan Tahun Dasar:")
print("1. Angka Indeks Harga Relatif Sederhana:")
naik_turun_dari_tahun_dasar(hasil_ihr, tahun_referensi)

print("\n2. Angka Indeks Kuantitas Relatif Sederhana:")
naik_turun_dari_tahun_dasar(hasil_iqr, tahun_referensi)

print("\n3. Angka Indeks Nilai Relatif Sederhana:")
naik_turun_dari_tahun_dasar(hasil_inr, tahun_referensi)

def naik_turun_dari_tahun_dasar(indeks, tahun_referensi):
    for tahun, nilai in indeks.items():
        if tahun != tahun_referensi:
            perubahan_persen = ((nilai - indeks[tahun_referensi]) / indeks[tahun_referensi]) * 100

            if nilai > indeks[tahun_referensi]:
                print(f"Indeks pada tahun {tahun} naik dari tahun referensi sebesar {abs(perubahan_persen):.2f}%.")
            elif nilai < indeks[tahun_referensi]:
                print(f"Indeks pada tahun {tahun} turun dari tahun referensi sebesar {abs(perubahan_persen):.2f}%.")
            else:
                print(f"Indeks pada tahun {tahun} sama dengan tahun referensi.")

print("\nPerbandingan dengan Tahun Dasar:")
print("1. Angka Indeks Harga Relatif Sederhana:")
naik_turun_dari_tahun_dasar(hasil_ihr, tahun_referensi)

print("\n2. Angka Indeks Kuantitas Relatif Sederhana:")
naik_turun_dari_tahun_dasar(hasil_iqr, tahun_referensi)

print("\n3. Angka Indeks Nilai Relatif Sederhana:")
naik_turun_dari_tahun_dasar(hasil_inr, tahun_referensi)
