dia = 1
mes = 30
ano = 365

anos = input ("Informe quantos anos você tem: \n")
anos = int(anos) * ano

meses = input ("Informe os meses: \n")
meses = int(meses) * mes

dias = input ("Informe os dias: \n")
dias = int(dias) * dia

diasTotais = anos + meses + dias


print ("Você viveu um total de ", diasTotais, " dias")