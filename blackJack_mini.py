import random

cards_deck =[11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#get a card:
def get_a_card(cards_deck):
    card = random.choice(cards_deck)
    return card

def calc_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    
    #check for 11
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    
    return sum(hand)

def compare_scores(players_score, dealers_score):
    #a bunch of camparisons:
    if players_score == dealers_score:
        return "It's a draw!"
    elif dealers_score == 0:
        return "Dealer is having Black Jack!"
    elif players_score == 0:
        return "Player is having Black Jack!"
    elif players_score > 21:
        return "Player is over! Dealer wins"
    elif dealers_score > 21:
        return "Dealer is over - Player wins!"
    elif players_score > dealers_score:
        return "Player wins!"
    else: 
        return "Dealer won!"


def playgame():
    #* * * * G A M E P L A Y * * * *
    players_hand = []
    players_score = 0

    dealers_hand = []
    dealers_score = 0

    is_game_over = False

    counter = 0


    #init of the game:
    for _ in range(2):
        players_hand.append(get_a_card(cards_deck))
        dealers_hand.append(get_a_card(cards_deck))


    while not is_game_over:

        players_score = calc_score(players_hand)
        dealers_score = calc_score(dealers_hand)

        #test:
        print(f"Player's Hand: {players_hand}: {players_score}\n Dealer's Hand: {dealers_hand[0]}")

        if players_score == 0 or dealers_score == 0 or players_score > 21:
            is_game_over = True
        else:
            #ask user for one more card:
            ask_user = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if ask_user == "y":
                players_hand.append(get_a_card(cards_deck))
                players_score = calc_score(players_hand)
                print(players_hand, players_score)
            else: 
                is_game_over = True

    #dealer's turn:
    while dealers_score != 0 and dealers_score < 17 and players_score <= 21:
        print("Dealer is getting a card")
        dealers_hand.append(get_a_card(cards_deck))
        dealers_score = calc_score(dealers_hand)
        print(dealers_hand, dealers_score)


    #check who won:
    print(compare_scores(players_score, dealers_score))

while input ("Do want to play a round? of Black Jack? Y/N: ").lower() == "y":
    print("\n" * 220)
    playgame()