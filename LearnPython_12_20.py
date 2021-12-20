l=[i for i in range(1,10)]
print(l)

score={'张三':100,'李四':20}
print(score)

adult=dict(name='liningqian',age='100')
print(adult)

print(adult['name'])



for item in score:
    print(item,score[item],score.get(item))


item=['Fruits','Books','Others']
prices=[96,78,85]
lst=zip(item,prices)
print(list(lst))

d={item:prices for item,prices in zip(item,prices)}

lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))


tup1=tuple('hello')

list1=['Python','Java']
tup2=tuple(list1)

l=(10,[20,30],9)
print(tup1)
print(tup2)

a=('Python','J',2,[100,20])
print(a)
for item in a:
    print(item)







