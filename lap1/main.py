# 1
number=int(input("Enter Number : "))
for i in range(1,number+1):
    print(" "*(number-i),"*"*i)

#2

def removeVoles(*words):
    voles = "aeiouAEIOU"
    newWord=""
    for word in words:
        for i in word:
            if i not in voles:
                newWord = newWord + i
        print(newWord)
        newWord=""

removeVoles("marina","halim")


