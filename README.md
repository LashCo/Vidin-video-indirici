# Vidin v1.0

Vidin, Pytube kütüphanesi kullanılarak basit bir YouTube video indirme aracıdır. Kullanıcılar, bir YouTube videosunun URL'sini girerek videoları indirebilirler.

## Kullanım

1. Vidin'i kullanmak için bilgisayarınızda Python yüklü olmalıdır. Eğer yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/) indirebilir ve kurabilirsiniz.

2. Ardından Pytube kütüphanesini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın:

    ```
    pip install pytube
    ```

3. Şimdi Vidin'i çalıştırmak için aşağıdaki adımları izleyin:

    - Terminal veya komut istemcisinde Vidin'in bulunduğu dizine gidin.
    - `vidin.py` dosyasını bir metin düzenleyiciyle açın ve YouTube videosunun URL'sini `linkim_entry.get()` fonksiyonuna yapıştırın.
    - Ardından terminal veya komut istemcisinde `python vidin.py` komutunu çalıştırın.
    - "Lütfen indirmek istediğiniz videonun linkini giriniz" metin kutusuna YouTube videosunun URL'sini yapıştırın ve "İndir" düğmesine tıklayın.
    - Video başarıyla indirildiğinde, aynı dizine kaydedilecektir.
