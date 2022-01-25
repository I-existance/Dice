import random

dice_count = int(input("Dice Count "))
dice_sides = int(input("Dice Sides "))
max = dice_count * dice_sides

print(random.randint(dice_count, max))
