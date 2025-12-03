#membatasi nilai unicode / ASCII dari teks yang sesuai dari tabel ASCII (jangkauan huruf kapital) agar saat di ubah nilainya tidak berubah menjadi
#bentuk yang lain 
HURUF_KAPITAL_AWAL = ord("A")
HURUF_KAPITAL_AKHIR= ord("Z")
JANGKAUAN_HURUF_KAPITAL = HURUF_KAPITAL_AKHIR - HURUF_KAPITAL_AWAL + 1

#membatasi nilai unicode / ASCII dari teks yang sesuai dari tabel ASCII (jangkauan huruf non-kapital)
HURUF_KECIL_AWAL = ord("a")
HURUF_KECIL_AKHIR = ord("z")
JANGKAUAN_HURUF_KECIL = HURUF_KECIL_AKHIR - HURUF_KECIL_AWAL +1

def caesarCipher (pesan, shift): 
    hasil = ""
    for char in pesan :
        if char.isalpha() and char.isupper():
            charCode = ord(char)
            newCharcode = charCode + shift

            if newCharcode > HURUF_KAPITAL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KAPITAL
            
            if newCharcode < HURUF_KAPITAL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KAPITAL
        
            newChar = chr(newCharcode)
            hasil += newChar
        elif char.isalpha() and char.islower():
            charCode = ord(char)
            newCharcode= charCode + shift
        
            if newCharcode > HURUF_KECIL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KECIL
            if newCharcode < HURUF_KECIL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KECIL

            newChar = chr(newCharcode)
            hasil += newChar

        else : 
            hasil += char
    return hasil



def caesarDecrypt(pesan, shift):
    hasil = ""
    for char in pesan:
        if char.isalpha() and char.isupper():
            charCode = ord(char)
            newCharcode = charCode - shift

            if newCharcode > HURUF_KAPITAL_AKHIR:
                newCharcode -= JANGKAUAN_HURUF_KAPITAL
            
            if newCharcode < HURUF_KAPITAL_AWAL:
                newCharcode += JANGKAUAN_HURUF_KAPITAL

            hasil += chr(newCharcode)

        elif char.isalpha() and char.islower():
            charCode = ord(char)
            newCharcode = charCode - shift

            if newCharcode > HURUF_KECIL_AKHIR:
                newCharcode -= JANGKAUAN_HURUF_KECIL
            
            if newCharcode < HURUF_KECIL_AWAL:
                newCharcode += JANGKAUAN_HURUF_KECIL

            hasil += chr(newCharcode)

        else:
            hasil += char
    
    return hasil

