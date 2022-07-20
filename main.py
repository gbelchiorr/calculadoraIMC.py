altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso : '))

IMC = peso / (altura/100)**2

print(IMC)

if IMC < 18.5: 
    print(f'Seu IMC é de {IMC}, e é classificado como Magreza ')

elif IMC < 24.9: 
    print(f'Seu IMC é de {IMC} e é classificado como Normal ')

elif IMC < 29.9: 
    print(f'Seu IMC é de {IMC} e é classificado como Sobrepeso ')

elif IMC < 39.9: 
    print(f'Seu IMC é de {IMC} e é classificado como Obesidade')

else:  
    print(f'Pode parar de comer e começar a malhar pois o negócio está feio! Você é classificado como Obesidade Grave')