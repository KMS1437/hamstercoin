import tkinter as tk

class CumsterCumbat:
    def __init__(self, master):
        self.master = master
        self.master.title("Hamster Combat")

        self.coins = 0
        self.coins_label = tk.Label(master, text="Камстеры: 0", font=("Arial", 24))
        self.coins_label.pack(pady=20)

        self.coin_image = tk.PhotoImage(file="cumstercoin.png")
        self.coin_image = self.coin_image.subsample(5, 8)

        self.click_button = tk.Button(master, image=self.coin_image, command=self.click)
        self.click_button.pack(pady=20)

        self.reset_button = tk.Button(master, text="Сбросить", command=self.reset, font=("Arial", 20))
        self.reset_button.pack(pady=20)

    def click(self):
        self.coins += 112093
        self.coins_label.config(text=f"Камстеры: {self.coins}")

    def reset(self):
        self.coins = 0
        self.coins_label.config(text=f"Монеты: {self.coins}")

if __name__ == "__main__":
    root = tk.Tk()
    game = CumsterCumbat(root)
    root.mainloop()
