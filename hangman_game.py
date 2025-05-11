import  random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculation_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def comparison (user_score, computer_score):

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
   

    user_card = []
    computer_card = []
    user_score = -1
    computer_score = -1
    game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_over:
        user_score = calculation_score(user_card)
        computer_score = calculation_score(computer_card)
        print(f"Your cards {user_card}, your score {user_score}")
        print(f"Computer Fist cards {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 :
            game_over = True
        else:
            use_deal_card = input("Type 'y' to select the other cards or 'n' to pass  ")
            if use_deal_card == "y":
                user_card.append(deal_card())
                #user_score = calculation_score(user_card)
            else:
                game_over = True

    while computer_score !=0 and computer_score < 17 :
        computer_card.append(deal_card())
        computer_score = calculation_score(computer_card)

    print(f"Your Final cards {user_card},Your final score :{user_score}")
    print(f"Computer cards {computer_card}, Computer Final Score {computer_score} ")
    print(comparison(user_score,computer_score))

while input("Do You want play the Blackjack Type 'y' or 'no' ") == "y":
    print("\n"*25)
    play_game()



