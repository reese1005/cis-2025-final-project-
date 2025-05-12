<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
import random
import os

# Define constants for suits and values
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

# Deck class to handle card deck operations
class Deck:
    def __init__(self):
        self.cards = [(value, suit) for value in VALUES for suit in SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

    def reshuffle(self):
        self.__init__()

# Player class to handle player's bank and actions
class Player:
    def __init__(self, name, bank=100):
        self.name = name
        self.bank = bank
        self.bet = 0

    def adjust_bank(self, amount):
        self.bank += amount

    def set_bet(self, amount):
        self.bet = amount

    def reset_bet(self):
        self.bet = 0

# Hand evaluation functions
def evaluate_hand(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    value_counts = {value: values.count(value) for value in set(values)}
    suit_counts = {suit: suits.count(suit) for suit in set(suits)}

    is_flush = len(suit_counts) == 1
    sorted_values = sorted([VALUES.index(value) for value in values])
    is_straight = sorted_values == list(range(min(sorted_values), max(sorted_values) + 1))

    if is_flush and is_straight and 'Ace' in values and 'King' in values:
        return 'Royal Flush', 2000
    if is_flush and is_straight:
        return 'Straight Flush', 250
    if 4 in value_counts.values():
        return 'Four of a Kind', 125
    if 3 in value_counts.values() and 2 in value_counts.values():
        return 'Full House', 40
    if is_flush:
        return 'Flush', 25
    if is_straight:
        return 'Straight', 20
    if 3 in value_counts.values():
        return 'Three of a Kind', 15
    if list(value_counts.values()).count(2) == 2:
        return 'Two Pair', 10
    if 2 in value_counts.values() and any(value in ['Jack', 'Queen', 'King', 'Ace'] for value in value_counts if value_counts[value] == 2):
        return 'Pair of Jacks or Better', 5
    return 'No Win', 0

# Game class to handle the main game logic
class VideoPokerGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Video Poker')
        self.deck = Deck()
        self.player = None
        self.hand = []
        self.buttons = {}
        self.setup_ui()

    def setup_ui(self):
        self.name_entry_button = tk.Button(self.root, text="Enter Name", command=self.ask_name)
        self.name_entry_button.pack()

        self.bet_button = tk.Button(self.root, text="Bet One Coin", command=self.bet_one)
        self.bet_button.pack()

        self.deal_button = tk.Button(self.root, text="Deal", command=self.deal_hand)
        self.deal_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_game)
        self.exit_button.pack()

    def ask_name(self):
        name = simpledialog.askstring("Player Name", "Enter your name:")
        if name:
            self.player = Player(name)
            self.name_entry_button.config(state='disabled')
            self.create_bet_ui()

    def create_bet_ui(self):
        self.bet_label = tk.Label(self.root, text=f"Bank: {self.player.bank} coins")
        self.bet_label.pack()

        self.bet_amount_button = tk.Button(self.root, text="Place Bet", command=self.place_bet)
        self.bet_amount_button.pack()

    def place_bet(self):
        bet_amount = simpledialog.askinteger("Place Bet", "How many coins would you like to bet? (1-50)", minvalue=1, maxvalue=50)
        if bet_amount and bet_amount <= self.player.bank:
            self.player.set_bet(bet_amount)
            self.update_bank()
            self.deal_hand()

    def deal_hand(self):
        self.hand = [self.deck.deal_card() for _ in range(5)]
        self.display_hand()
        self.show_hand_value()

    def display_hand(self):
        for index, card in enumerate(self.hand):
            card_label = tk.Label(self.root, text=f"{card[0]} of {card[1]}")
            card_label.grid(row=1, column=index)
            self.buttons[index] = tk.Button(self.root, text="Keep", command=lambda i=index: self.toggle_discard(i))
            self.buttons[index].grid(row=2, column=index)

    def toggle_discard(self, index):
        card = self.hand[index]
        if self.buttons[index].cget("text") == "Keep":
            self.buttons[index].config(text="Discard")
        else:
            self.buttons[index].config(text="Keep")
        self.hand[index] = None

    def show_hand_value(self):
        hand_name, payout = evaluate_hand(self.hand)
        result_text = f"Hand: {hand_name}, Payout: {payout} coins"
        result_label = tk.Label(self.root, text=result_text)
        result_label.pack()

    def update_bank(self):
        self.bet_label.config(text=f"Bank: {self.player.bank} coins")
    
    def exit_game(self):
        if self.player:
            self.player.adjust_bank(-self.player.bet)
            with open(f"{self.player.name}.txt", "w") as file:
                file.write(str(self.player.bank))
        self.root.quit()

if __name__ == "__main__":
    import tkinter.simpledialog as simpledialog
    root = tk.Tk()
    game = VideoPokerGame(root)
    root.mainloop()
=======
import tkinter as tk
from tkinter import messagebox
import random
import os

# Define constants for suits and values
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

# Deck class to handle card deck operations
class Deck:
    def __init__(self):
        self.cards = [(value, suit) for value in VALUES for suit in SUITS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

    def reshuffle(self):
        self.__init__()

# Player class to handle player's bank and actions
class Player:
    def __init__(self, name, bank=100):
        self.name = name
        self.bank = bank
        self.bet = 0

    def adjust_bank(self, amount):
        self.bank += amount

    def set_bet(self, amount):
        self.bet = amount

    def reset_bet(self):
        self.bet = 0

# Hand evaluation functions
def evaluate_hand(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    value_counts = {value: values.count(value) for value in set(values)}
    suit_counts = {suit: suits.count(suit) for suit in set(suits)}

    is_flush = len(suit_counts) == 1
    sorted_values = sorted([VALUES.index(value) for value in values])
    is_straight = sorted_values == list(range(min(sorted_values), max(sorted_values) + 1))

    if is_flush and is_straight and 'Ace' in values and 'King' in values:
        return 'Royal Flush', 2000
    if is_flush and is_straight:
        return 'Straight Flush', 250
    if 4 in value_counts.values():
        return 'Four of a Kind', 125
    if 3 in value_counts.values() and 2 in value_counts.values():
        return 'Full House', 40
    if is_flush:
        return 'Flush', 25
    if is_straight:
        return 'Straight', 20
    if 3 in value_counts.values():
        return 'Three of a Kind', 15
    if list(value_counts.values()).count(2) == 2:
        return 'Two Pair', 10
    if 2 in value_counts.values() and any(value in ['Jack', 'Queen', 'King', 'Ace'] for value in value_counts if value_counts[value] == 2):
        return 'Pair of Jacks or Better', 5
    return 'No Win', 0

# Game class to handle the main game logic
class VideoPokerGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Video Poker')
        self.deck = Deck()
        self.player = None
        self.hand = []
        self.buttons = {}
        self.setup_ui()

    def setup_ui(self):
        self.name_entry_button = tk.Button(self.root, text="Enter Name", command=self.ask_name)
        self.name_entry_button.pack()

        self.bet_button = tk.Button(self.root, text="Bet One Coin", command=self.bet_one)
        self.bet_button.pack()

        self.deal_button = tk.Button(self.root, text="Deal", command=self.deal_hand)
        self.deal_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_game)
        self.exit_button.pack()

    def ask_name(self):
        name = simpledialog.askstring("Player Name", "Enter your name:")
        if name:
            self.player = Player(name)
            self.name_entry_button.config(state='disabled')
            self.create_bet_ui()

    def create_bet_ui(self):
        self.bet_label = tk.Label(self.root, text=f"Bank: {self.player.bank} coins")
        self.bet_label.pack()

        self.bet_amount_button = tk.Button(self.root, text="Place Bet", command=self.place_bet)
        self.bet_amount_button.pack()

    def place_bet(self):
        bet_amount = simpledialog.askinteger("Place Bet", "How many coins would you like to bet? (1-50)", minvalue=1, maxvalue=50)
        if bet_amount and bet_amount <= self.player.bank:
            self.player.set_bet(bet_amount)
            self.update_bank()
            self.deal_hand()

    def deal_hand(self):
        self.hand = [self.deck.deal_card() for _ in range(5)]
        self.display_hand()
        self.show_hand_value()

    def display_hand(self):
        for index, card in enumerate(self.hand):
            card_label = tk.Label(self.root, text=f"{card[0]} of {card[1]}")
            card_label.grid(row=1, column=index)
            self.buttons[index] = tk.Button(self.root, text="Keep", command=lambda i=index: self.toggle_discard(i))
            self.buttons[index].grid(row=2, column=index)

    def toggle_discard(self, index):
        card = self.hand[index]
        if self.buttons[index].cget("text") == "Keep":
            self.buttons[index].config(text="Discard")
        else:
            self.buttons[index].config(text="Keep")
        self.hand[index] = None

    def show_hand_value(self):
        hand_name, payout = evaluate_hand(self.hand)
        result_text = f"Hand: {hand_name}, Payout: {payout} coins"
        result_label = tk.Label(self.root, text=result_text)
        result_label.pack()

    def update_bank(self):
        self.bet_label.config(text=f"Bank: {self.player.bank} coins")
    
    def exit_game(self):
        if self.player:
            self.player.adjust_bank(-self.player.bet)
            with open(f"{self.player.name}.txt", "w") as file:
                file.write(str(self.player.bank))
        self.root.quit()

if __name__ == "__main__":
    import tkinter.simpledialog as simpledialog
    root = tk.Tk()
    game = VideoPokerGame(root)
    root.mainloop()
>>>>>>> c1e1f30904da74523f73e02fc5c6687467f17971
