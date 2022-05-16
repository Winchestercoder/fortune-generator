import random

lucky_number = random.randint(1, 100)

lucky_words = ["Something great will happen today", "You will surpass all others", "Be thankful for what you have", "When fear hurts you, conquer it and defeat it!"]

lucky_chooser = random.choice(lucky_words)

print(f"{lucky_chooser}. Your Lucky Number: {lucky_number}")