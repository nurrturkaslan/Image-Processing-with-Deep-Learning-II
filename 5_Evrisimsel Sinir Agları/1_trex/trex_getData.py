"""
Trex Projesi

1- Veri topla
2- Derin öğrenme modelinin eğitimini gerçekleştir
3- Modeli test et
"""

import keyboard #klavye üzerindeki tuşları kullanarak veri toplamamıza yardımcı olacak kütüphane
import uuid #bu kütüphane sayesindede ekrandan kayıt alabileceğiz
import time #süreyi tutacağız
from PIL import Image #python resim kütüphanesi
from mss import mss #bizim pikseller doğrultusunda ekrandan o ilgili alanı kesip frame e dönüştürecek kütüphanemiz


"""
http://www.trex-game.skipser.com/
"""

mon = {"top":300, "left":770, "width":250, "height":100}
sct = mss()

i = 0

def record_screen(record_id, key):
    global i
    
    i += 1
    print("{}: {}".format(key, i))
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("./img_/{}_{}_{}.png".format(key, record_id, i)) #img klasörü açmanız gerek yoksa hata verecektir
    
is_exit = False #fonk. çıkmamı sağlayacak, veri toplama işlemini bırakmak için

def exit():
    global is_exit
    is_exit = True
    
keyboard.add_hotkey("esc", exit)

record_id = uuid.uuid4()

while True:
    
    if is_exit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screen(record_id, "up")
            time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screen(record_id, "down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):
            record_screen(record_id, "right")
            time.sleep(0.1)
    except RuntimeError: continue
            

#try kendi içerisindeki kodu deniyor except ile kodun calısmasında bir hata olursa runTimeError ver diyor






















