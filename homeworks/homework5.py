from distance import Distance

d1 = Distance(100, 'cm')
d2 = Distance(2, 'm')
d3 = Distance(1, 'km')

print("Объекты:")
print(d1)
print(d2)
print(d3)

sum1 = d1 + d2
print("\nСложение d1 + d2:")
print(sum1)

diff1 = d3 - d2
print("\nВычитание d3 - d2:")
print(diff1)

d4 = Distance(300, 'cm')
sum2 = d1 + d4
print("\nСложение одинаковых мер (cm):")
print(sum2)
