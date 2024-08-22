print('Cuestionario')
p1=int(input('Primera pregunta ¿Colon descubrio América?, Responda 1 para si y 2 para no '))
if p1 == 1:
    p2=int(input('Segunda pregunta: ¿La independencia de Colombia fue en 1810? Responda 1 para si y 2 para no '))
    if p2== 2:
        p3=int(input("Tercera pregunta: The Door's fue un grupo de rock americano? Responda 1 para si y 2 para no "))
        if p3 == 2:
            print('Señor usuario ha contestado de manera incorrecta la ultima pregunta, fin del cuestionario')
    else:
        print('Señor usuario ha contestado de manera incorrecta la ultima pregunta, fin del cuestionario')
else:
    print('Señor usuario ha contestado de manera incorrecta la ultima pregunta, fin del cuestionario')

if p1 == 1:
    if p2== 2:
        if p3==1:
            print('Señor usuario usted ha ganado')

