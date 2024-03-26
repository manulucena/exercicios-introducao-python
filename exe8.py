horas_trabalhadas = float(input("Informe o número de horas trabalhadas:"))
salario_minimo = float(input("Informe o valor do salário mínimo:"))
horas_extras = float(input("Informe o número de horas extras trabalhadas:"))

valor_hora = salario_minimo / 8
valor_hora_extra = salario_minimo / 4
salario_bruto = horas_trabalhadas * valor_hora

valor_horas_extras_a_receber = horas_extras * valor_hora_extra

salario_a_receber = salario_bruto + valor_horas_extras_a_receber

print("Valor hora trabalhada:", valor_hora)
print("Valor hora extra:", valor_hora_extra)
print("Salário bruto:", salario_bruto)
print("Valor horas extras a receber:", valor_horas_extras_a_receber)
print("Salário a receber:", salario_a_receber)


