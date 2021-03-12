aluno = input ("Insira o nome do aluno: \n")
aluno = str(aluno)

nota1 = input("Insira a primeira nota: \n")
nota1 = float(nota1)

nota2 = input("Insira a segunda nota: \n")
nota2 = float(nota2)

nota3 = input("Insira a terceira nota: \n")
nota3 = float(nota3)

media = (nota1 + nota2 + nota3) / 3
media = round(media,1)

print ("A média do aluno ", aluno, " é ", media)

