#Zip element of two lists
s1 = {2,3,1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3,"\n")


#Zip element of two lists
# print elements one by one, but elements of 2nd list will be in reverse order
list1 = [10, 20, 30,40]
list2 = [100,200,300,400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)


#Zip into dictonary
stocks = ['reliance', 'infosys', 'tcs']

prices = [2175, 1127, 2750]

new_dict = {stock: price for stock, price in zip(stocks, prices)}