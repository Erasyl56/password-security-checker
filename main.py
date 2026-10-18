
password = input("Құпиясөзді енгізіңіз: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(not char.isalnum() for char in password):
    score += 1

print("\n--- Тексеру нәтижесі ---")
print("Құпиясөз ұзындығы:", len(password))

if score <= 2:
    print("Қауіпсіздік деңгейі: Әлсіз")
elif score <= 4:
    print("Қауіпсіздік деңгейі: Орташа")
else:
    print("Қауіпсіздік деңгейі: Күшті")

print("Жиналған ұпай:", score, "/ 5")

