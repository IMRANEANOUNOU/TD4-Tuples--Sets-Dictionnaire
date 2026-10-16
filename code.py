from collections import Counter
from random import sample


def occurences(lettre, mot):
    return Counter(mot.lower())[lettre.lower()]


scrabble = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 10,
    "l": 1,
    "m": 2,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 8,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 10,
    "x": 10,
    "y": 10,
    "z": 10,
}


def score_mot(mot):
    return sum(scrabble[lettre] for lettre in mot.lower())


jetons = {
    "a": 9,
    "b": 2,
    "c": 2,
    "d": 3,
    "e": 15,
    "f": 2,
    "g": 2,
    "h": 2,
    "i": 8,
    "j": 1,
    "k": 1,
    "l": 5,
    "m": 3,
    "n": 6,
    "o": 6,
    "p": 2,
    "q": 1,
    "r": 6,
    "s": 6,
    "t": 6,
    "u": 6,
    "v": 2,
    "w": 1,
    "x": 1,
    "y": 1,
    "z": 1,
}

# question de la partie 3 :
# 1 . le script remplie une list par
# les key de dic jetons multiplier par chaque value

# 2 . from random import randint

L_jetons = []

for lettre in jetons:
    L_jetons += [lettre] * jetons[lettre]


def poiche():
    return dict(Counter(sample(L_jetons, 7)))


def possible(mot, lettres):
    mot = Counter(mot.lower())
    return all(mot[lettre] <= lettres.get(lettre, 0) for lettre in mot)


print(occurences("o", "bonjour"))
print(score_mot("said"))
print(poiche())
print(possible("maman", {"m": 2, "a": 2, "n": 1}))
print(possible("baton", {"m": 2, "a": 2, "n": 1, "t": 1}))
