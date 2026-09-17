
hasil_panen = [10, 15, 20, 12]

total = sum(hasil_panen)

def hitung_diskon(total):
    diskon = total * 0.10
    return total - diskon

total_setelah_diskon = hitung_diskon(total)

print("Hasil panen:", hasil_panen)
print("Total hasil panen:", total, "kg")
print("Total setelah diskon 10%:", total_setelah_diskon, "kg")
