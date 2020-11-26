import random


# Aufgabe 1.a #
def is_integer_matrix(M):
    k = len(M[0])
    for m in M:
        if len(m) != k:
            return False
        for n in m:
            if int(n) != n:
                return False
    return True


matrix = [[1, 3, 5], [2, 4, 6]]
print(is_integer_matrix(matrix))


# Aufgabe 1.b #
def generate_matrix(k, l, i, j):
    if (k < 0) or (l < 0):
        exit("Eine positive Ganzzahl fuer die Zeile und Spalte eingeben!")
    if i <= j:
        g_matrix = [[random.randint(i, j) for row in range(k)] for column in range(l)]
        return g_matrix
    else:
        g_matrix = [[random.randint(j, i) for row in range(k)] for column in range(l)]
        return g_matrix


row = int(input("Gib eine Ganzzahl fuer die Zeile ein: "))
column = int(input("Gib eine weitere Ganzzahl fuer die Spalte ein: "))
first_number = int(input("Eine zufaellige Zahl eingeben: "))
second_number = int(input("Eine weitere zufaellige Zahl eingeben: "))

print(generate_matrix(row, column, first_number, second_number))


