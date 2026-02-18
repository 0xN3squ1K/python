def calculate_love_score(name1, name2):
    name1 = name1.upper()
    name2 = name2.upper()
    combined = name1+name2
    cont1 = 0
    cont2 = 0
    for letter in combined:
        if letter in "TRUE":
            cont1 += 1
        if letter in "LOVE":
            cont2 += 1
    print(f'Love score: {cont1}{cont2}')

name1 = input('Name of the person 1: ')
name2 = input('Name of the person 2: ')
calculate_love_score(name1, name2)
