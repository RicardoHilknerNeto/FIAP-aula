frutas = ["maçã", "uva", "kiwi"]
frutas[1] = "manga"
print(frutas)

frutas[1:3] = ["manga", "caqui"]
print(frutas)

frutas.insert(1, "banana")
print(frutas)

citricos = ["limão", "laranja"]
frutas.extend(citricos)
print(frutas)

frutas.remove("caqui")
print(frutas)

frutas.pop(2)
print(frutas)

for i in frutas :
    print (i)

for i in range(0, len(frutas), 1):
    print(frutas[i])