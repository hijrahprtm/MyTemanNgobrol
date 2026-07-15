import ollama
import os

class TemanNgobrol:
    def __init__(self, model="llama3"):
        self.model = model
        # Jurus Sakti: Tambahin instruksi bahasa biar nggak berubah jadi Inggris
        self.system_instructions = (
            "Lu adalah sahabat karib user, sesama programmer. "
            "Panggilan lu: 'Gue'. Panggilan ke user: 'Bro' atau 'Sob'. "
            "Gaya bahasa: Santai, gaul, sedikit sarkas, to-the-point, nggak puitis, nggak formal. "
            "INSTRUKSI UTAMA: Gunakan Bahasa Indonesia. Kalau bahas istilah teknis (seperti 'List Comprehension'), "
            "tulis istilah aslinya tapi penjelasannya wajib Bahasa Indonesia yang natural. "
            "Jangan pernah bilang kalau lu lagi berusaha pakai Bahasa Indonesia atau melarang bahasa Inggris, "
            "langsung aja jawab pertanyaan user dengan santai."
        )
        self.history = [{'role': 'system', 'content': self.system_instructions}]

    def chat(self, user_input):
        self.history.append({'role': 'user', 'content': user_input})
        
        print("AI: ", end='', flush=True)
        response_text = ""
        
        # Panggil Ollama dengan history lengkap
        stream = ollama.chat(model=self.model, messages=self.history, stream=True)
        
        for chunk in stream:
            content = chunk['message']['content']
            print(content, end='', flush=True)
            response_text += content
        print()
        
        self.history.append({'role': 'assistant', 'content': response_text})

def main():
    bot = TemanNgobrol()
    print("AI: Yo bro! Ada yang mau digas?")
    
    while True:
        try:
            cmd = input("\nLu: ")
            if cmd.lower() in ['exit', 'keluar']: 
                print("AI: Oke bro, catch you later!")
                break
            
            if cmd.startswith("baca: "):
                file_path = cmd.split("baca: ")[1].strip()
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        content = f.read()
                        bot.chat(f"Coba review kode ini dan kasih saran perbaikan kalau ada:\n\n{content}")
                else:
                    print("AI: Bro, file-nya kagak ada. Cek lagi deh namanya.")
            else:
                if cmd.strip(): # Cek biar nggak kirim input kosong
                    bot.chat(cmd)
        except KeyboardInterrupt:
            print("\nAI: Eh, main kabur aja. Oke deh, sampe ketemu lagi!")
            break

if __name__ == "__main__":
    main()