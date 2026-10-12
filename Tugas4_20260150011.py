# =====================================================================
# BAGIAN 1: SISTEM KEAMANAN LOGIN (Menggunakan while)
# =====================================================================
password_benar = "AI2026"
percobaan = 0
maks_percobaan = 3
akses_diterima = False

print("=== SISTEM KEAMANAN PORTAL AI ===")

# Loop akan berjalan selama belum 3 kali mencoba dan belum sukses login
while (percobaan < maks_percobaan) and (akses_diterima == False):
    input_password = input("Masukkan kata sandi rahasia: ")
    percobaan = percobaan + 1  # Bagian ini sudah dibetulkan
    
    if input_password == password_benar:
        akses_diterima = True
    else:
        sisa = maks_percobaan - percobaan
        if sisa > 0:
            print(f"Kata sandi salah ! Sisa percobaan : {sisa}\n")
        else:
            print("Kata sandi salah!")

# =====================================================================
# VALIDASI: MEMISAHKAN BLOK LOGIN DENGAN BLOK SUHU SERVER
# =====================================================================
if akses_diterima == True:
    print("Akses Diberikan!\n")
    
    # -----------------------------------------------------------------
    # BAGIAN 2: ANALISIS SUHU SERVER (Hanya jalan jika login berhasil)
    # -----------------------------------------------------------------
    print("=== ANALISIS SUHU SERVER HARIAN ===")
    
    total_suhu = 0.0
    suhu_tertinggi = None  # Diubah jadi None agar tidak menghasilkan bug '-inf'
    jumlah_hari = 5
    
    for hari in range(1, jumlah_hari + 1):
        suhu = float(input(f"Masukkan suhu server untuk Hari ke-{hari} (°C): "))
        total_suhu = total_suhu + suhu
        
        # Logika pembetulan untuk membandingkan nilai suhu terbesar
        if suhu_tertinggi is None or suhu > suhu_tertinggi:
            suhu_tertinggi = suhu
            
    rata_rata_suhu = total_suhu / jumlah_hari
    
    # Menampilkan rekapitulasi analisis yang benar dan akurat
    print("\n=== REKAPITULASI ANALISIS SUHU ===")
    print(f"Total suhu     : {total_suhu:.2f} °C")
    print(f"Rata-rata suhu : {rata_rata_suhu:.2f}°C")
    print(f"Suhu Tertinggi : {suhu_tertinggi:.2f}°C")

else:
    # Jika gagal 3 kali, program langsung stop di sini tanpa minta input suhu
    print("Sistem Terkunci!")
