username = input("Masukkan User anda :")
if len(username) < 12:
    print("Masukkan Minimal 12 karakter")
elif not username.upper():
    print("Username Huruf besar semua")
elif username.isdigit():
    print("Username Tidak Boleh angka")
elif not username.capitalize():
    print("Username harus huruf besar semua")
else:
    print("Username anda berhasil dibuat")
