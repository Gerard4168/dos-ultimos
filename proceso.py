# Los dos ultimos digitos son iguales?

print("----------------------------------------------------")
print("---------Digite un numero de minimo 2 cifras--------")
print("----------------------------------------------------")

#input
u= int(input("Digite el valor de u: "))

#procesing

de= u//10%10
mod= u%10
x = de
y = mod

#output
if u<11:
    print(" no cumple con la condicion")
else:
 if x == y:

    print(" sus dos ultimos digitos son iguales")

 else:

    print(" sus dos ultimos digitos son diferentes")




