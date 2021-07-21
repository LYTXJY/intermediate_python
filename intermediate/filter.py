number_list = range(-5, 5)

less_than_zero = filter(lambda x : x < 0, number_list)

print(list(less_than_zero))


list_need = []
for x in range(-5, 5):
    list_need.append( x * x)

print(list_need)

list_need_ger = [x * x for x in range(-5, 5) ]
print(list_need_ger)

a = [x for x in range(1, 11) if x % 2 == 0]
print(a)

b = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(b)