import fungsi_matematika

def menu_aritmatika():
    while True:
        print("\n--- Sub-Menu Aritmatika ---")
        print("1. Penjumlahan")
        print("2. Perpangkatan")
        print("3. Perkalian")
        print("4. Kembali ke Menu Utama")
        
        pilihan = input("Pilih operasi (1-4): ")
        if pilihan == '4':
            break
        
        if pilihan in ['1', '2', '3']:
            try:
                x = float(input("Masukkan bilangan pertama: "))
                y = float(input("Masukkan bilangan kedua: "))
                
                if pilihan == '1':
                    print(f"Hasil: {x} + {y} = {fungsi_matematika.tambah(x, y)}")
                elif pilihan == '2':
                    print(f"Hasil: {x} ^ {y} = {fungsi_matematika.pangkat(x, y)}")
                elif pilihan == '3':
                    print(f"Hasil: {x} * {y} = {fungsi_matematika.kali(x, y)}")
            except ValueError:
                print("Input harus berupa angka!")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def menu_konversi():
    while True:
        print("\n--- Sub-Menu Konversi ---")
        print("1. CM to M")
        print("2. M to CM")
        print("3. Kembali ke Menu Utama")
        
        pilihan = input("Pilih konversi (1-3): ")
        if pilihan == '3':
            break
            
        if pilihan in ['1', '2']:
            try:
                nilai = float(input("Masukkan nilai: "))
                if pilihan == '1':
                    print(f"Hasil: {nilai} CM = {fungsi_matematika.cm_ke_m(nilai)} M")
                elif pilihan == '2':
                    print(f"Hasil: {nilai} M = {fungsi_matematika.m_ke_cm(nilai)} CM")
            except ValueError:
                print("Input harus berupa angka!")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def menu_ubah_bilangan():
    while True:
        print("\n--- Sub-Menu Ubah Bilangan ---")
        print("1. Desimal to Biner")
        print("2. Desimal to Oktal")
        print("3. Desimal to Hexadesimal")
        print("4. Kembali ke Menu Utama")
        
        pilihan = input("Pilih pengubahan (1-4): ")
        if pilihan == '4':
            break
            
        if pilihan in ['1', '2', '3']:
            try:
                nilai = int(input("Masukkan bilangan desimal: "))
                if pilihan == '1':
                    print(f"Biner dari {nilai} adalah: {fungsi_matematika.desimal_ke_biner(nilai)}")
                elif pilihan == '2':
                    print(f"Oktal dari {nilai} adalah: {fungsi_matematika.desimal_ke_oktal(nilai)}")
                elif pilihan == '3':
                    print(f"Hexadesimal dari {nilai} adalah: {fungsi_matematika.desimal_ke_hexadesimal(nilai)}")
            except ValueError:
                print("Input harus berupa bilangan bulat (integer)!")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def main():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Aritmatika")
        print("2. Konversi")
        print("3. Ubah Bilangan")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            menu_aritmatika()
        elif pilihan == '2':
            menu_konversi()
        elif pilihan == '3':
            menu_ubah_bilangan()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid, silakan masukkan angka 1-4.")

if __name__ == "__main__":
    main()