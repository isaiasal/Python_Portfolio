baseball = set (['Jodi', 'Maria', 'Mario', 'Alicia'])
basketball = set (['Carlos', 'Maria', 'Carla', 'Juan'])

#Display members of the basball set 
print('The following students are on the basball team:')
for name in baseball:
    print(name)

#Display members of the basball set 
print('The following students are on the basball team:')
for name in basketball:
    print(name)

#Demostrate intersection 
print()
print('the following students are on the basketball team:')
for name in baseball.intersection(basketball):
    print(name)

#Demostrate union 
print()
print('the following students play either baseball or basketball:')

for name in baseball.union(basketball):
    print(name)

#Demostrate differences of basball and basketball 
print()
print('the following students play basball but not basketabll:')
for name in baseball.difference(basketball):
    print(name)

print('the following students play basball but not basketabll:')
for name in basketball.difference(baseball):
    print(name)
   
#Demostrate symetric difference
print()
print('The following students play one sport, but not both:')
for name in basketball.symmetric_difference(basketball):
    print(name)