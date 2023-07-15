import string
import random
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


def evaluate_password_strength(*args): # Şifre gücünü değerlendiriyorum
    password = password_entry.get() # Entry widget'inden şifreyi alıyorum
    score = 0
    
    #şifre uzunluğunu kontrol ediyorum
    if len(password) >= 8:
         score += 1
    if len(password) >= 12:
        score += 1
        
    # Büyük harf, küçük harf, rakam ve özel karakter içeriyor mu sorgusu?
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
        
    # Progrressbar'ı güncelliyorum
    strength_bar['value'] = score
    
    # Güvenlik seviyesi belirliyorum bu alanda
    if score <= 2:
        strength_level.set("Çok Zayıf")
    elif score == 3:
        strength_level.set("Zayıf")
    elif score == 4:
        strength_level.set("Orta")
    elif score == 5:
        strength_level.set("Güçlü")
    else:
        strength_level.set("Çok Güçlü")
        
        
        
        
        
def create_password(): # Rastgele bir şifre oluşturacağım bu bölümde
    # Metin giriş kuturularından verileri alacağım
    try:
        password_length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Hatalı Giriş", "Lütfen şifre uzunluğu için bir sayı girin...")
        return
    
    # Kullanıcıdan alınan karakter setini oluşturuyorum
    password_characters = ''
    if use_lowercase.get():
        password_characters += string.ascii_lowercase
    if use_uppercase.get():
        password_characters += string.ascii_uppercase
    if use_digits.get():
        password_characters += string.digits
    if use_special.get():
        password_characters += string.punctuation
        
    # Şifreyi oluşturuyorum burada
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    # Metin giriş kutusundan platform bilgisini alıyorum
    platform = platform_entry.get()

    # Database işlemleri 
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
            
    # Table oluşturuyorum ve şifreyi kaydediyorum burada
    c.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                platform TEXT,
                password TEXT
            )
            ''')
    c.execute('''
            INSERT INTO passwords (platform, password)
            VALUES (?, ?)
            ''', (platform, password))
    conn.commit()
    conn.close()
        
    # Şifreyi entry widget'a ekliyorum ve gücünü değerlendiriyorum bu kısımda
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    evaluate_password_strength()
        
    
    # Sonuçları bir messagebox ile gösteriyorum
    messagebox.showinfo("Şifre Oluşturuldu", f"Şifreniz başarıyla oluşturuldu ve kaydedildi.\nŞifrenizin gücü {strength_level.get()}")

# tk penceresini oluşturuyorum (arayüz)
root = tk.Tk()
root.title("TUA Passwords Generator")


# Etiketler, metin giriş kutuları ve checkbutton'ları oluşturuyorum

tk.Label(root, text="Şifre uzunluğu ").pack()
length_entry = tk.Entry(root)
length_entry.pack()

tk.Label(root, text="Şifre hangi platform için oluşturulacak? ").pack()
platform_entry = tk.Entry(root)
platform_entry.pack()

use_lowercase = tk.BooleanVar()
use_uppercase = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_special = tk.BooleanVar()

tk.Checkbutton(root, text="Küçük harf", variable=use_lowercase).pack()
tk.Checkbutton(root, text="Büyük harf", variable=use_uppercase).pack()
tk.Checkbutton(root, text="Rakam", variable=use_digits).pack()
tk.Checkbutton(root, text="Özel Karakter", variable=use_special).pack()

tk.Label(root, text="Şifre ").pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Her karakter girişinde şifre gücünü kontrol eden bir event ekliyorum buraya
password_entry.bind('<KeyRelease>', evaluate_password_strength)

# Şifre gücünü gösteren bir progressbar ekliyorum buraya
strength_bar = ttk.Progressbar(root, maximum=6)
strength_bar.pack()

# Güvenlik seviyesini belirten bir label ekliyorum buraya
strength_level = tk.StringVar()
strength_level.set("Çok Zayıf")
tk.Label(root, textvariable=strength_level).pack()

# şifre oluşturma butonu ekliyorum buraya
button = tk.Button(root, text="Şifre oluştur", command=create_password)
button.pack()

#Pencerenin ana döngüsü başlatıyorum
root.mainloop()