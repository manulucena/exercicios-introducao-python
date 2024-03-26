salario = float (input("Informe o salário de João:"))
valor_conta1_sem_multa = float (input("Informe o valor da conta 1:"))
valor_conta2_sem_multa = float (input("Informe o valor da conta 2:"))

valor_conta1_com_multa = valor_conta1_sem_multa + (valor_conta1_sem_multa * 2/100)
valor_conta2_com_multa = valor_conta2_sem_multa + (valor_conta2_sem_multa * 2/100)

salario_final = salario - (valor_conta1_com_multa + valor_conta2_com_multa)

print("Valor da Conta 1 com multa:", valor_conta1_com_multa)
print("Valor da Conta 2 com multa:", valor_conta2_com_multa)
print("O que restou do salário de João foi:", salario_final)



