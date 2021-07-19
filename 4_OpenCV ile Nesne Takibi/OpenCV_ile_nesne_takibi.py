"""
OpenCV ile Nesne Takibi:
    Nesne algılamada, resimdeki bir nesneyi algılar, etrafına
    bir sınırlayıcı kutu koyar ve nesneyi sınıflandırırız.
    
    Nesne izleme, bir dizi video karesi boyunca hareket eden nesneleri
    izlemeyi amaçlayan, bilgisayar görüşü içindeki bir disiplindir.
    
    Nesneler insanlar, hayvanlar, araçlar ve futbol maçındaki
    top gibi diğer ilgi çekici nesnelerde olabilir.
    
    Nesne izleme, gözetim, tıbbi görüntüleme, trafik akışı analizi
    insansız araçlar, insan sayma ve izleyici akış analizi
    ve insan-bilgisayar etkileşimi gibi birçok pratik uygulamaya sahiptir.
    
    
"""
"""
Teknik olarak nesne izleme, bir görüntüdeki nesneleri tanımlama ve bunlara
sınırlayıcı kutular atama olan nesne algılamayla başlar.

Nesne izleme algoritması, görüntüde tanımlanan 
her nesneye bir kimlik atar ve sonraki çerçevelerde
bu kimliği geçmeye ve aynı nesnenin yeni konumunu belirlemeye çalışır
"""
"""
Nesne takibinin belli başlı zorlukları:
    Yeniden tanımlama-bir çerçevedeki bir nesneyi sonraki çerçevelerde
    aynı nesneye bağlama/ilişkilendirme
    
    Görünme ve kaybolma-nesneler karenin içine veya dışına
    tahmin edilemeyecek şekilde hareket edebilir
    ve bunları daha aynı ortamda görünen diğer nesnelere bağlamamız gerekir.
    
    Tıkanma/Bloklama- diğer nesnenin önlerinde göründüğünden ve onları örttüğünden
    bazı çerçevelerde nesneler kısmen ve tamamen tıkanmıştır.
    
    Kimlik Anahtarları-iki nesne birbirleriyle kesiştiğinde hangisinin
    hangisi olduğunu anlamamız gerekir
    
    Hareket Bulanıklığı-nesneler farklı bakış açılarından çok farklı görülebilir
    ve aynı nesneyi tüm perspektiflerden tutarlı bir şekilde tanımlamamız gerekir
    
    Değişimi Ölçekle- bir videodaki nesnelerin ölçeği önemli ölçüde değişebilir
    örneğin kamera yakınlaştırması nedeniyle
    
    Aydınlatma- VİDEODAKİ IŞIK DEĞİŞİKLİKLERİ NESNELERİN NASIL GÖRÜNDÜĞÜ ÜZERİNE BÜYÜK BİR
    ETKİYE SAHİP VE ONLARI TUTARLI BİR ŞEKİLDE
    ALGILAMAYI ZORLAŞTIRABİLİR
"""
"""
Peki Nesne Takibi ile Neler yapacağız ? 

Ortalama Kayma Algoritması

Takip Algoritmaları

Çoklu Nesne Takibi
"""