


1. **Veri Yükleme ve Hazırlama**:
    - `pandas` kütüphanesi kullanılarak `karar_agaci_veri_100.xlsx` dosyasından veriler yükleniyor.
    - Veri çerçevesi (DataFrame) oluşturuluyor ve veriler işleniyor.
    - `X` değişkeni (özellikler) olarak "Yaş", "Kan Basıncı" ve "Kolesterol" sütunları seçiliyor.
    - `y` değişkeni (hedef) olarak "Hastalık" sütunu seçiliyor. Bu, sınıflandırma yapmak istediğimiz veriyi temsil ediyor.

2. **Model Oluşturma ve Eğitim**:
    - Bir **Decision Tree Classifier** (Karar Ağacı Sınıflandırıcısı) kullanılıyor.
    - Modelin parametreleri şu şekilde ayarlanıyor: `max_depth=1`, `min_samples_split=2`, `min_samples_leaf=2`. Bu parametreler modelin karmaşıklığını kontrol eder.
    - Model, tüm veri kümesi üzerinde eğitiliyor (fit).

3. **Kullanıcıdan Veri Alma ve Tahmin**:
    - Kullanıcıdan yaş, kan basıncı ve kolesterol bilgileri girilmesi isteniyor.
    - Bu veriler, modele uygun formatta (`pandas DataFrame`) dönüştürülüyor.
    - `predict()` metodu kullanılarak, model bu veriler üzerinde tahmin yapıyor.
    - Tahmin sonucuna göre hastalığın olup olmadığı kullanıcıya bildiriliyor.

### Geliştirilmesi Gereken Kısımlar:
- Modelin daha iyi değerlendirilmesi için veri setinin eğitim ve test olarak ayrılması ve ardından doğrulama yapılması gerekiyor. Ancak bu kısım şu an için yoruma alınmış durumda.
- Ayrıca, `cross_val_score` kullanılarak çapraz doğrulama yapılması önerilmiş. Bu, modelin performansını daha iyi ölçmek için kullanılabilir.

---

### README Dosyası:

---

# Hastalık Tahmin Modeli (Decision Tree Classifier)

Bu Python uygulaması, karar ağacı sınıflandırıcısı kullanarak kişinin yaş, kan basıncı ve kolesterol seviyelerine dayalı olarak hastalık durumu tahmini yapmaktadır.

## Gerekli Kütüphaneler

Uygulamayı çalıştırmadan önce aşağıdaki Python kütüphanelerinin yüklü olduğundan emin olun:

- `pandas`
- `matplotlib`
- `scikit-learn`
- `openpyxl`

Bu kütüphaneleri yüklemek için:

```bash
pip install pandas matplotlib scikit-learn openpyxl
```

## Uygulama Adımları

1. **Veri Yükleme**:
   - `karar_agaci_veri_100.xlsx` dosyasındaki veriler yüklenir.
   - Bu veri dosyası yaş, kan basıncı, kolesterol ve hastalık durumunu içermektedir.
   
2. **Karar Ağacı Modeli**:
   - Verilerden "Yaş", "Kan Basıncı" ve "Kolesterol" sütunları, bağımsız değişken (özellik) olarak kullanılır.
   - "Hastalık" sütunu ise bağımlı değişken (hedef) olarak seçilir.
   - **Karar Ağacı Sınıflandırıcısı** kullanılarak model eğitilir.

3. **Kullanıcı Girdisi ile Tahmin**:
   - Kullanıcıdan yaş, kan basıncı ve kolesterol bilgileri alınır.
   - Bu bilgiler modele uygun formatta dönüştürülür.
   - Model bu veriler üzerinde tahmin yapar ve hastalık durumunu kullanıcıya bildirir.

## Uygulama Nasıl Çalışır?

1. Python dosyasını çalıştırın.
2. Program, sizden sırayla yaş, kan basıncı ve kolesterol seviyenizi girmenizi isteyecektir.
3. Girdiğiniz bilgilere dayanarak model, hastalık olup olmadığını tahmin edecektir.
4. Sonuç, konsolda görüntülenir:
   - "Hastalığınız Var!" veya "Hastalığınız Yok!"

## Örnek Kullanım

```bash
Lütfen tahmin için aşağıdaki bilgileri giriniz:
Yaşınızı giriniz: 35
Kan basıncınızı giriniz: 130
Kolesterol seviyenizi giriniz: 210

Tahmin: Hastalığınız Var!
```

## Geliştirme Notları

- Model, daha iyi sonuçlar almak için eğitim ve test veri setlerine ayrılmalı.
- `cross_val_score` ile modelin çapraz doğrulama skoru hesaplanabilir.
  
---

