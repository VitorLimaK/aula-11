print("---saiba o aumento do seu salário----")
                                                      
salario = float(input("digite o seu salario: ").replace(',','.'))
salari = float(input ("digite a porcentagem recebida: "))

salari =  salari/100

salario = salario * salari + salario
print("O seu novo salario é = R$%.2f"%salario)