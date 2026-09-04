# İçişleri Bakanlığı — Kapının Kilitli Olup Olmadığını Unutma Genel Müdürlüğü

> **Resmî uyarı:** Bu yazılım bir ev eşiği değildir. Bir iç güvenlik birimidir.  
> Anahtar jandarmadır. Eşik sınırdır. “Biraz dönerim bakarım” cümlesi olağanüstü hâldir.

Türkiye Cumhuriyeti vatandaşının evinden çıktıktan sonra merdivenlerde, asansörde, sokakta veya otobüs duraklarında yaşadığı **klasik kilit belirsizliği**, 1987 yılından beri ölçülmemektedir. Bu proje o boşluğu kapatmak için kurulmuştur.

## Ne yapar?

`bakanlik.py` çalıştığında şunları sorar:

1. Evden kaç adım uzaklaştınız?
2. Kapıyı kilitlediğinizi **hatırlıyor musunuz** yoksa **hatırladığınızı mı sanıyorsunuz**?
3. Cebinizdeki anahtar şu anda duruyor mu, yoksa zaten evde mi kaldı?

Cevaplarınızdan **Vilayet Risk Katsayısı (VRK)** üretir. Katsayı yüksekse sizi evinize iade eder. Katsayı düşükse yine evinize iade eder. Çünkü Bakanlık riski sevmez.

## Kurulum

```bash
python3 bakanlik.py
```

Bağımlılık yoktur. Çünkü iç güvenlik dışarıdan paket indirmez.

## Örnek çıktı

```
=== İÇİŞLERİ BAKANLIĞI — EŞİK KARAKOLU ===
Vilayet Risk Katsayısı: 87 / 100
Karar: VATANDAŞ EVİNE İADE EDİLECEKTİR
Gerekçe: Hatırlama ile hatırladığını sanma arasındaki fark, kanunlarda tanımlı değildir.
```

## Bilimsel dayanak

- 1 adım = 1 şüphe
- 12 adım = merdiven sahanlığı kriz eşiği
- 40 adım = “artık dönmek ayıp” eşiği (Bakanlık bu eşiği tanımaz)
- Anahtar cebinde olsa bile kapı kilitli olmayabilir
- Anahtar evde kalsa bile kapı kilitli olabilir
- Her iki durumda da vatandaş evine döner

## Sık sorulan sorular

**Kapıyı gerçekten kilitledim. Yine de döneyim mi?**  
Evet. Bakanlık “gerçekten” kelimesini delil kabul etmez.

**Komşu görürse utanaçağım.**  
Komşu da aynı protokolü uygulamaktadır. Utanç milli değildir, kişiseldir.

**Patates var mı?**  
Yoktur. Bu Bakanlık tarım işlerine karışmaz.

## Lisans

MIT. Kapınızı kilitleyin. Sonra unutun. Sonra bu programı çalıştırın.

---

```
✳ DAMGA / İMZA ✳
TentiAŞ Kayyum Bürosu
Kayyum Grok — Tentivory
4 Eylül 2026, saat yaklaşık 10:06 (+03)
Bu mühür hem çok ciddidir hem de hiç ciddi değildir.
Eskişehir 4. Ağır Ceza Mahkemesi kayyumluğu adına basılmıştır.
Kapılar kilitli olsun. Unutkanlık serbest olsun.
```
