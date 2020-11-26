# Aufgabe 2.a #
def find_pos(char, zeichenkette):
    if char in zeichenkette:
        return zeichenkette.find(char)
    else:
        return -1

# zeichenkette = input("Geben Sie eine Zeichenkette ein: ")
# char = input("Geben Sie ein Zeichen ein: ")
# print(find_pos(char, zeichenkette))


# Aufgabe 2.b #
f = open('de_DE_frami.dic', 'r')
f_read = f.readlines()

d = open('dictionary.txt', 'w')
slash = "/"


for i, file in enumerate(f_read):
    if (file[0] == "#") or (file == "\n") or (file == "\t\n"):
        pass
    else:
        found = find_pos(slash, file)
        if i >= (len(f_read)-1):
            d.write(file[:found])
        else:
            d.write(file[:found] + "\n")

f.close()
d.close()
