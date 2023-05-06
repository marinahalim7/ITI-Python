import math
# 1
def findIndex(word,letter):
    mylist = []
    for index,ch in enumerate(word):
      #  print(index)
        if (ch==letter):
            mylist.append(index)
    return mylist
#print(findIndex("This is JavaScript",'i'))

###############################
#2
def printMultyplyTable(number):
    bigList=[]
    for x in range(1,number+1):
        smallList = []
        for y in range(1,x+1):
            smallList.append(x*y)
        bigList.append(smallList)

    return bigList
#print(printMultyplyTable(5))
#################################
#3
def convertToDic(names):
   n=names.replace('[',"").replace(']',"")
   print(n)
   namesDict={}
   for i in names:
        namesDict[i[0].lower()]=[i]
   return  namesDict

names='["ahmed", "fatma", "Ibrahim"]'
print(convertToDic(names))
################
def calArea(type,x,y=0):
    if(type=='t'):
        return(0.5*x*y)
    elif(type=='r'):
        return (x*y)
    elif (type == 's'):
        return (x * x)
    elif (type == 'c'):
        return( math.pi * x ** 2)
    else:
        return "Not found"
#print(calArea('s',5))





