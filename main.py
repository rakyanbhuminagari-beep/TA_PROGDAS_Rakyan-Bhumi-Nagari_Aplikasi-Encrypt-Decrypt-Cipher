import tkinter as tk
from GUI import CipherGUI
import customtkinter as ctk


from Caesar_Cipher import caesarCipher, caesarDecrypt
from ROT13 import ROT13, ROT13decrypt, ROT18, ROT18decrypt, ROT47, ROT47decrypt
from Vigenère_Cipher import viginereEncrypt, viginereDecrypt

# Jalankan GUI
if __name__ == "__main__":
    root = ctk.CTk()
    app = CipherGUI(
        root,
        caesarCipher, caesarDecrypt,
        ROT13, ROT13decrypt,
        ROT18, ROT18decrypt,
        ROT47, ROT47decrypt,
        viginereEncrypt, viginereDecrypt
    )
    root.mainloop()