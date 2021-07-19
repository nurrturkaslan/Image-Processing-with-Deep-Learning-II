"""
<Evrişimsel Sinir Ağları>
Convolutional Neural Network (ConvNet yada CNN)

Evrişimsel Sinir Ağları Nedir?
.. Evrişimsel sinir ağları, görüntü üzerinde 
sınıflandırma, nesne tespiti ve takibi problemlerini
çözmek için özelleştirilmiş ağlardır.
"""
import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread("cnn.PNG")
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal Img")

"""
Örneğin:
     Yukarıdaki görselle birlikte yazdıklarımı anlamaya çalışalım:
    Şimdi biz bu bölümde sınıflandırmaya odaklanacağımız için
    girdiden başlayarak çıktıya kadar olan süreci anlatabiliriz
    
    Yukarıda görselde görünen yapı CNN yapısı
    Girdiden başlayan (evrişim kısmından) sonuna gidiyoruz buna cnn yapısı diyoruz.
    Bu yapı fix değil
    Değişebilir(katman sayıları ile oynama yapabiliriz)
     peki burada bize ne anlatılıyor:
         Bir tane resmimiz var 28x28 pikselden oluşuyor
         
         Şimdi biz bu resmi sınıflandırabilmek için 
         yani bunun hangi rakam olduğunu anlayabilmek için
         bu resimle ilgili belli başlı özellikleri, featureları çıkartmamız yani extract etmemiz gerekiyor
         yani feature extraction işlemi gerçekleştirmemiz gerekiyor.
         
         Sonrasında ise bu resime dair çıkardığımız özellikleri kullanarak
         sınıflandırma işlemini yapmamız gerekiyor.
         
         Evrişimden başlayarak resimdeki tam bağlantıya kadar olan kısım "Bizim Öznitelik Çıkarımı" yaptığımız kısım
         yani;
         bu resimin niteliklerini özelliklerini çıkarttık.
         
         Bu özellikleri elde ettikten sonra "seyreltme kısmı"(Düzleştirme dahil) ile geri kalan "Tam Bağlantı
         bu bir "artificial neural network" tür. yani yapay sinir ağıdır.
         Bu bölümde ise "öznitelikleri kullanarak" bir çıktı üretiyoruz.
         Buda bizim sınıflandırma yaptığımız yer.
         
         öğrendik ki CNN in iki işlevi var
         öznitelik çıkarımı ve sınıflandırma
         
         peki öznitelikleri nasıl çıkarıyoruz?
         Öznitelik denilen şeyler resmi ifade etmek için kullandığımız özellikler
         Ama biz görüntü işlemede biliyoruz ki bizim öznitelik
         dediğimiz kısımlar (kenar, köşe, kenar ve köşenin birleşmesi ile başka bir şey, iki düz bir yan çizgi olabilir)
         bu kavramlara öznitelik diyoruz
         
         burada bulunan evrişim katmanı resim üzerinden öznitelik çıkarıyor.
         Ve özellik haritalarını oluşturuyor
         
         
         Öznitelikleri çıkarırken featureların boyutu azalıyor.
         Bizde bu boyutu arttırmak için piksel ekleme yapıyoruz.
         sonra bir tane daha evrişim katmanı ekliyoruz 2 evrişim katmanımız oldu.
         
         peki ilkinde öznitelik çıkardıysan 2.evrişim katmanında ne çıkarıyoruz
         2.evrişim katmanı high level olarak adlandırılıyor.
         en baştaki ise low level olarak adlandırılır
         
         Alçak seviyede bulunan katmanlar resimlerle ilgili
         sadece temel feature çıkarır(kenar, kçşe, düz çizgi, yan çizgi)
         
         Yüksek seviye katmanlar ise resimler ile ilgili ayırt edici özellikler çıkarır
         
         örneğin görseldeki (5) te gördüğümüz ters c kısımı bizim için ayırt edicidir
         yani bu high level katmanlarda ortaya çıkar
         yani derinliği ve anlamı artmış olur bizim için görselin
         
       
         sonuç:
           sınıflandırma sonucunda 0 ile 1 arasında değişen sayı çıkıyor
           örneğin farklı sınıfa aitse 10 tane sayı çıkıyor
           bu 10 sayının toplamlarının 1 olması gerekiyor
           
           bu bize neyi ifade ediyor:
               rakamlarımız 10 tane 0 dan 9 dahil 10 tane
               her bir rakam için benim girdim doğrultusunda bir olasılık değeri çıkıyor
               örneğin 5 için %80 diğerleri arasında %20 paylaştırılıyor olarak düşünebilirz
               sonra %80 yükselmiş diyoruz
               ve %80 e karşılık gelen değerin görüntüm 5 rakamını ifade ediyor diyebiliriz
 """   










"""
<Evrişim Operasyonu Nedir ? >

Özellik algılayıcı, kenarlar veya dışbükey şekiller hibi özellikleri algılar.
Örneğin; görüntümüz bir köpek ise, özellik algılayıcı
köpeğin kulağı veya kuyruğu gibi özellikleri algılayabilir

özellik haritası = EVRİŞİM. Matrislerin elemanlarının çarpımı

Görüntü üzerinde gezinme gerçekleşir

Bu işlemler sonucunda orjinal görüntünün boyutu azalmıs oluyor.
Bu modelimizin hızlı çalışması açısından önemli

Birden çok özellik haritası oluşturuyoruz, çünkü birden çok özellik algılayıcı
(filtre kullanıyoruz.) örneğin kenarı tespit etmek için filtre
bu filtreler cnn de öğrenilen şeyler
yani resmimi sınıflandırmak için network tarafından öğrenilen şeyler
en iyi filtre network kullanılarak belirlenmiş oluyor
filtre kullanarakta bir özellik haritası ortaya çıkarmış oluyoruz.
 
"""

"""
Aktivasyon Fonksiyonu:
    Evrişim katmanından sonra aktivasyon fonksiyonu olarak ReLU kullanıyoruz.
    Bu aktivasyon fonksiyonu doğrusallığı kırarak, modelimizin doğrusal olamayan
    yapılarını öğrenmesine olanak tanır.
    Yani modelimizin doğrusallığını azaltıyor
    model dediğimiz şey cnn (non-linear) doğrusal olmamasını arttırıyor
    
    
    ReLU türevi çok kolay alınabilen bir aktivasyon fonksiyonu
    
    Öğrenme işlemini türev alama ile gerçekleştiriyoruz
    Türev dediğimiz şey değişim zaten
    değişimi bularak kendi parametrelerimizi güncelliyoruz
    taki nereye kadar değişim sıfır çıkana kadar.
    
    Modelimize herhangi bir yük katmadığı için ReLU yu kullanıyoruz.
          
"""








"""
Piksel Ekleme:
    Üstte yapımızın boyutu inputtan farklıydı.
    bunu arttırmmaız gerikiyor
    çünkü neden resime dair bilgi kaybediyoruz.
    
    Evrişim katmanlarını uygulamaya devam ettikçe, resmin boyutu
    istediğimizden daha hızlı azalacaktır.
    Ağımızın ilk katmanlarında, düşük seviyeli özellikleri çıkarabilmemiz için orijinal giriş boyutu hakkında 
    olabildiğince fazla bilgiyi korumak istiyoruz.
    Bu yüzden piksel eklemesi yapıyoruz.
    
"""




"""
Ortaklama:
    Aşağı örnekleme veya alt örnekleme yapar.(Parametre sayısını azaltır)
    Ölçek veya yön değişikliklerine göre değişmeyen özelliklerin algılanmasını sağlar
    Ağdaki parametre ve hesaplama miktarlarını azaltır ve
    dolayısıyla ezberlemeyi(overfitting) da kontrol eder.
    Tamam burada bilgi kaybetmiyoruz ama veriyide ezberlemek istemiyoruz
    
"""






"""
Düzleştirme:
    cnn in featurelarını yine cnn in sınıflandırıcısına sokabilmek için düzleştiriyoruz
    iki boyutlu veriyi vektör haline getirir.
"""




"""
Tam Bağlantı:
    
    Bir katmandaki nöronların önceki katmandaki tüm aktivasyonlarla
    bağlantıları vardırç Örneğin yapay sinir ağları
    
    Sınıflandırma işlemi gerçekleştirir.
    
    
    (Düzleştirmede elde ettiğimiz vektör burada girdi katmanımız oluyoor)
    Burada istediğimiz kadar gizli katman kullanabilirz
    gizli katman sayısı arttıkça bizim modelimizin derinliği artar
    (karmaşık yapıyı algılama ve sınıflandırma) derinlik artmasında yarar
    
  
"""



"""
Dropout(seyreltme):
    rastgele seçilen nöronların eğitim sırasında göz ardı edildiği bir tekniktir.
    Ezberlemeyi Overfitting i önler.
    feature extraction ve sınıflandırma kısmında kullanılabilir.
    
"""





"""
Veri arttırma:
    Ezberleme sorununu önlemek için, el yazısı rakam veri setimizi
    yapay olarak genişletmemiz gerekyor.
    
    Rakam varyasyonlarını yeniden oluşturmak için eğitim verilerini küçük dönüşümlerle değiştirebilirz.
    
    Örneğin sayı ortalanmıştır ölçek aynı değildir
    (bazıları büyük/ küçük sayılarla yazanlar) veya görüntü döndürülür
"""





"""
Trex Projesi

Gerçek zamanlı rakam sınıflandırma projesi
"""




