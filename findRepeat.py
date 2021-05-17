def complement(s):
    basecomplement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
        "a": "t",
        "t": "a",
        "g": "c",
        "c": "g",
    }
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)


def revcomp(seq):
    return complement(seq)[::-1]


def findIR(Lenth, s: str):
    visited = list()
    res = list()
    for i in range(0, len(s) - Lenth + 1):
        tmp = s[i:i + Lenth]
        tmpIR = revcomp(tmp)

        if tmpIR in visited:

            tmpInfo = list()
            tmpInfo.append(tmpIR)
            tmpInfo.append(tmp)
            tmpInfo.append(Lenth)
            tmpInfo.append(visited.index(tmpIR))
            tmpInfo.append(i)
            res.append(tmpInfo)

        visited.append(tmp)
    return res


def findCR(Lenth, s: str):
    visited = list()
    res = list()
    for i in range(0, len(s) - Lenth + 1):
        tmp = s[i:i + Lenth]
        tmpCR = complement(tmp)

        if tmpCR in visited:
            tmpInfo = list()
            
            tmpInfo.append(tmpCR)
            tmpInfo.append(tmp)
            tmpInfo.append(Lenth)
            tmpInfo.append(visited.index(tmpCR))
            tmpInfo.append(i)
            res.append(tmpInfo)

        visited.append(tmp)
    return res


minlen = 10
maxlen = 25


with open("HSHBBup5000bp.txt") as f1, open("PROMOresult.txt") as f2:
    a = f1.read()
    a = a.replace("\n", "")
    reps = list()
    IR = list()
    CR = list()
    for i in range(minlen, maxlen + 1):
        IR = IR + findIR(Lenth=i, s=a)
        print(i)
    for i in range(minlen, maxlen + 1):
        CR = CR + findCR(Lenth=i, s=a)
        print(i)
    
    f3 = open("IR.txt", "w")
    for item in IR:
        f3.write(item[0])
        f3.write("  IR:  ")
        f3.write(item[1])
        f3.write("  Length:  ")
        f3.write(str(item[2]))
        f3.write("  pos1:  ")
        f3.write(str(item[3]))
        f3.write("  pos2:  ")
        f3.write(str(item[4]))
        f3.write('\n')
    f3.close()
    f3.close()
    

    f3 = open("CR.txt", "w")
    for item in CR:
        f3.write(item[0])
        f3.write("  CR:  ")
        f3.write(item[1])
        f3.write("  Length:  ")
        f3.write(str(item[2]))
        f3.write("  pos1:  ")
        f3.write(str(item[3]))
        f3.write("  pos2:  ")
        f3.write(str(item[4]))
        f3.write('\n')
    f3.close()


