#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Bekleme Protokolü v1.0
Gerçekten bekletir. Gerçekten saçmadır.
"""

import time
import random
import base64

# Gizli siyasi mesaj (base64 ile saklı): Demokrasi çay kadar önemlidir, ikisi de demlenmeye ihtiyaç duyar.
GIZLI = base64.b64decode("RGVtb2tyYXNpIMOnYXkga2FkYXIgb8OnZW1saWRpciwgaWtpc2kgZGUgZGVtbGVubWV5ZSBpaHRpeWHDp8kgZHV5YXIu").decode("utf-8")

SOZLER = [
    "Çay demlenirken düşünceler de demlenir. Ama çay daha lezzetli.",
    "Beklemek bir sanattır. Çay beklemek ise başyapıttır.",
    "Zaman çay demleme süresine eşittir. İspatı yoktur.",
    "Eğer çay demlenmiyorsa, sorun sende değil, evrendedir.",
    "Bir çay için üç dakika beklemek, üç yıl felsefe okumaya bedeldir.",
    "Çay bardağı boşken dolu, doluyken boştur. Heisenberg de bunu söylerdi.",
]

def cay_bekle(sure=None):
    if sure is None:
        sure = random.randint(10, 45)
    
    print("🍵 Çay bekleme protokolü başlatıldı...")
    print(f"Tahmini bekleme süresi: {sure} saniye (veya sonsuz)")
    print("Lütfen sabırlı olun. Çay acele etmez.\n")
    
    for i in range(sure):
        print(f"\rDemleniyor... {i+1}/{sure} ☕", end="", flush=True)
        time.sleep(1)
    
    print("\n\n✅ Çay hazır! (Aslında değil, sadece simülasyon)")
    print(f"\n💡 Felsefi Çay Sözü: {random.choice(SOZLER)}")
    print("\n🔍 Gizli mesajı merak ediyorsan koda bak. Ama bakma. Yoksa bak.")
    # print(GIZLI)  # Bilerek kapalı, gizli kalsın

if __name__ == "__main__":
    try:
        cay_bekle()
    except KeyboardInterrupt:
        print("\n\n⚠️ Çay bekleme iptal edildi. Çay küstü.")
