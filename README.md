# 📞 Python Kisi Rehberi (Console Application)

Bu proje, Python programlama dili kullanılarak geliştirilmiş, komut satırı (terminal) tabanlı basit bir kişi rehberi uygulamasıdır. Uygulama, kişilerin birden fazla iletişim bilgisini yönetebilir ve tüm verileri kalıcı olarak saklar.

## ✨ Temel Özellikler

* **Kalıcı Kayıt:** Tüm rehber verileri **rehber_kaydi.txt** adlı düz metin dosyasına kaydedilir ve açılışta otomatik yüklenir.
* **Çoklu İletişim:** Her kişi için birden fazla telefon numarası ve e-posta adresi kaydedilebilir (girişler virgül ile ayrılır).
* **Tam CRUD Desteği:** Kişi Ekleme (Create), Görüntüleme (Read), Düzenleme (Update) ve Silme (Delete) işlemleri.
* **Hata Yönetimi:** Geçersiz menü seçimleri ve boş alan girişlerine karşı temel koruma içerir.
* **Veri Bütünlüğü:** Düzenleme (Edit) sırasında listeden gelen veri yapısını korur.

## 🚀 Nasıl Çalıştırılır?

### Ön Gereksinimler

Sisteminizde **Python 3.x** kurulu olmalıdır.

### Kurulum ve Çalıştırma

1.  Bu depoyu yerel bilgisayarınıza klonlayın veya indirin:
    ```bash
    git clone https://github.com/BerkOzbezen/Python-Kisi-Rehberi.git
    cd Python-Kisi-Rehberi
    ```
2.  Uygulama dosyanızın adını biliyorsanız (örneğin `rehber_uygulamasi.py`), terminalde aşağıdaki komutu çalıştırın:
    ```bash
    python rehber_uygulamasi.py 
    ```
    *(Not: Lütfen yukarıdaki `rehber_uygulamasi.py` kısmını, kendi Python dosyanızın adı neyse onunla değiştirin.)*

## 💡 Kullanım İpuçları

### Kişi Ekleme ve Düzenleme
Telefon veya e-posta girerken, birden fazla bilgi girmek için her öğeyi **virgül (`,`)** ile ayırarak tek bir dize olarak girin:

* **Örnek Telefon Girişi:** `5551112233, 5320001122, 5449998877`
* **Düzenleme:** Düzenleme sırasında bir alanı değiştirmek istemiyorsanız, boş bırakıp `Enter` tuşuna basmanız yeterlidir; eski veriler korunacaktır.

### Çıkış Yapma
Verilerinizin kalıcı olarak kaydedilmesi için mutlaka **6. Kisi defterinden cik** menü seçeneğini kullanınız.

---

## 💻 Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Yapılar:** Sözlükler, Listeler, Fonksiyonlar, Dosya İşlemleri (`os`).
* **Kalıcılık Yöntemi:** Düz Metin Serileştirme (`.txt`).