a=2
b=3
c=4

if b<a:
    print("é menor")
elif a==b:
    print("é igual")
else:
    print("é maior")

print("è menor") if a < b else print("E maior")

if(a<b) and (b!=c):
    print("Ok")

if(a<b) or (b!=c):
    print("Não")

while(c<10):
    print("Aumentando c")
    c=c+1

minhaLista=["eu","realdo","justino"]

for x in minhaLista:
    print("quem", x)

for x in "realdo":
    print(x)

for x in range(5):
    print(x)

for x in range(2,5):
    print(x)

for x in range(5,50,5):
    print(x)