f = open("resultatsXifratsMcopy1.txt","r")

valorsXifrats = []
count = 0

valorsXifratsDic = {}

maxfreq = 0
valuefreq = 0

for x in f:
    value = x.split(' ', 1)[0].strip()
    valorsXifrats.append(value)
    valueInt = int(value, 16)
    finalxor = valueInt ^ (count+2)
    count = count+1

    if finalxor in valorsXifratsDic:
        valorsXifratsDic[finalxor]+=1
    else:
        valorsXifratsDic[finalxor] = 1

for x, y in valorsXifratsDic.items():
    if y > maxfreq:
        maxfreq = y 
        valuefreq = x
    #print(x,y)

print(chr(valuefreq),maxfreq)
#print(valuefreq,maxfreq)

f.close()

#busquem el primer valor de la clau k[0]
f2 = open("resultatsXifrats2Mcopy1.txt","r")
count2 = 0
valorsXifratsDic2 = {}

maxfreq2 = 0
valuefreq2 = 0

for x in f2:
    value = x.split(' ', 1)[0].strip()
    valueInt = int(value, 16)

    valuek = 0
    for x in range(256):
        finalxor = valuefreq ^ (count2+6+x)
        if finalxor == valueInt:
            valuek = x
            if x in valorsXifratsDic2:
                valorsXifratsDic2[x]+=1
            else:
                valorsXifratsDic2[x] = 1

    count2 = count2+1

for x, y in valorsXifratsDic2.items():
    if y > maxfreq2:
        maxfreq2 = y 
        valuefreq2 = x
    #print(x,y)

print(hex(valuefreq2),maxfreq2)

f2.close()

#busquem el segon valor de la clau k[1]
f3 = open("resultatsXifrats3Mcopy1.txt","r")
count3 = 0
valorsXifratsDic3 = {}

maxfreq3 = 0
valuefreq3 = 0

for x in f3:
    value = x.split(' ', 1)[0].strip()
    valueInt = int(value, 16)

    valuek = 0
    for x in range(256):
        finalxor = valuefreq ^ (count3+10+valuefreq2+x)

        if finalxor == valueInt:
            valuek = x
            if x in valorsXifratsDic3:
                valorsXifratsDic3[x]+=1
            else:
                valorsXifratsDic3[x] = 1

    count3 = count3+1

for x, y in valorsXifratsDic3.items():
    if y > maxfreq3:
        maxfreq3 = y 
        valuefreq3 = x
    #print(x,y)

print(hex(valuefreq3),maxfreq3)

f3.close()