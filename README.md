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
**Not: Öncesinde path uzantılarını değiştirmeniz gerekebilir**
```shellscript
$ python3 toGrayResize.py
```

## Kullanımı
Aşağıdaki kodu çalıştırmanız yeterli olacaktır. 
```shellscript
$ python3 license-plate-ocr.py img/
```
## Test Sonuçları
**20 Adet Plaka resmi ile elde edilen sonuçlar 15 doğru 5 hatalı tarama ile sonuçlanmıştır.**
```
layer     filters    size              input                output
    0 conv     32  3 x 3 / 1   240 x  80 x   3   ->   240 x  80 x  32  0.033 BFLOPs
    1 max          2 x 2 / 2   240 x  80 x  32   ->   120 x  40 x  32
    2 conv     64  3 x 3 / 1   120 x  40 x  32   ->   120 x  40 x  64  0.177 BFLOPs
    3 max          2 x 2 / 2   120 x  40 x  64   ->    60 x  20 x  64
    4 conv    128  3 x 3 / 1    60 x  20 x  64   ->    60 x  20 x 128  0.177 BFLOPs
    5 conv     64  1 x 1 / 1    60 x  20 x 128   ->    60 x  20 x  64  0.020 BFLOPs
    6 conv    128  3 x 3 / 1    60 x  20 x  64   ->    60 x  20 x 128  0.177 BFLOPs
    7 max          2 x 2 / 2    60 x  20 x 128   ->    30 x  10 x 128
    8 conv    256  3 x 3 / 1    30 x  10 x 128   ->    30 x  10 x 256  0.177 BFLOPs
    9 conv    128  1 x 1 / 1    30 x  10 x 256   ->    30 x  10 x 128  0.020 BFLOPs
   10 conv    256  3 x 3 / 1    30 x  10 x 128   ->    30 x  10 x 256  0.177 BFLOPs
   11 conv    512  3 x 3 / 1    30 x  10 x 256   ->    30 x  10 x 512  0.708 BFLOPs
   12 conv    256  3 x 3 / 1    30 x  10 x 512   ->    30 x  10 x 256  0.708 BFLOPs
   13 conv    512  3 x 3 / 1    30 x  10 x 256   ->    30 x  10 x 512  0.708 BFLOPs
   14 conv     80  1 x 1 / 1    30 x  10 x 512   ->    30 x  10 x  80  0.025 BFLOPs
   15 detection
mask_scale: Using default '1.000000'
Loading weights from data/ocr/ocr-net.weights...Done!
Performing OCR...
	Scanning img/0_0.jpg_lp.png
		**LP: 35GA4434**
	Scanning img/0x0-2.jpg_lp.png
		**LP: 34DUA34**
	Scanning img/440px-Turkey_licenceplate.jpg_lp.png
		**LP: 38VU055**
	Scanning img/44_ab_044_malatya_ozel_plaka_sat_l_k_8390135523727512913.jpg_lp.png
		**LP: 44AB044**
	Scanning img/5DYvgL.jpg_lp.png
		**LP: 34ZB3636**
	Scanning img/61BB2F3F8DE7424F88551964D7D0252F.jpg_lp.png
		**LP: 35AP7**
	Scanning img/app-plakalar-cesitleri-129120064433690-12.jpeg_lp.png
		**LP: 06K88**
	Scanning img/app-plakalar-cesitleri-129120064433690-1223.jpeg_lp.png
		**LP: 06AY6651**
	Scanning img/bos-plaka-bulma.jpg_lp.png
		**LP: 06GKN62**
	Scanning img/download223.jpg_lp.png
		**LP: 35AD7227**
	Scanning img/download33221.jpg_lp.png
		**LP: 42FNG29**
	Scanning img/images (2).jpg_lp.png
		**LP: 06LRN00**
	Scanning img/images (3).jpg_lp.png
		**LP: 09T449**
	Scanning img/images.jpg_lp.png
		**LP: 19AAB001**
	Scanning img/plaka-png-1.png_lp.png
		**LP: 06CNU56**
	Scanning img/tr-plaka-png-4.png_lp.png
		**LP: 34SG1957**
	Scanning img/turkije23.jpg_lp.png
		**LP: 7**
	Scanning img/turkije36.jpg_lp.png
		**LP: 3EZ6T**
	Scanning img/unnamed (1).jpg_lp.png
		**LP: 33BJJ09**
```
