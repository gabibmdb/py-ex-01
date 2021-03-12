valorPago = input ("Informe a quantia paga: R$")
valorPago = float(valorPago)

valorProduto = input ("Informe o valor do produto: R$")
valorProduto = float(valorProduto)

troco = valorPago - valorProduto
troco = round(troco,2)

print ("O troco recebido é: R$" , troco)