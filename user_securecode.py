from mail_sender import send_verification

user_email = input("Email gir: ")

dogrulama_kodu = send_verification(user_email)

print("Kod gönderildi!")

giris = input("Kodu gir: ")

if giris == dogrulama_kodu:
    print("✔ Doğrulandı!")
else:
    print("❌ Hatalı kod")