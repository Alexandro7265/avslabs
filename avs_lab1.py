def tri_to_dec(n):
    dec = 0
    for i,w in enumerate(reversed(n)):
        dec += int(w) * (3**i)
    return dec
def dec_to_tri(n):
    tri = ' '
    while (n>0):
        tri += str(n%3)
        n = n//3
    return tri
print(tri_to_dec('120'))
print(dec_to_tri(17))
