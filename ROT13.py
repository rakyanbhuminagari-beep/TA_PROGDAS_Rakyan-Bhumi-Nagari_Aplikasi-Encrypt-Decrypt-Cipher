#membatasi nilai unicode / ASCII dari teks yang sesuai dari tabel ASCII (jangkauan huruf kapital) agar saat di ubah nilainya tidak berubah menjadi
#bentuk yang lain 
HURUF_KAPITAL_AWAL = ord("A")
HURUF_KAPITAL_AKHIR= ord("Z")
JANGKAUAN_HURUF_KAPITAL = HURUF_KAPITAL_AKHIR - HURUF_KAPITAL_AWAL + 1

#membatasi nilai unicode / ASCII dari teks yang sesuai dari tabel ASCII (jangkauan huruf non-kapital)
HURUF_KECIL_AWAL = ord("a")
HURUF_KECIL_AKHIR = ord("z")
JANGKAUAN_HURUF_KECIL = HURUF_KECIL_AKHIR - HURUF_KECIL_AWAL +1

#membatasi nilai nomor
KODE_AWAL_NOMOR = ord("0")
KODE_AKHIR_NOMOR = ord("9")
JANGKAUAN_KODE_NOMOR = KODE_AKHIR_NOMOR-KODE_AWAL_NOMOR + 1

# #membatasi kode pada rot47
BATAS_AWAL = ord("!")
BATAS_AKHIR = ord("~")
JANGKAUAN_KODE = BATAS_AKHIR-BATAS_AWAL +1

def ROT13 (pesan): 
    hasil = ""
    for char in pesan :
        if char.isalpha() and char.isupper():
            charCode = ord(char)
            newCharcode = charCode + 13

            if newCharcode > HURUF_KAPITAL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KAPITAL
            
            if newCharcode < HURUF_KAPITAL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KAPITAL
        
            newChar = chr(newCharcode)
            hasil += newChar
        elif char.isalpha() and char.islower():
            charCode = ord(char)
            newCharcode= charCode + 13
        
            if newCharcode > HURUF_KECIL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KECIL
            
            if newCharcode < HURUF_KECIL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KECIL
                
            newChar = chr(newCharcode)
            hasil += newChar

        else : 
            hasil += char
    return hasil


def ROT18 (pesan): 
    hasil = ""
    for char in pesan :
        if char.isalpha() and char.isupper():
            charCode = ord(char)
            newCharcode = charCode + 18

            if newCharcode > HURUF_KAPITAL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KAPITAL
            
            if newCharcode < HURUF_KAPITAL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KAPITAL
        
            newChar = chr(newCharcode)
            hasil += newChar
        elif char.isalpha() and char.islower():
            charCode = ord(char)
            newCharcode= charCode + 18
        
            if newCharcode > HURUF_KECIL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KECIL
            
            if newCharcode < HURUF_KECIL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KECIL
                
            newChar = chr(newCharcode)
            hasil += newChar
        
        elif char.isdigit():
            charCode = ord(char)
            newCharcode = charCode + 5

            if newCharcode > KODE_AKHIR_NOMOR :
                newCharcode -= JANGKAUAN_KODE_NOMOR
            if newCharcode < KODE_AWAL_NOMOR :
                newCharcode += JANGKAUAN_KODE_NOMOR
            
            newChar = chr(newCharcode)
            hasil += newChar

        else : 
            hasil += char
    return hasil



def ROT47 (pesan): 
    hasil = ""
    for char in pesan :
        charCode = ord(char)
        if BATAS_AWAL <=charCode <= BATAS_AKHIR :
            newCharcode = charCode + 47
            if newCharcode > BATAS_AKHIR :
                newCharcode -= JANGKAUAN_KODE
            if newCharcode < BATAS_AWAL :
                newCharcode += JANGKAUAN_KODE
            
            newChar = chr(newCharcode)
            hasil += newChar
    
           
        else : 
            hasil += char
    return hasil



def ROT13decrypt (pesan): 
    hasil = ""
    for char in pesan :
        if char.isalpha() and char.isupper():
            charCode = ord(char)
            newCharcode = charCode - 13

            if newCharcode > HURUF_KAPITAL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KAPITAL
            
            if newCharcode < HURUF_KAPITAL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KAPITAL
        
            newChar = chr(newCharcode)
            hasil += newChar
        elif char.isalpha() and char.islower():
            charCode = ord(char)
            newCharcode= charCode - 13
        
            if newCharcode > HURUF_KECIL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KECIL
            
            if newCharcode < HURUF_KECIL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KECIL
                
            newChar = chr(newCharcode)
            hasil += newChar

        else : 
            hasil += char
    return hasil


def ROT18decrypt (pesan): 
    hasil = ""
    for char in pesan :
        if char.isalpha() and char.isupper():
            charCode = ord(char)
            newCharcode = charCode - 18

            if newCharcode > HURUF_KAPITAL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KAPITAL
            
            if newCharcode < HURUF_KAPITAL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KAPITAL
        
            newChar = chr(newCharcode)
            hasil += newChar
        elif char.isalpha() and char.islower():
            charCode = ord(char)
            newCharcode= charCode -18
        
            if newCharcode > HURUF_KECIL_AKHIR :
                newCharcode -= JANGKAUAN_HURUF_KECIL
            
            if newCharcode < HURUF_KECIL_AWAL :
                newCharcode += JANGKAUAN_HURUF_KECIL
                
            newChar = chr(newCharcode)
            hasil += newChar
        
        elif char.isdigit() and char:
            charCode = ord(char)
            newCharcode = charCode - 5

            if newCharcode > KODE_AKHIR_NOMOR :
                newCharcode -= JANGKAUAN_KODE_NOMOR
            if newCharcode < KODE_AWAL_NOMOR :
                newCharcode += JANGKAUAN_KODE_NOMOR
            
            newChar = chr(newCharcode)
            hasil += newChar

        else : 
            hasil += char
    return hasil




def ROT47decrypt (pesan): 
    hasil = ""
    for char in pesan :
        charCode = ord(char)
        if BATAS_AWAL <=charCode <= BATAS_AKHIR :
            newCharcode = charCode - 47
            if newCharcode > BATAS_AKHIR :
                newCharcode -= JANGKAUAN_KODE
            if newCharcode < BATAS_AWAL :
                newCharcode += JANGKAUAN_KODE
            
            newChar = chr(newCharcode)
            hasil += newChar
        else : 
            hasil += char
    return hasil