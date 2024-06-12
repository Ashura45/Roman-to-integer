def rim_to_integer(rim):
    rim += '0'
    numb = 0
    for i in range(len(rim)):
        if rim[i] == 'C' and rim[i + 1] == 'M':
            numb -= 100
        elif rim[i] == 'M':
            numb += 1000

        elif rim[i] == 'C' and rim[i + 1] == 'D':
            numb -= 100
        elif rim[i] == 'D':
            numb += 500

        elif rim[i] == 'X' and rim[i + 1] == 'C':
            numb -= 10
        elif rim[i] == 'C':
            numb += 100

        elif rim[i] == 'X' and rim[i + 1] == 'L':
            numb -= 10
        elif rim[i] == 'L':
            numb += 50

        elif rim[i] == 'I' and rim[i + 1] == 'X':
            numb -= 1
        elif rim[i] == 'X':
            numb += 10

        elif rim[i] == 'I' and rim[i + 1] == 'V':
            numb -= 1
        elif rim[i] == 'V':
            numb += 5

        elif rim[i] == 'I':
            numb += 1
    return print(numb)


while True:
    print('I = 1; V = 5; X = 10; L = 50; C = 100; D = 500; M = 1000')
    print()
    RIM = input('print rim number or to get out print q: ').upper()
    if RIM == 'Q':
        break
    rim_to_integer(RIM)

