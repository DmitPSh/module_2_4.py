

list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []


for i in range(2,len(list)):
     print('list [',i,']=',list[i])
     for j in range(1, len(list)):
          if list[i] % list[j] != 0:
               print('number', list[i],  '= prime')
               prime.append(list[i])
               break


          else:
               print('number', list[i],  '= not_prime')
               not_prime.append(list[i])
               break

print(not_prime)
print(prime)

