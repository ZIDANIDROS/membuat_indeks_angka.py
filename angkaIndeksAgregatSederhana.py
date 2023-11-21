# Fungsi input jumlah data kain
def input_jumlah_kain():
    return int(input("Masukkan jumlah jenis kain: "))

# Fungsi input jenis kain
def input_nama_kain(jumlah_kain):
    jenis_kain = []
    for i in range(jumlah_kain):
        kain = input(f"Masukkan jenis kain ke-{i + 1}: ")
        jenis_kain.append(kain)
    return jenis_kain

# Fungsi input harga kain per tahun
def input_harga_kain(jenis_kain, jumlah_tahun):
    data_harga = {}
    for tahun in range(jumlah_tahun):
        tahun_data = {}
        print(f"\nTahun {tahun + 1}:")
        for kain in jenis_kain:
            harga = float(input(f"Harga kain {kain}: "))
            tahun_data[kain] = harga
        data_harga[tahun + 1] = tahun_data
    return data_harga

# Fungsi utama untuk menghitung indeks
def hitung_angka_indeks_harga(data_harga, tahun_referensi):
    harga_referensi = data_harga[tahun_referensi]
    angka_indeks = {}

    for tahun, harga in data_harga.items():
        indeks_tahun = {}
        for kain, hrg in harga.items():
            indeks_tahun[kain] = (hrg / harga_referensi[kain]) * 100
        angka_indeks[tahun] = indeks_tahun

    return angka_indeks

# Fungsi untuk menghitung total harga seluruh kain pada setiap tahun
def hitung_total_harga(data_harga):
    total_harga_per_tahun = {}
    for tahun, harga_per_tahun in data_harga.items():
        total_harga = sum(harga_per_tahun.values())
        total_harga_per_tahun[tahun] = total_harga
    return total_harga_per_tahun

# Fungsi untuk menghitung perbandingan total harga seluruh kain antara dua tahun
def perbandingan_total_harga(harga_per_tahun):
    total_harga_tahun_1 = harga_per_tahun.get(1, 0)  # Mendapatkan total harga tahun 1
    total_harga_tahun_2 = harga_per_tahun.get(2, 0)  # Mendapatkan total harga tahun 2

    if total_harga_tahun_2 != 0:  # Memastikan pembaginya tidak nol
        perbandingan = (total_harga_tahun_1 / total_harga_tahun_2) * 100
        return perbandingan
    else:
        return 0

# Fungsi input data dari pengguna
def input_data():
    jumlah_kain = input_jumlah_kain()
    jenis_kain = input_nama_kain(jumlah_kain)
    jumlah_tahun = int(input("\nMasukkan jumlah tahun: "))

    harga_kain = input_harga_kain(jenis_kain, jumlah_tahun)

    return jenis_kain, jumlah_tahun, harga_kain

# Input data dari pengguna
jenis_kain, jumlah_tahun, harga_kain = input_data()

# Menggunakan fungsi untuk menghitung total harga seluruh kain pada setiap tahun
total_harga_per_tahun = hitung_total_harga(harga_kain)

# Menampilkan total harga seluruh kain pada setiap tahun
print("\nTotal Harga Seluruh Kain per Tahun:")
for tahun, total_harga in total_harga_per_tahun.items():
    print(f"Tahun {tahun}: {total_harga}")

# Menggunakan fungsi untuk menghitung perbandingan total harga seluruh kain antara tahun 1 dan tahun 2
perbandingan = perbandingan_total_harga(total_harga_per_tahun)
print(f"\nPerbandingan Total Harga Kain Tahun 1 dengan Tahun 2: {perbandingan}%")

######################################

# Fungsi input jumlah data kain
def input_jumlah_kain():
    return int(input("Masukkan jumlah jenis kain: "))

# Fungsi input jenis kain
def input_nama_kain(jumlah_kain):
    jenis_kain = []
    for i in range(jumlah_kain):
        kain = input(f"Masukkan jenis kain ke-{i + 1}: ")
        jenis_kain.append(kain)
    return jenis_kain

# Fungsi input kuantitas kain per tahun
def input_kuantitas_kain(jenis_kain, jumlah_tahun):
    data_kuantitas = {}
    for tahun in range(jumlah_tahun):
        tahun_data = {}
        print(f"\nTahun {tahun + 1}:")
        for kain in jenis_kain:
            kuantitas = float(input(f"Kuantitas kain {kain}: "))
            tahun_data[kain] = kuantitas
        data_kuantitas[tahun + 1] = tahun_data
    return data_kuantitas

# Fungsi utama untuk menghitung indeks
def hitung_angka_indeks_kuantitas(data_kuantitas, tahun_referensi):
    kuantitas_referensi = data_kuantitas[tahun_referensi]
    angka_indeks = {}

    for tahun, kuantitas in data_kuantitas.items():
        indeks_tahun = {}
        for kain, qty in kuantitas.items():
            indeks_tahun[kain] = (qty / kuantitas_referensi[kain]) * 100
        angka_indeks[tahun] = indeks_tahun

    return angka_indeks

# Fungsi untuk menghitung total kuantitas seluruh kain pada setiap tahun
def hitung_total_kuantitas(data_kuantitas):
    total_kuantitas_per_tahun = {}
    for tahun, kuantitas_per_tahun in data_kuantitas.items():
        total_kuantitas = sum(kuantitas_per_tahun.values())
        total_kuantitas_per_tahun[tahun] = total_kuantitas
    return total_kuantitas_per_tahun

# Fungsi untuk menghitung perbandingan total kuantitas seluruh kain antara dua tahun
def perbandingan_total_kuantitas(kuantitas_per_tahun):
    total_kuantitas_tahun_1 = kuantitas_per_tahun.get(1, 0)  # Mendapatkan total kuantitas tahun 1
    total_kuantitas_tahun_2 = kuantitas_per_tahun.get(2, 0)  # Mendapatkan total kuantitas tahun 2

    if total_kuantitas_tahun_2 != 0:  # Memastikan pembaginya tidak nol
        perbandingan = (total_kuantitas_tahun_1 / total_kuantitas_tahun_2) * 100
        return perbandingan
    else:
        return 0

# Fungsi input data dari pengguna
def input_data():
    jumlah_kain = input_jumlah_kain()
    jenis_kain = input_nama_kain(jumlah_kain)
    jumlah_tahun = int(input("\nMasukkan jumlah tahun: "))

    kuantitas_kain = input_kuantitas_kain(jenis_kain, jumlah_tahun)

    return jenis_kain, jumlah_tahun, kuantitas_kain

# Input data dari pengguna
jenis_kain, jumlah_tahun, kuantitas_kain = input_data()

# Menggunakan fungsi untuk menghitung total kuantitas seluruh kain pada setiap tahun
total_kuantitas_per_tahun = hitung_total_kuantitas(kuantitas_kain)

# Menampilkan total kuantitas seluruh kain pada setiap tahun
print("\nTotal Kuantitas Seluruh Kain per Tahun:")
for tahun, total_kuantitas in total_kuantitas_per_tahun.items():
    print(f"Tahun {tahun}: {total_kuantitas}")

# Menggunakan fungsi untuk menghitung perbandingan total kuantitas seluruh kain antara tahun 1 dan tahun 2
perbandingan_kuantitas = perbandingan_total_kuantitas(total_kuantitas_per_tahun)
print(f"\nPerbandingan Total Kuantitas Kain Tahun 1 dengan Tahun 2: {perbandingan_kuantitas}%")
