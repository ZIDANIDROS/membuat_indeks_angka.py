import numpy as np

# Input data dari pengguna
barang = input("Masukkan daftar barang (pisahkan dengan koma): ").split(', ')
Ho = np.array([float(x) for x in input("Masukkan harga pada periode dasar (Ho), pisahkan dengan spasi: ").split()])
Ht = np.array([float(x) for x in input("Masukkan harga pada periode tertentu (Ht), pisahkan dengan spasi: ").split()])
Ko = np.array([float(x) for x in input("Masukkan kuantitas pada periode dasar (Ko), pisahkan dengan spasi: ").split()])
Kt = np.array([float(x) for x in input("Masukkan kuantitas pada periode tertentu (Kt), pisahkan dengan spasi: ").split()])

# Bobot (gunakan harga pada periode dasar sebagai bobot)
w = Ho

# a. Angka Indeks Harga Agregat Tertimbang (Laspeyres)
IL = round((np.sum(Ho * Kt) / np.sum(Ho * Ko)) * 100)
IL_change = round(((IL - 100) / 100) * 100)
IL_trend = "Kenaikan" if IL_change > 0 else "Penurunan" if IL_change < 0 else "stabil"

# b. Angka Indeks Harga Agregat Tertimbang (Paasche)
IP = round((np.sum(Ht * Kt) / np.sum(Ht * Ko)) * 100)
IP_change = round(((IP - 100) / 100) * 100)
IP_trend = "Kenaikan" if IP_change > 0 else "Penurunan" if IP_change < 0 else "stabil"

# c. Angka Indeks Harga Agregat Tertimbang (Fisher)
IF = round(np.sqrt(IL * IP))
IF_change = round(((IF - 100) / 100) * 100)
IF_trend = "Kenaikan" if IF_change > 0 else "Penurunan" if IF_change < 0 else "stabil"

# d. Angka Indeks Harga Agregat Tertimbang (Drobisch)
ID = round(2 * (IL * IP) / (IL + IP))
ID_change = round(((ID - 100) / 100) * 100)
ID_trend = "Kenaikan" if ID_change > 0 else "Penurunan" if ID_change < 0 else "stabil"

# e. Angka Indeks Harga Agregat Tertimbang (Marshall)
IM = round((np.sum(Ht * Kt) / np.sum(w * Ko)) * 100)
IM_change = round(((IM - 100) / 100) * 100)
IM_trend = "Kenaikan" if IM_change > 0 else "Penurunan" if IM_change < 0 else "stabil"

# f. Angka Indeks Harga Agregat Tertimbang (Wals)
IW = round((np.sum(w * Kt) / np.sum(w * Ko)) * 100)
IW_change = round(((IW - 100) / 100) * 100)
IW_trend = "Kenaikan" if IW_change > 0 else "Penurunan" if IW_change < 0 else "stabil"

# Menampilkan hasil
print("1. Angka Indeks Harga Agregat Tertimbang (Laspeyres):")
print(f"   Indeks Terjadi {IL_trend} sebesar {IL_change}%.")
print("\n2. Angka Indeks Harga Agregat Tertimbang (Paasche):")
print(f"   Indeks Terjadi {IP_trend} sebesar {IP_change}%.")
print("\n3. Angka Indeks Harga Agregat Tertimbang (Fisher):")
print(f"   Indeks Terjadi {IF_trend} sebesar {IF_change}%.")
print("\n4. Angka Indeks Harga Agregat Tertimbang (Drobisch):")
print(f"   Indeks Terjadi {ID_trend} sebesar {ID_change}%.")
print("\n5. Angka Indeks Harga Agregat Tertimbang (Marshall):")
print(f"   Indeks Terjadi {IM_trend} sebesar {IM_change}%.")
print("\n6. Angka Indeks Harga Agregat Tertimbang (Wals):")
print(f"   Indeks Terjadi {IW_trend} sebesar {IW_change}%.")
