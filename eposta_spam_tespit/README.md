# E-posta Spam Tespit Projesi

Bu proje, makine öğrenmesi kullanılarak e-postaların **spam** veya **normal (ham)** olarak sınıflandırılmasını amaçlamaktadır.

Projede, temizlenmiş bir spam e-posta veri seti kullanılarak temel bir sınıflandırma modeli eğitilmiş ve modelin doğruluk performansı değerlendirilmiştir. Amaç, metin verileri üzerinde makine öğrenmesi sürecini uçtan uca göstermektir.

## Kullanılan Veri Seti

Bu projede, spam ve normal (ham) e-postalardan oluşan, ön işleme adımlarından geçirilmiş bir CSV veri seti kullanılmıştır.

Veri seti içeriği özetle:
- E-posta metni
- E-postanın sınıf etiketi (spam / ham)

Toplamda **2000 adet e-posta** örneği bulunmaktadır ve veri seti model eğitimi ile test aşamalarında kullanılmıştır.

## Model ve Yöntem

E-posta metinleri, makine öğrenmesi algoritmalarının işleyebileceği sayısal bir forma dönüştürülmüştür. Bu amaçla metin verileri vektörleştirilmiş ve ardından bir sınıflandırma modeli kullanılarak eğitim gerçekleştirilmiştir.

Model eğitimi sürecinde:
- Veri seti eğitim ve test olarak ayrılmıştır
- Metinler sayısal özelliklere dönüştürülmüştür
- Sınıflandırma modeli eğitilmiş ve test verisi üzerinde değerlendirilmiştir

Model, bir e-postanın spam olup olmadığını ikili (binary) sınıflandırma yaklaşımıyla tahmin etmektedir.

## Sonuçlar ve Değerlendirme

Eğitilen model, test verisi üzerinde yüksek doğruluk ile çalışmıştır. Modelin performansı doğruluk (accuracy) metriği kullanılarak değerlendirilmiştir.

Elde edilen sonuçlar, temel metin vektörleştirme ve sınıflandırma yaklaşımının spam e-posta tespiti için etkili olduğunu göstermektedir. Bu proje, daha gelişmiş modeller ve özellik mühendisliği yöntemleri için bir temel niteliği taşımaktadır.
