# -*- coding: utf-8 -*-
"""python_programming_challenge

## Poker Hand

In this challenge, we have to find out which kind of Poker combination is present in a deck of 5 cards.Every card is a string containing the card value (with the upper-case initial for face-cards) and the lower-case initial for suits, as in the examples below:

> "Ah" ➞ Ace of hearts <br>
> "Ks" ➞ King of spades<br>
> "3d" ➞ Three of diamonds<br>
> "Qc" ➞ Queen of clubs <br>

There are 10 different combinations. Here's the list, in decreasing order of importance:

| Name            | Description                                         |
|-----------------|-----------------------------------------------------|
| Royal Flush     | A, K, Q, J, 10, all with the same suit.             |
| Straight Flush  | Five cards in sequence, all with the same suit.     |
| Four of a Kind  | Four cards of the same rank.                        |
| Full House      | Three of a Kind with a Pair.                        |
| Flush           | Any five cards of the same suit, not in sequence    |
| Straight        | Five cards in a sequence, but not of the same suit. |
| Three of a Kind | Three cards of the same rank.                       |
| Two Pair        | Two different Pairs.                                |
| Pair            | Two cards of the same rank.                         |
| High Card       | No other valid combination.                         |

### 1. Given a list `hand` containing five strings being the cards, implement a function `poker_hand_ranking` that returns a string with the name of the **highest** combination obtained, accordingly to the table above.

#### Examples

> poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]) ➞ "Royal Flush"<br>
> poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]) ➞ "High Card"<br>
> poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]) ➞ "Four of a Kind"<br>
"""


def poker_hand_ranking(deck):
                       
    valueMap = {
        "2" : 1,
        "3" : 2,
        "4" : 3,
        "5" : 4,
        "6" : 5,
        "7" : 6,
        "8" : 7,
        "9" : 8,
        "10" : 9,
        "J" : 10,
        "Q" : 11,
        "K" : 12,
        "A" : 13
    }
    
    values = []
    mappedValues = []
    suits = []

    for d in deck:
        values.append(d[:-1])
        mappedValues.append(valueMap.get(d[:-1]))
        suits.append(d[-1])
    
    mappedValues.sort()
    
    firstSuit = suits[0]
    flush = True
    straight = True

    for s in suits:
        if s != firstSuit:
            flush = False
              
    same = 1
    pair = False
    for i in range(len(mappedValues)):    
        if i!= 0:
            if mappedValues[i] != mappedValues[i-1] + 1:
                straight = False        
            
            if mappedValues[i] == mappedValues[i-1]:
                same += 1
            elif same == 2:
                pair = True
                same = 1
        
    if(flush and set(values) == set(("A", "K", "Q", "J", "10"))):
        return "Royal Flush"
    elif(straight and flush):
        return "straight Flush"
    elif same == 4:
        return "Four of a Kind"
    elif pair and same == 3:
        return "Full House"
    elif(flush):
        return "Flush"
    elif(straight):
        return "Straight"
    elif same == 3:
        return "Three of a Kind"
    elif same == 2 and pair:
        return "Two Pair"
    elif same == 2:
        return "Pair"
    else:
        return "High Card"


"""### 2.  Implement a function `winner_is` that returns the winner given a dictionary with different players and their hands. For example:

#### Example

We define dictionary like
```
round_1 = {"John" = ["10h", "Jh", "Qh", "Ah", "Kh"],
        "Peter" = ["3h", "5h", "Qs", "9h", "Ad"]
}
```

Our function returns the name of the winner:
> winner_is(round_1) -> "John"

One table can have up to 10 players.

"""

round_1 = {"John" :["10h", "Jh", "Qh", "Ah", "Kh"],
            "Peter" : ["3h", "5h", "Qs", "9h", "Ad"]}

def winner_is(players):
    
    scoreMap = {
"Royal Flush" : 10,
"Straight Flush"  : 9,
"Four of a Kind" : 8,
"Full House" : 7,
"Flush" : 6,
"Straight" : 5,
"Three of a Kind" : 4,
"Two Pair" : 3,
"Pair" : 2,
"High Card" : 1       
}

    highestScore = 0
    for player, deck in round_1.items():
        score = scoreMap.get(poker_hand_ranking(deck))
        if score > highestScore:
            highestScore = score
            winner = player
    
    return winner
    

"""### Optional: Create a generator that randomly gives 5 cards to every player given a list of player names
#### Example

> distribute_cards(["John","Peter"])  -> round_1 = {"John" = ["10h", "Jh", "Qh", "Ah", "Kh"],
        "Peter" = ["3h", "5h", "Qs", "9h", "Ad"]
}
"""
import random as rand

valueMap = {
        "2" : 1,
        "3" : 2,
        "4" : 3,
        "5" : 4,
        "6" : 5,
        "7" : 6,
        "8" : 7,
        "9" : 8,
        "10" : 9,
        "J" : 10,
        "Q" : 11,
        "K" : 12,
        "A" : 13
    }
valueMapInv = {v: k for k, v in valueMap.items()}
    
suitMap = {
        1: "h",
        2: "s",
        3: "d",
        4: "c"
        }        
 
def distribute_cards(players):

    deck = {}
    
    for player in players:
        cards = []
        for i in range(5):
            randSuit = rand.randint(1, 4)
            randValue = rand.randint(1, 13)
            card = (valueMapInv.get(randValue)) + (suitMap.get(randSuit))
            cards.append(card)
        deck[player] = cards

    return deck



