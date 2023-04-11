import random
from characters import numbers, lowerCases, upperCases, specialCharacters


def passwordGenerator(
    charaterCount=8,
    lowerCase=True,
    upperCase=True,
    number=True,
    specialCharacter=True,
):
    characters = []
    password = ""
    match lowerCase:
        case True:
            for character in lowerCases:
                characters.append(character)
    match upperCase:
        case True:
            for character in upperCases:
                characters.append(character)
    match number:
        case True:
            for character in numbers:
                characters.append(character)
    match specialCharacter:
        case True:
            for character in specialCharacters:
                characters.append(character)

    while charaterCount != 0:
        password = password + random.choice(characters)
        charaterCount -= 1

    return password
