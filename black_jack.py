import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter  # python 2


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    # For each suit, retrieve the image for the cards
    for suit in suits:
        # First the number cards, 1 to 10
        for card in range(1, 11):
            name = "cards\\{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # Next the face cards
        for card in face_cards:
            name = "cards\\{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def _deal_card(frame):
    # Pop the next card off the top of the deck
    next_card = deck.pop(0)

    # Add the image to a Label and display the Label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')  # why next_card has [1] and not [0]

    # Now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all cards in the list.
    # Only one ace can have the value 11, and this will be reduced to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        # If we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False

    return score


def deal_dealer():
    # _deal_card(dealer_card_frame)
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")

    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    #
    # # checking to see whether player already has an ace or not,
    # # -if not, counting the ace as 11
    # if card_value == 1 and not player_ace:
    #     card_value = 11
    #     player_ace = True
    # player_score += card_value
    #
    # # If we would bust, check if there is an ace and convert it's value from 11 to 1
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer Wins!")


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def restart_game():
    global deck
    dealer_hand.clear()
    player_hand.clear()

    for card in dealer_card_frame.winfo_children():
        card.destroy()

    for card in player_card_frame.winfo_children():
        card.destroy()

    deck = list(cards)
    random.shuffle(deck)
    initial_deal()


def play():
    initial_deal()

    main_window.mainloop()


main_window = tkinter.Tk()

# Set up the screen and frames for the dealer and player
main_window.title("Black Jack")
main_window.geometry("640x480")
main_window.config(background="green")

result_text = tkinter.StringVar()

result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# Embedded frame to hold the card images
dealer_card_frame = tkinter.LabelFrame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# Embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

restart_button = tkinter.Button(button_frame, text="New Game", command=restart_game)
restart_button.grid(row=1, column=0, columnspan=2, sticky="ew")

# Load cards
cards = []
load_images(cards)
print(cards)

# Create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# Create the list  to store the dealer's and player's hands
dealer_hand = []
player_hand = []

deal_player()
dealer_hand.append(_deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

if __name__ == "__main__":
    play()
