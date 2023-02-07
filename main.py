def new_game():
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game == "y":
            blackjack()
    else:
        exit()
def blackjack():
    import random
    import art
    print(art.logo)
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    def deal_card():
        card = random.choice(cards)
        return card
    
    
    user_cards = []
    computer_cards = []
    continuar = []

    
    def calculate_score(cards):
        score = sum(cards)
        if score == 21:
            return 0
        elif 11 in cards and score > 21:
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
            return score
        return score
    def calculate(): 
        calculate_score(user_cards)
        calculate_score(computer_cards)
        if calculate_score(computer_cards) == 0 or calculate_score(user_cards) > 21:
            print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
            print("You lose")
            new_game()
        if calculate_score(user_cards) == 0 or calculate_score(computer_cards) > 21:
            print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
            print("You win")
            new_game()
        
    
    def player_playing():
        continuar = input("Type 'y' to get another card, type 'n' to pass: ")
        while continuar == 'y':
            user_cards.append(deal_card())
            calculate()
            print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
            print(f"Computer's cards: {calculate_score(computer_cards)}")
            continuar = input("Type 'y' to get another card, type 'n' to pass: ")
    def computer_playing():
        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())
            calculate()
        
    
    
    def compare():
        print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
        if calculate_score(computer_cards) == calculate_score(user_cards):
            print("Draw")
        elif calculate_score(computer_cards) > calculate_score(user_cards):
            print("You lose")
        elif calculate_score(computer_cards) < calculate_score(user_cards):
            print("You win")
    
    def initial_deal():
        user_cards.append(deal_card()), user_cards.append(deal_card())
        computer_cards.append(deal_card())
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards}")

    
    initial_deal()
    
    player_playing()
    
    computer_playing()
    
    compare()
    if input("Play another game?: Type 'y'") == "y":
        blackjack()

new_game()
blackjack()