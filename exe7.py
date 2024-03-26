n1 = float(input("Informe a nota 1:"))
p1 = float(input("Informe o peso 1:"))
n2 = float(input("Informe a nota 2:"))
p2 = float(input("Informe o peso 2:"))
n3 = float(input("Informe a nota 3:"))
p3 = float(input("Informe o peso 3:"))

mp = ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)

print("Média ponderada:", mp)
