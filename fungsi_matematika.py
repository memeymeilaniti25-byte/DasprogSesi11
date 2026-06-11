def tambah(a, b):
    return a + b

def pangkat(a, b):
    return a ** b

def kali(a, b):
    return a * b

# --- Konversi Panjang ---
def cm_ke_m(cm):
    return cm / 100

def m_ke_cm(m):
    return m * 100

# --- Ubah Bilangan (Basis) ---
def desimal_ke_biner(desimal):
    # bin() menghasilkan string '0b...', diambil dari indeks 2 dst.
    return bin(desimal)[2:]

def desimal_ke_oktal(desimal):
    # oct() menghasilkan string '0o...', diambil dari indeks 2 dst.
    return oct(desimal)[2:]

def desimal_ke_hexadesimal(desimal):
    # hex() menghasilkan string '0x...', diambil dari indeks 2 dst, dijadikan huruf kapital.
    return hex(desimal)[2:].upper()