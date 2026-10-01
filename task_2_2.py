import random
deck = [f"{v}{s}" for s in " ♠♥♦♣" for v in "6789TJQKA"]
random.seed(7)
print("Всего карт в калоде:", len(deck))

hand = random.sample(deck, 5)
print("Рука игрока(sample):", len(hand))

print("Карта дня (choice):", random.choice(deck))

weights = {"обычная": 70, "редкая": 25, "легендарная": 5}
loot = random.choices(list(weights),weights=list(weights.values()),k=5)
print("Лут (choice, 5 шт.):", loot)
random.shuffle(deck)
print("После shuffle:", deck[:6],"...")
print("\n--- Раздача 3 игракам по 5 карт ---")
players = ["Алиса", "Борис", "Вера"]
pool = deck.copy()
for p in players:
    hand = random.sample(pool, 5)
    print(f"{p:6s}: {hand}")
    for card in hand:
        pool.remove(card)