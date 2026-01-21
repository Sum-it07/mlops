string=input()
# vowel=["a","e","i","o","u"]
li=[]
for i in string:
    if i not in li:
        li.append(i)
length=len(li)
if(length%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
