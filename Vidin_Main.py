import tkinter as tk
from pytube import YouTube

def script_indirme():
    link = linkim_entry.get()
    yt = YouTube(link)
    pixels = yt.streams.get_highest_resolution()
    print("Video indiriliyor...")
    pixels.download()
    print("Video başarıyla indirildi :)")

# Tkinter penceresi oluşturduk
pencere = tk.Tk()
pencere.title("Vidin v1.0")
pencere.geometry("699x500")

# Labellerimizi ekledik
label = tk.Label(pencere, font=("Courier", 16, "bold"), text="Lütfen indirmek istediğiniz videonun linkini giriniz")
label.pack()  # Widget'larla aynı hizada olması için yazdık

# Link giriş kutusunu yapalım
linkim_entry = tk.Entry(pencere, width=50)
linkim_entry.pack() # Widget'larla aynı hizada olması için yazdık

# İndirme düğmesini yapalım ve fonksiyonu bağlayalım
download_button = tk.Button(pencere, font=("Courier", 16, "bold"), text="İndir", command=script_indirme)
download_button.pack() # Widget'larla aynı hizada olması için yazdık

pencere.mainloop()
