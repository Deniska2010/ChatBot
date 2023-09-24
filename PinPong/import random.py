import random

# Створення колоди з картами
suits = ['Черви', 'Бубни', 'Пики', 'Трефи']
ranks = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# Перемішуємо колоду
random.shuffle(deck)

# Роздаємо карти гравцям
player1_hand = deck[:6]
player2_hand = deck[6:12]

# Головний цикл гри
while len(player1_hand) > 0 and len(player2_hand) > 0:
    print("Карти гравця 1:", player1_hand)
    print("Карти гравця 2:", player2_hand)
    
    # Гравці вибирають карти для відкидання або взяття
    # Додайте власний код для обробки вибору кард
    
    # Симулюємо взяття карти з колоди
    if len(deck) > 0:
        new_card = deck.pop(0)
        if len(player1_hand) <= len(player2_hand):
            player1_hand.append(new_card)
        else:
            player2_hand.append(new_card)
    
# Визначаємо переможця
if len(player1_hand) == 0:
    print("Гравець 1 переміг!")
elif len(player2_hand) == 0:
    print("Гравець 2 переміг!")