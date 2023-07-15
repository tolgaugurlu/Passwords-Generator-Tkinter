# Password Generator & Evaluator (Şifre Oluşturucu & Değerlendirici)

Bu uygulama, kullanıcının belirttiği kriterlere göre rastgele bir şifre oluşturur ve bu şifrenin gücünü değerlendirir. Aleyna Kaya ile üzerinde farklı kriptografik işlemler yapmaya çalışacağımız projenin başlangıcıdır.

## Özellikler

- Kullanıcı şifrenin uzunluğunu belirleyebilir.
- Oluşturulan şifreler isteğe bağlı olarak küçük harf, büyük harf, rakam ve özel karakter içerebilir.
- Oluşturulan şifrelerin gücü değerlendirilir ve "Çok Zayıf", "Zayıf", "Orta", "Güçlü", "Çok Güçlü" şeklinde bir değerlendirme sonucu gösterilir.
- Oluşturulan şifreler bir SQLite veritabanında saklanır. Her şifre, hangi platform için oluşturulduğu bilgisi ile birlikte tutulur.

## Nasıl Çalışır?

1. Şifrenin hangi platform için oluşturulacağını belirtin.
2. Şifrenin uzunluğunu girin.
3. Şifrenin hangi karakterleri içereceğini belirtin (küçük harf, büyük harf, rakam, özel karakter).
4. "Şifre Oluştur" düğmesine tıklayın. Oluşturulan şifre ve gücü ekranınıza yansıyacaktır.

## Ekran Görüntüleri

![demo-img](https://github.com/tolgaugurlu/Passwords-Generator-Tkinter/assets/85436268/5f654113-048d-4143-be46-e1e60ac82a31)


## Kurulum

Bu uygulamanın çalışması için Python 3 ve SQLite gerekmektedir. Ayrıca 'requirements.txt' dosyasında belirtilen kütüphanelerin yüklenmesi gerekmektedir. Detaylar için lütfen 'INSTALLATION.md' dosyasına bakın.

## Katkıda Bulunma

Projeye katkıda bulunmak isterseniz, lütfen 'CONTRIBUTING.md' dosyasını inceleyin.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için 'LICENSE' dosyasına bakınız.
