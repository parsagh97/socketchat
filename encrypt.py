mono = {
    'a':'f',    'b':'g',    'c':'h',    'd':'i',
    'e':'j',    'f':'k',    'g':'l',    'h':'m',
    'i':'n',    'j':'o',    'k':'p',    'l':'q',
    'm':'r',    'n':'s',    'o':'t',    'p':'u',
    'q':'v',    'r':'w',    's':'x',    't':'y',
    'u':'z',    'v':'a',    'w':'b',    'x':'c',
    'y':'d',    'z':'e',    ' ':' ' 
}
rev_mono = {val:key for (key, val) in mono.items()}
def encrypt(inp):
    inp = list(inp)
    for i in range(len(inp)):
        inp[i] = mono[inp[i]]
    out = "".join(str(x) for x in inp)
    return out

def decrypt(inp):
    inp = list(inp)
    for i in range(len(inp)):
        inp[i] = rev_mono[inp[i]]
    out = "".join(str(x) for x in inp)
    return out

