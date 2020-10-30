from sys import argv

script, date, time = argv

print("Welcome to Aventura!")

name = input("Whats is your name? ")
age = int(input("How old are you? "))
health = 100


def ver_age(user_age):
    if user_age > 13:
        return "Welcome, lets begin!"
    else:
        return "You are not old enough to play....."


print(f"Hello {name}, welcome to Aventura, a test-based adventure game.")
print(ver_age(age))
print(f"Your Starting health is {health}.")

weapon_cho = input("What weapon would you like?" ).lower()
user_cho = input("Let's start first with Left or Right? (left/right) ").lower()

if user_cho == "left" and weapon_cho:
    print("Croton Village")
    health -= 10
    user_cho = "Croton Village"
    print("As you begin to walk Westworld you begin to notice.....")

elif user_cho == "right" and weapon_cho:
    print("High Peak Valley")
    health += 30
    user_cho = "High Peak Valley"
    print("As you begin to walk Eastwood you begin to notice.....")

elif user_cho == "up" and weapon_cho:
    print("Endless Hills")
    health -= 50
    user_cho = "Endless Hills"
    print("As you begin to walk Northwood you begin to notice.....")

elif user_cho == "down" and weapon_cho:
    print("Dragon Raveen")
    health -= 70
    user_cho = "Dragon Raveen"
    print("As you begin to walk Southworld you begin to notice.....")
    
else:
    print("You Picked None.......")
    health -= 100
    print("As you begin to walk.......")

if health == 0:
    print("You've lost all you health..... GAME OVER!!!")

ans = input("Would you like to check on your health? ")
if ans == "yes":
    print(f"Your health is {health}...")

print(f"""As you arrive to {user_cho}, you notice a lone martial artist. 
\nAs you approach the lone warrior.""")
print("His name is Lue Zeng.")

convo_lst = ["Whats your martial arts level?", "STOP HIM HE STOLE MY WALLET!!!", "Welcome to the heavenly reaching arena."]
#convo_resp = [{} {} {} {} {} {}]

def convo(name, user_cho):
    for convos in convo_lst:
        print(f"Hey {name}, Welcome to {convos}")

print(convo(name, user_cho))


