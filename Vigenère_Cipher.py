#membatasi nilai unicode / ASCII dari teks yang sesuai dari tabel ASCII (jangkauan huruf kapital) agar saat di ubah nilainya tidak berubah menjadi
#bentuk yang lain 
HURUF_KAPITAL_AWAL = ord("A")
HURUF_KAPITAL_AKHIR= ord("Z")
JANGKAUAN_HURUF_KAPITAL = HURUF_KAPITAL_AKHIR - HURUF_KAPITAL_AWAL + 1

#membatasi nilai unicode / ASCII dari teks yang sesuai dari tabel ASCII (jangkauan huruf non-kapital)
HURUF_KECIL_AWAL = ord("a")
HURUF_KECIL_AKHIR = ord("z")
JANGKAUAN_HURUF_KECIL = HURUF_KECIL_AKHIR - HURUF_KECIL_AWAL +1

def buatKunci (pesan,kunci) :
    kunciShift = "".join([c.lower() for c in kunci if c.isalpha()])
    i = 0
    for char in pesan :
        if char.isalpha() :
            kunciShift += kunci[i % len(kunci)].lower()
            i += 1
        else :
            kunciShift += char

    return kunciShift

def viginereEncrypt (pesan,kunci) :
    hasil = ""
    inputkunci = buatKunci(pesan,kunci)
    
    for pChar, kChar in zip(pesan,inputkunci) :
        if pChar.isalpha() and pChar.isupper() :
            shift = ord(kChar) - ord("a")
            shiftPesan = ord(pChar) - HURUF_KAPITAL_AWAL
            enkripsi = (shiftPesan + shift) % 26
            hasil += chr(enkripsi + HURUF_KAPITAL_AWAL)

        elif pChar.isalpha() and pChar.islower() :
            shift = ord(kChar) - ord("a")
            shiftPesan = ord(pChar) - HURUF_KECIL_AWAL
            enkripsi = (shiftPesan +shift) % 26
            hasil += chr (enkripsi + HURUF_KECIL_AWAL)

        else :
            hasil += pChar

    return hasil


def viginereDecrypt (pesan,kunci) :
    hasil = ""
    inputkunci = buatKunci(pesan,kunci)
    
    for pChar, kChar in zip(pesan,inputkunci) :
        if pChar.isalpha() and pChar.isupper() :
            shift = ord(kChar) - ord("a")
            shiftPesan = ord(pChar) - HURUF_KAPITAL_AWAL
            enkripsi = (shiftPesan - shift) % 26
            hasil += chr(enkripsi + HURUF_KAPITAL_AWAL)

        elif pChar.isalpha() and pChar.islower() :
            shift = ord(kChar) - ord("a")
            shiftPesan = ord(pChar) - HURUF_KECIL_AWAL
            enkripsi = (shiftPesan - shift) % 26
            hasil += chr (enkripsi + HURUF_KECIL_AWAL)

        else :
            hasil += pChar

    return hasil

