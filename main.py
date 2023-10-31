import os, sys

dirs, charlist = sys.argv, []
dirs.pop(0)

def analize(i) :
    def ch(x) :
        lit, alit = [], []
        with open(x, "rb") as z :
            st = z.read()
            for char in st :
                if char not in lit :
                    lit.append(char)
                else :
                    alit.append(char)
        return(lit, alit)
    for x in dirs :
        charlist.append(ch(x)[i])
    
    files, pers, lower = charlist, [], len(charlist[0])
    files.pop(0)
    if i == 1 :
        files.pop(0)
    for x in charlist:
        if len(x) < lower :
            lower = len(x)
    
    for x in files :
        pers.append(0)
        for y in range(lower) :
            if charlist[0][y] in x :
                pers[len(pers) - 1] += 1
        pers[len(pers) - 1] = pers[len(pers) - 1] * 100 / len(x)

    return pers
if __name__ == "__main__" :
    print(analize(0), analize(1))
