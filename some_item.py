import random


some_items =["Milk", "eggs", "butter","salt"]
print("originals:",some_items)

random.shuffle(some_items)
print("items after shuffling:",some_items)

result_4 = random.choice(some_items)
print("choosen item is:",result_4)
