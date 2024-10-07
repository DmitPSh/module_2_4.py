#
# list_=[12,34,88,21,92,22]
# print(len(list_))
# for i in range(0,len(list_)):
#     print( i, '=',      list_[i])


list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(len(list))
print(list[len(list)-1])

for i in range(2,len(list)):
     print('list [',i,']=',list[i])
     for j in range(1, len(list)):
          if list[i] % list[j] != 0:
               print('number', list[i],  '= prime')
               break


          else:
               print('number', list[i],  '= not_prime')
               break
















         # for i in range(0, 20):
#     print('arr ', '[', i, '] ==' , i + 5 )
#
# for i in range(1, 10):
#     print(' ')
#     for j in range(1, 10):
#         print( i,' ** ', j, ' = ', i**j  )
#
#         # print(f"{i} x {j} = {i * j}")


#
# #numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# numbers = [1, 2, 3, 4, 5, 6]
# print(len(numbers))
#
#
#
#
#
#
#
# # if numbers[4] % numbers[3] != 0:
# #     print('Simple')









