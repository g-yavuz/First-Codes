import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        """Başlangıçta gerekli tüm ayarları yapar."""
        self.player_score = 0
        self.computer_score = 0
        self.game_mode = 'normal'  # Varsayılan oyun modu normal
        self.root = root
        self.root.title("Taş, Kağıt, Makas 🪨📄✂️")
        self.root.geometry("500x500")
        self.root.config(bg="#f4f4f9")
        
        
        # Başlık etiketi
        self.title_label = tk.Label(self.root, text="Taş, Kağıt, Makas", font=("Arial", 24, "bold"), bg="#f4f4f9", fg="#333")
        self.title_label.pack(pady=10)
        
        # Skor etiketi
        self.score_label = tk.Label(self.root, text=f"Sen: {self.player_score} 🟢 Bilgisayar: {self.computer_score} 🔴", 
                                    font=("Arial", 16), bg="#f4f4f9", fg="#333")
        self.score_label.pack(pady=10)
        
        # Sonuç etiketi
        self.result_label = tk.Label(self.root, text="Oyuna başlamak için bir seçim yap! 🎉", font=("Arial", 14), bg="#f4f4f9", fg="#555")
        self.result_label.pack(pady=10)
        
        # Mod Seçim Butonları
        self.mode_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.mode_frame.pack(pady=10)

        self.normal_mode_button = tk.Button(self.mode_frame, text="Normal Mod", font=("Arial", 14), bg="#d1e7dd", 
                                            command=self.set_normal_mode, width=10)
        self.normal_mode_button.grid(row=0, column=0, padx=10, pady=10)

        self.cheat_mode_button = tk.Button(self.mode_frame, text="Hileli Mod", font=("Arial", 14), bg="#ffecb3", command=self.set_cheat_mode, width=10)
        self.cheat_mode_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Butonlar
        self.button_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.button_frame.pack(pady=20)
        
        self.taş_button = tk.Button(self.button_frame, text="🪨 Taş", font=("Arial", 14), bg="#d1e7dd", 
                                    command=lambda: self.play('taş'), width=10)
        self.taş_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.kağıt_button = tk.Button(self.button_frame, text="📄 Kağıt", font=("Arial", 14), bg="#ffecb3", command=lambda: self.play('kağıt'), width=10)
        self.kağıt_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.makas_button = tk.Button(self.button_frame, text="✂️ Makas", font=("Arial", 14), bg="#f8d7da", command=lambda: self.play('makas'), width=10)
        self.makas_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Yeniden Oyna Butonu
        self.reset_button = tk.Button(self.root, text="🔄 Yeniden Oyna", font=("Arial", 14), bg="#e0e0e0", command=self.reset_game, width=20)
        self.reset_button.pack(pady=20)

    def get_computer_choice(self,player_choice):
        if self.game_mode == 'cheat':
            if (player_choice == "taş"):
                return "kağıt"
            if (player_choice == "kağıt"):
                return "makas"
            if (player_choice == "makas"):
                return "taş"  
        return random.choice(['taş', 'kağıt', 'makas'])

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Berabere!"
        elif (player_choice == 'taş' and computer_choice == 'makas') or \
            (player_choice == 'kağıt' and computer_choice == 'taş') or \
                (player_choice == 'makas' and computer_choice == 'kağıt'):
            return "Oyuncu kazandı!"
        else:
            return "Bilgisayar kazandı!"
    
    def play(self, player_choice):
        computer_choice = self.get_computer_choice(player_choice)
        result = self.determine_winner(player_choice, computer_choice)
        
        self.result_label.config(text=f"Sen: {player_choice} 🤜 Bilgisayar: {computer_choice} 🤖\n{result}")
        
        if result == "Oyuncu kazandı!":
            self.player_score += 1
        elif result == "Bilgisayar kazandı!":
            self.computer_score += 1
        
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Sen: {self.player_score} 🟢 Bilgisayar: {self.computer_score} 🔴")

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.result_label.config(text="Oyuna başlamak için bir seçim yap!")
        self.update_score()

    def set_normal_mode(self):
        """Normal modda oynamayı seçer."""
        self.game_mode = 'normal'
        self.result_label.config(text= "Normal mod seçildi! Oyuna başlamak için bir seçim yap! ")

    def set_cheat_mode(self):
        self.game_mode = 'cheat'
        self.result_label.config(text= "Hileli mod seçildi! Oyuna başlamak için bir seçim yap! ")

# Tkinter Penceresini oluştur
root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
