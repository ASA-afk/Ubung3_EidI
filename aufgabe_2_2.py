# Aufgabe 2.c #
def search_row(search):
    d = open('dictionary.txt', 'r')
    row = 0
    for line in d.readlines():
        row += 1
        if line.find(search) >= 0:
            return row
    return -1


s = input("Suche nach einem Wort: ")
print(search_row(s))
