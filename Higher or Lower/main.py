import random
from graphics import logo, vs, score
#=>bei import mit from ist logo und vs modul-namen aufrufbar!
from game_data import data

""" get some DATA: Funktion nimmt aus der game_data.py Daten entgegen."""
def format_data(data):
    data_name = data["name"]
    data_description = data["description"]
    data_country = data["country"]
    return f"{data_name}, {data_description}, from {data_country}"

def check_answer(follower_data_a, follower_data_b, ask_user):
    if follower_data_a > follower_data_b:
        return ask_user == "a"
    else:
        return ask_user == "b"
print(logo)
count = 0
continue_game = True

"""get Data for A and B"""
data_b = random.choice(data)


while continue_game:
    data_a = data_b
    data_b = random.choice(data)
    while data_a == data_b:
        data_b = random.choice(data)

    #call format_data Funktion and print:
    print("\n")
    print(f"A: {format_data(data_a)}")
    print(vs)
    print(f"B: {format_data(data_b)}")
    #print(f"Follower from A: {data_a[follower_count]}")

    ask_user = input("Who's having more followers? A or B? ").lower()

    while ask_user != "a" and ask_user != "b":
        print("Enter a valid answer: A or B!")
        ask_user = input("Who's having more followers? A or B?").lower()

    #get follower count 
    follower_data_a = (data_a["follower_count"])
    follower_data_b = (data_b["follower_count"])

    #check if user's input is right!
    is_correct = check_answer(follower_data_a, follower_data_b, ask_user)
    if is_correct:
        count += 1
        print(f"You are right: Score : {count}")
    else:
        print(f"Game is over - Final {score}: {count}")
        continue_game = False






