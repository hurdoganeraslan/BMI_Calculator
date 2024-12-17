import tkinter as tk


# BMI hesaplama fonksiyonu
def hesapla_bmi():
    try:
        # Boy ve kilo değerlerini al
        boy = float(my_entry.get())
        kilo = float(my_entry.get())

        # Boyu metre cinsine çevirmek (cm'yi metreye çevirelim)
        boy = boy / 100

        # BMI hesaplama
        bmi = kilo / (boy ** 2)

        # Açıklama metnini güncelle
        my_aciklama.config(text=my_aciklama(bmi))

    except ValueError:
        my_aciklama.config(text="Lütfen geçerli bir değer girin.")


# BMI değerine göre açıklama döndüren fonksiyon
def bmi_aciklama(bmi):
    if bmi < 18.5:
        return "Kilo Düşüklüğü: Sağlıklı bir kilo aralığında değilsiniz, bir sağlık uzmanı ile görüşün."
    elif 18.5 <= bmi < 24.9:
        return "Normal Kilo: Sağlıklı bir vücut ağırlığınız var."
    elif 25 <= bmi < 29.9:
        return "Fazla Kilo: Kilonuzu sağlıklı bir seviyeye çekmek için bir uzmandan tavsiye alabilirsiniz."
    elif 30 <= bmi < 34.9:
        return "Obezite Sınıfı 1: Sağlık riskleri arttı, bir sağlık uzmanına başvurun."
    elif 35 <= bmi < 39.9:
        return "Obezite Sınıfı 2: Ciddi sağlık riskleri bulunuyor, doktor önerisi önemlidir."
    else:
        return "Obezite Sınıfı 3: Çok ciddi sağlık riskleri mevcut, tıbbi yardım almanız önerilir."


# Ana pencereyi oluştur
window = tk.Tk()
window.title("BMI Calculator")
window.minsize(width=500, height=200)

# Boy etiket ve giriş alanı
my_label = tk.Label(window, text="Boyunuzu Yazınız(cm)")
my_label.pack()

my_entry = tk.Entry(window)
my_entry.pack()

# Kilo etiket ve giriş alanı
my_label = tk.Label(window, text="Kilonuzu Yazın(kg)")
my_label.pack()

my_entry = tk.Entry(window)
my_entry.pack()

# Hesapla butonu
my_hesapla_button = tk.Button(window, text="Hesapla", command=hesapla_bmi)
my_hesapla_button.pack()


# Açıklama etiketini oluştur
my_aciklama_label = tk.Label(window, text="BMI açıklaması:")
my_aciklama_label.pack()

# Açıklama metni
my_aciklama = tk.Label(window, text="", justify="left", padx=10, pady=5)
my_aciklama.pack()

# Pencereyi çalıştır
window.mainloop()
