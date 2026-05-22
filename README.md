# Python SMTP E-posta Doğrulama Sistemi

Python ile geliştirilmiş, SMTP protokolü üzerinden kullanıcılara güvenli tek kullanımlık şifre (OTP) göndererek kimlik doğrulama yapan bir prototip sistem.

---

## Özellikler

- Gmail SMTP üzerinden 6 haneli OTP kodu gönderimi
- Kullanıcı e-posta adresi girişi ile anlık doğrulama
- Basit ve anlaşılır iki dosyalı modüler yapı
- Standart Python kütüphaneleri ile çalışır (harici bağımlılık yok)

---

## Proje Yapısı

```
python-smtp-email-verification-system/
├── mail_sender.py       # OTP üretimi ve e-posta gönderimi
└── user_securecode.py   # Kullanıcı arayüzü ve doğrulama kontrolü
```

### `mail_sender.py`
6 haneli rastgele bir OTP kodu üretir, Gmail SMTP sunucusu üzerinden belirtilen e-posta adresine gönderir ve kodu döndürür.

### `user_securecode.py`
Kullanıcıdan e-posta adresini alır, doğrulama kodunun gönderilmesini tetikler, ardından kullanıcının girdiği kodu sistemin ürettiği kodla karşılaştırır.

---

## ⚙️ Kurulum ve Kullanım

### Gereksinimler

- Python 3.x
- Gmail hesabı
- Gmail için **Uygulama Şifresi** (App Password)

### Adımlar

**1. Repoyu klonlayın:**

```bash
git clone https://github.com/TurkerAlbayrak/python-smtp-email-verification-system.git
cd python-smtp-email-verification-system
```

**2. `mail_sender.py` dosyasındaki kimlik bilgilerini güncelleyin:**

```python
EMAIL = "sizin_gmail_adresiniz@gmail.com"
PASSWORD = "gmail_uygulama_sifreniz"
```

> Normal Gmail şifrenizi **kullanmayın**. Aşağıdaki talimatları izleyerek bir Uygulama Şifresi oluşturun.

**3. Uygulamayı çalıştırın:**

```bash
python user_securecode.py
```

**4. İstendiğinde e-posta adresinizi girin; gelen kodu terminale yazın:**

```
Email gir: ornek@gmail.com
Kod gönderildi!
Kodu gir: 483921
✔ Doğrulandı!
```

---

## Gmail Uygulama Şifresi Oluşturma

Gmail'in standart şifresi bu projede çalışmaz. Bunun yerine bir **Uygulama Şifresi** (App Password) oluşturmanız gerekir:

1. [Google Hesabım](https://myaccount.google.com/) sayfasına gidin.
2. **Güvenlik** sekmesini açın.
3. **2 Adımlı Doğrulama**'yı etkinleştirin (zorunlu).
4. Arama kutusuna **"Uygulama şifreleri"** yazın ve açın.
5. Yeni bir uygulama şifresi oluşturun ve `mail_sender.py` içindeki `PASSWORD` alanına yapıştırın.

---

## Güvenlik Notları

- Kimlik bilgilerinizi (`EMAIL`, `PASSWORD`) doğrudan kaynak kodda bırakmayın.
- Ortam değişkenleri veya `.env` dosyası kullanmanız önerilir:

```python
import os
EMAIL = os.environ.get("SENDER_EMAIL")
PASSWORD = os.environ.get("SENDER_PASSWORD")
```

- `.env` dosyasını `.gitignore`'a eklemeyi unutmayın.
- Bu proje bir **prototip/eğitim amaçlı** çalışmadır; production ortamında kullanmadan önce güvenlik iyileştirmeleri yapılmalıdır.

---

## Geliştirme Fikirleri

- [ ] OTP için süre sınırı (TTL) ekleme
- [ ] Birden fazla deneme hakkı ve kilitleme mekanizması
- [ ] Flask/FastAPI ile REST API entegrasyonu
- [ ] HTML e-posta şablonu desteği
- [ ] Farklı SMTP sağlayıcıları için destek (Outlook, Yahoo, vb.)

---

---

## Geliştirici

**Türker Albayrak**
[GitHub](https://github.com/TurkerAlbayrak)
