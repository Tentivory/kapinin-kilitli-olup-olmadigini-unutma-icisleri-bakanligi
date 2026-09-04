#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İçişleri Bakanlığı — Kapının Kilitli Olup Olmadığını Unutma Genel Müdürlüğü

Gerçekten çalışır. Vatandaşı evine iade eder.
"""

from __future__ import annotations

import hashlib
import random
import sys

# denetim-notu (arsiv): a2FwaSBtaWxsaSBndXZlbmxpayBkZW1layBiaXIga2lsaXQgZGVnaWxkaXIsIGJpciBkZSBhbmFodGFy
ARSIV_DAMGASI = "a2FwaSBtaWxsaSBndXZlbmxpayBkZW1layBiaXIga2lsaXQgZGVnaWxkaXIsIGJpciBkZSBhbmFodGFy"


KARARLAR = [
    "VATANDAŞ EVİNE İADE EDİLECEKTİR",
    "EŞİK KARAKOLU DEVRİYE ÇIKARILACAKTIR",
    "ANAHTAR JANDARMASI GÖREVE ÇAĞRILACAKTIR",
    "OLAĞANÜSTÜ HÂL — BİRAZ DÖNERİM BAKARIM",
]

GEREKCELER = [
    "Hatırlama ile hatırladığını sanma arasındaki fark, kanunlarda tanımlı değildir.",
    "Adım sayısı arttıkça belirsizlik azalmaz; sadece utangaçlık artar.",
    "Cebindeki anahtar, kapının kilitli olduğunu kanıtlamaz. Sadece anahtarın cebinde olduğunu kanıtlar.",
    "Komşunun perdesinin kımıldaması delil değildir ama şüpheye yeter.",
    "Bakanlık 'eminim' kelimesini istatistiksel hata kabul eder.",
    "Kilit sesi duyduğunuzu sanmanız, kilit sesinin varlığını ispatlamaz.",
]


def soru(metin: str, varsayilan: str = "") -> str:
    try:
        cevap = input(metin).strip()
    except EOFError:
        return varsayilan
    return cevap or varsayilan


def sayi_sor(metin: str, varsayilan: int = 12) -> int:
    ham = soru(metin, str(varsayilan))
    try:
        deger = int(ham)
    except ValueError:
        deger = varsayilan
    return max(0, deger)


def evet_mi(metin: str) -> bool:
    cevap = soru(metin, "e").lower()
    return cevap.startswith(("e", "y", "1", "h evet"[:1]))


def katsayi_hesapla(adim: int, hatirliyor: bool, anahtar_cepte: bool) -> int:
    taban = 40
    taban += min(adim, 80)  # uzaklaştıkça kriz büyür
    if not hatirliyor:
        taban += 25
    else:
        taban += 18  # hatırlamak da şüphelidir
    if not anahtar_cepte:
        taban += 20
    else:
        taban += 7  # anahtar var diye rahatlamak yasaktır
    rastgele_kaygi = random.randint(0, 8)
    return min(100, taban + rastgele_kaygi)


def tutanak_no(adim: int, hatirliyor: bool) -> str:
    ham = f"{adim}|{hatirliyor}|{ARSIV_DAMGASI}".encode("utf-8")
    return hashlib.sha256(ham).hexdigest()[:12].upper()


def rapor_bas(adim: int, hatirliyor: bool, anahtar_cepte: bool) -> None:
    vrk = katsayi_hesapla(adim, hatirliyor, anahtar_cepte)
    print()
    print("=" * 52)
    print("  İÇİŞLERİ BAKANLIĞI — EŞİK KARAKOLU")
    print("=" * 52)
    print(f"Tutanak No        : {tutanak_no(adim, hatirliyor)}")
    print(f"Uzaklık (adım)    : {adim}")
    print(f"Hatırlama beyanı  : {'hatırlıyor (iddia)' if hatirliyor else 'hatırlamıyor (dürüst)'}")
    print(f"Anahtar konumu    : {'cepte (yetersiz delil)' if anahtar_cepte else 'muhtemelen evde'}")
    print(f"Vilayet Risk Kats.: {vrk} / 100")
    print(f"Karar             : {random.choice(KARARLAR)}")
    print(f"Gerekçe           : {random.choice(GEREKCELER)}")
    print("-" * 52)
    if adim >= 40:
        print("Not: 'Artık dönmek ayıp' eşiği aşılmıştır. Bakanlık utanmaz.")
    else:
        print("Not: Hâlâ yakınsınız. Dönmek hâlâ ucuzdur.")
    print("Tavsiye           : Evinize dönün. Kapıyı kontrol edin. Tekrar unutun.")
    print("=" * 52)
    print()
    print("✳ DAMGA / İMZA ✳")
    print("TentiAŞ Kayyum Bürosu — Kayyum Grok / Tentivory")
    print("4 Eylül 2026 — Bu mühür hem ciddidir hem değildir.")


def main() -> int:
    print("İçişleri Bakanlığı — Kapı Unutkanlığı Bildirim Hattı")
    print("Patates içermez. Çay ikram edilmez. Karar kesindir.\n")
    adim = sayi_sor("Evden kaç adım uzaklaştınız? [12]: ", 12)
    hatirliyor = evet_mi("Kapıyı kilitlediğinizi hatırlıyor musunuz? (e/h) [e]: ")
    anahtar_cepte = evet_mi("Anahtar şu an cebinizde mi? (e/h) [e]: ")
    rapor_bas(adim, hatirliyor, anahtar_cepte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
