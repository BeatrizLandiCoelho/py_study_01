#_______________________COLECTIONS____________________________________________#
#listas com varios dados
family = ["caio","camila","giovanna","lucca","cleo","david"]

print(family[3:5])

#add more registers
family.extend(["vitor","victor"])
print(family)

# add a single register
family.append("albedo")
print(family)

#insert a item in  any position 
family.insert(8,"akaza")
print(family)

#remove last item of an colection
family.pop()
print(family)

#remove an especific item of an collection
family.remove("victor")
print(family)

#print an specif index
print(family.index("akaza"))

#cont how many itens have with the name
print(family.count("cleo"))

#clear the collection
#family.clear()
print(family)

#___________________________AGE_______________________________________

age_family =[19,18,19,6,19,36,20,22]
print(age_family)

#put in the order min to max if is a string by alfabetic order
age_family.sort()
family.sort()

print(age_family)
print(family)

#put in the order but in reverse {to reverse aways put in order}
age_family.reverse()
print(age_family)

#copy a list by making a reference for an actual variable
family2 = family
print(family2)
family2.remove("akaza")
print(family)

#in fact make a copy of a collection
family3 = family.copy()
print(family3)
family.remove("vitor")
print(family)
print(family3)

#changes an indice
family[0] = "Caio"
print(family)
