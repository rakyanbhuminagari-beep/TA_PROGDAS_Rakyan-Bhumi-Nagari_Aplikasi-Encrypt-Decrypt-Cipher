import customtkinter as ctk

class CipherGUI:
    def __init__(self, root, caesar_encrypt, caesar_decrypt, 
                 rot13_enc, rot13_dec, rot18_enc, rot18_dec, rot47_enc, rot47_dec,
                 vigenere_enc, vigenere_dec):
        self.root = root
        self.root.title("Enkripsi & Dekripsi Pesan")
        self.root.geometry("750x720")
        self.root.resizable(True,True)
        
        # Set tema dark mode
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Simpan fungsi cipher
        self.caesar_encrypt = caesar_encrypt
        self.caesar_decrypt = caesar_decrypt
        self.rot13_enc = rot13_enc
        self.rot13_dec = rot13_dec
        self.rot18_enc = rot18_enc
        self.rot18_dec = rot18_dec
        self.rot47_enc = rot47_enc
        self.rot47_dec = rot47_dec
        self.vigenere_enc = vigenere_enc
        self.vigenere_dec = vigenere_dec
        
        # Variables
        self.shift_var = ctk.IntVar(value=0)
        self.mode = ctk.StringVar(value="encrypt")
        self.cipher_type = ctk.StringVar(value="Caesar Cipher")
        self.key_var = ctk.StringVar(value="")
        
        # Setup GUI terlebih dahulu
        self.setup_gui()
        
        # Trace untuk auto-update
        self.shift_var.trace('w', lambda *args: self.process_message())
        self.mode.trace('w', lambda *args: self.process_message())
        self.cipher_type.trace('w', lambda *args: self.on_cipher_change())
        self.key_var.trace('w', lambda *args: self.process_message())
        
    def setup_gui(self):
        # Frame utama
        main_frame = ctk.CTkFrame(self.root, corner_radius=15)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Judul
        title_label = ctk.CTkLabel(main_frame, text="Multi Cipher Tool", 
                                   font=("Times New Roman", 32, "bold"),
                                   text_color="#3b82f6")
        title_label.pack(pady=(20, 5))
        
        subtitle_label = ctk.CTkLabel(main_frame, text="Enkripsi dan Dekripsi Pesan", 
                                      font=("Arial", 14))
        subtitle_label.pack(pady=(0, 20))
        
        # Pilihan Cipher Type
        cipher_label = ctk.CTkLabel(main_frame, text="Pilih Metode Cipher:", 
                                    font=("Arial", 13, "bold"),
                                    anchor="w")
        cipher_label.pack(pady=(5,10), padx=15, anchor="w")
        
        cipher_options = [
            "Caesar Cipher",
            "ROT13",
            "ROT18", 
            "ROT47",
            "Vigenere Cipher"
        ]
        
        self.cipher_combo = ctk.CTkComboBox(main_frame, 
                                           variable=self.cipher_type,
                                           values=cipher_options,
                                           width=680,
                                           height=40,
                                           font=("Arial", 13),
                                           dropdown_font=("Arial", 12),
                                           state="readonly")
        self.cipher_combo.pack(pady=(0, 20), padx=30)
        
        # Radio button untuk mode Encrypt/Decrypt
        mode_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        mode_frame.pack(pady=(0, 20))
        
        encrypt_radio = ctk.CTkRadioButton(mode_frame, text="Enkripsi", 
                                          variable=self.mode, value="encrypt",
                                          font=("Arial", 14, "bold"),
                                          radiobutton_width=20,
                                          radiobutton_height=20)
        encrypt_radio.pack(side="left", padx=30)
        
        decrypt_radio = ctk.CTkRadioButton(mode_frame, text="Dekripsi", 
                                          variable=self.mode, value="decrypt",
                                          font=("Arial", 14, "bold"),
                                          radiobutton_width=20,
                                          radiobutton_height=20)
        decrypt_radio.pack(side="left", padx=30)
        
        # Input pesan
        input_label = ctk.CTkLabel(main_frame, text="Pesan Input:", 
                                   font=("Arial", 13, "bold"),
                                   anchor="w")
        input_label.pack(pady=(0, 5), padx=30, anchor="w")
        
        self.input_text = ctk.CTkTextbox(main_frame, height=120, width=680,
                                        font=("Consolas", 12),
                                        corner_radius=10,
                                        border_width=2,
                                        wrap="word")
        self.input_text.pack(pady=(0, 15), padx=30)
        self.input_text.bind('<KeyRelease>', lambda e: self.process_message())
        
        # Frame untuk Caesar Cipher Control (KOMPAK)
        self.caesar_frame = ctk.CTkFrame(main_frame, corner_radius=10, 
                                        fg_color=("#2b2b2b", "#1a1a1a"))
        self.caesar_frame.pack(pady=(0, 15), padx=30, fill="x")
        
        # Horizontal layout untuk shift control yang kompak
        shift_horizontal_frame = ctk.CTkFrame(self.caesar_frame, fg_color="transparent")
        shift_horizontal_frame.pack(pady=10, padx=20)
        
        caesar_title = ctk.CTkLabel(shift_horizontal_frame, 
                                    text="Shift:",
                                    font=("Arial", 13, "bold"))
        caesar_title.pack(side="left", padx=(0, 15))
        
        minus_btn = ctk.CTkButton(shift_horizontal_frame, text="−", width=40, height=35,
                                 font=("Arial", 18, "bold"),
                                 hover_color="#1E93AB",
                                 corner_radius=8,
                                 command=self.decrement_shift)
        minus_btn.pack(side="left", padx=5)
        
        self.shift_display = ctk.CTkLabel(shift_horizontal_frame, 
                                         textvariable=self.shift_var,
                                         font=("Arial", 20, "bold"),
                                         width=60, height=35,
                                         fg_color=("#3b3b3b", "#2a2a2a"),
                                         corner_radius=8)
        self.shift_display.pack(side="left", padx=8)
        
        plus_btn = ctk.CTkButton(shift_horizontal_frame, text="+", width=40, height=35,
                                font=("Arial", 18, "bold"),
                                fg_color="#10b981", hover_color="#AF0404",
                                corner_radius=8,
                                command=self.increment_shift)
        plus_btn.pack(side="left", padx=5)
        
        shift_range = ctk.CTkLabel(shift_horizontal_frame, 
                                  text="(-25 s/d +25)",
                                  font=("Arial", 11),
                                  text_color="gray")
        shift_range.pack(side="left", padx=(10, 0))
        
        # Frame untuk Vigenere Cipher Control
        self.vigenere_frame = ctk.CTkFrame(main_frame, corner_radius=10,
                                          fg_color=("#2b2b2b", "#1a1a1a"))
        self.vigenere_frame.pack(pady=(0, 15), padx=30, fill="x")
        
        key_input_frame = ctk.CTkFrame(self.vigenere_frame, fg_color="transparent")
        key_input_frame.pack(pady=10, padx=20, fill="x")
        
        key_label = ctk.CTkLabel(key_input_frame, text="Kunci:", 
                                font=("Arial", 13, "bold"))
        key_label.pack(side="left", padx=(0, 10))
        
        self.key_entry = ctk.CTkEntry(key_input_frame, 
                                     textvariable=self.key_var,
                                     font=("Arial", 13),
                                     height=35,
                                     corner_radius=8,
                                     border_width=2,
                                     placeholder_text="Masukkan kunci...")
        self.key_entry.pack(side="left", fill="x", expand=True)
        
        key_note = ctk.CTkLabel(self.vigenere_frame, 
                               text="* Hanya huruf (A-Z atau a-z)",
                               font=("Arial", 10),
                               text_color="gray")
        key_note.pack(pady=(0, 10))
        
        self.vigenere_frame.pack_forget()
        
        # Frame untuk ROT
        self.rot_frame = ctk.CTkFrame(main_frame, corner_radius=10,
                                     fg_color=("#2b2b2b", "#1a1a1a"))
        self.rot_frame.pack(pady=(0, 15), padx=30, fill="x")
        
        rot_info = ctk.CTkLabel(self.rot_frame, 
                               text="ROT cipher bekerja otomatis tanpa pengaturan",
                               font=("Arial", 12))
        rot_info.pack(pady=12)
        
        self.rot_frame.pack_forget()
        
        # Output pesan
        output_label = ctk.CTkLabel(main_frame, text="Hasil:", 
                                   font=("Arial", 13, "bold"),
                                   anchor="w")
        output_label.pack(pady=(5, 5), padx=30, anchor="w")
        
        self.output_text = ctk.CTkTextbox(main_frame, height=120, width=680,
                                         font=("Consolas", 12),
                                         corner_radius=10,
                                         border_width=2,
                                         fg_color=("#2b2b2b", "#1a1a1a"),
                                         wrap="word")
        self.output_text.pack(pady=(0, 20), padx=30)
        self.output_text.configure(state="disabled")
        
    def on_cipher_change(self):
        cipher = self.cipher_type.get()
        
        # Sembunyikan semua frame
        self.caesar_frame.pack_forget()
        self.vigenere_frame.pack_forget()
        self.rot_frame.pack_forget()
        
        # Tampilkan frame yang sesuai
        if cipher == "Caesar Cipher":
            self.caesar_frame.pack(pady=(0, 15), padx=30, fill="x", 
                                  before=self.output_text.master.winfo_children()[-2])
        elif cipher == "Vigenere Cipher":
            self.vigenere_frame.pack(pady=(0, 15), padx=30, fill="x",
                                    before=self.output_text.master.winfo_children()[-2])
        else:
            self.rot_frame.pack(pady=(0, 15), padx=30, fill="x",
                               before=self.output_text.master.winfo_children()[-2])
            
        self.process_message()
    
    def increment_shift(self):
        current = self.shift_var.get()
        if current < 25:
            self.shift_var.set(current + 1)
    
    def decrement_shift(self):
        current = self.shift_var.get()
        if current > -25:
            self.shift_var.set(current - 1)
    
    def process_message(self):
        pesan = self.input_text.get("1.0", "end-1c").strip()
        
        if not pesan:
            self.update_output("")
            return
        
        cipher = self.cipher_type.get()
        mode = self.mode.get()
        hasil = ""
        
        try:
            if cipher == "Caesar Cipher":
                shift = self.shift_var.get()
                if mode == "encrypt":
                    hasil = self.caesar_encrypt(pesan, shift)
                else:
                    hasil = self.caesar_decrypt(pesan, shift)
                    
            elif cipher == "ROT13":
                if mode == "encrypt":
                    hasil = self.rot13_enc(pesan)
                else:
                    hasil = self.rot13_dec(pesan)
                    
            elif cipher == "ROT18":
                if mode == "encrypt":
                    hasil = self.rot18_enc(pesan)
                else:
                    hasil = self.rot18_dec(pesan)
                    
            elif cipher == "ROT47":
                if mode == "encrypt":
                    hasil = self.rot47_enc(pesan)
                else:
                    hasil = self.rot47_dec(pesan)
                    
            elif cipher == "Vigenere Cipher":
                kunci = self.key_var.get().strip()
                if not kunci:
                    hasil = "[Masukkan kunci terlebih dahulu]"
                elif not kunci.isalpha():
                    hasil = "[Kunci harus berupa huruf saja (A-Z atau a-z)]"
                else:
                    if mode == "encrypt":
                        hasil = self.vigenere_enc(pesan, kunci)
                    else:
                        hasil = self.vigenere_dec(pesan, kunci)
            
            if not hasil and cipher != "Vigenere Cipher":
                hasil = pesan
                        
        except AttributeError as e:
            if "isnumber" in str(e):
                hasil = "[Error: Bug di kode ROT18 - gunakan isdigit() bukan isnumber()]"
            else:
                hasil = "[Error: " + str(e) + "]"
        except Exception as e:
            hasil = "[Error: " + str(e) + "]"
        
        self.update_output(hasil)
    
    def update_output(self, text):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", text)
        self.output_text.configure(state="disabled")