#Libraries
import requests
from collections import Counter
#pre-set card rankings
card_rankings = {str(i): i for i in range(2, 11)}
card_rankings.update({"JACK": 11, "QUEEN": 12, "KING": 13, "ACE": 14})

#Congrats:
cgt = "\U0001F389"

#Get a deck and substract deckID
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url).json()
deck_id = response["deck_id"]

#Draw two cards from deck ID
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url).json()

#Print the two drawn cards using a loop
for card in draw_response["cards"]:
    print(f"{card['value']} of {card['suit']}")


#Checking user cards
card_values, card_suits = zip(*[(card['value'], card['suit']) for card in draw_response['cards']])
card_values = list(card_values)
card_suits = list(card_suits)

card_value_counts = Counter(card_values).items()
ranked_values = sorted(card_rankings[value] for value in card_values)

triples = [value for value, count in card_value_counts if count == 3]
pairs = [value for value, count in card_value_counts if count == 2]

#Congratulate if any condition met
if len(set(card_suits)) == 1:
    print(f"{cgt} Congratulations! All cards are of the same suit!")
elif ranked_values == list(range(ranked_values[0], ranked_values[0] + 5)):
    print(f"{cgt} Congratulations! You got a straight!")
if triples:
    print(f"{cgt} Congratulations! You have a triple of {triples}")
if pairs:
    print(f"{cgt} Congratulations! You have a pair of {pairs}")




