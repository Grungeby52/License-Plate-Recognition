# License-Plate-Recognition
Bu proje araç plakaları üzerindeki karakterleri sırası ile okumak için Darknet projesi kullanılarak yapılmıştır.

## Gereksinimler
Uygulamayı kolayca çalıştırmak için Keras çerçevesini TensorFlow arka uç ile yüklemiş olmanız gerekir. Darknet çerçevesi "darknet" klasöründe bağımsızdır ve testleri çalıştırmadan önce derlenmelidir. Darknet oluşturmak için "darknet" klasörüne "make" yazmanız yeterlidir:
```shellscript
$ cd darknet && make
```
**Uygulama Ubuntu 18.04, Keras 2.2.3, TensorFlow 2.4.0, OpenCV 4.2.0, NumPy 1.19.5 ve Python 3.6.9 ile test edilmiştir**

## Önceden Eğitilmiş Modeli İndir
Terminalden "get-networks.sh" script dosyasını çalıştırın.
```shellscript
$ bash get-networks.sh
```
## Kurulum
Plaka resmlerini "img" klasörünün içine kopyalayın ve ardından "toGrayResize.py" doyasını çalıştırın.
Not: Öncesinde path uzantılarını değiştirmeniz gerekebilir.
```shellscript
$ python3 toGrayResize.py
```

## Kullanımı
Aşağıdaki kodu çalışrırmanız yeterli olacaktır. 
```shellscript
$ python3 license-plate-ocr.py img/
```
