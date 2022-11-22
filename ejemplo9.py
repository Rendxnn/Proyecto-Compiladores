from collections import deque


def vacia(pila):
    return 1 if not pila else 0


def cima(pila):
    top = pila.pop()
    pila.append(top)
    return top


def desapila(pila):
    top = pila.pop()
    if top == '#':
        pila.append(top)
    return pila


def apila_pal(w, pila):
    for char in w:
        pila.appendleft(char)


def rec_w2wt(ent):
    ent = ent + '#'
    pila = deque([])
    acepta = 1
    i = 0
    while ent[i] != '2' and ent[i] != '#':
        apila_pal(ent[i], pila)
        i += 1
    if ent[i] == '2':
        i += 1
    else:
        acepta = 0
    while vacia(pila) == 0 and cima(pila) == ent[i]:
        desapila(pila)
        i += 1
    if vacia(pila) == 0 or ent[i] != '#':
        acepta = 0
    return acepta


def main():
    print(rec_w2wt(input()))


main()
