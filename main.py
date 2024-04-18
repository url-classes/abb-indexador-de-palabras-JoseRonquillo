from line_text import LineText


text = []
text1 = "Soy un condenado a muerte con su cuaderno esperando algo que lo salve del suplicio eterno "
text2 = "Abrí la jaula y me olvidé de cómo ser libre "
text3 = "Pasando del remordimiento de un hecho pasado "
text4 = "Ya no se esconde el norte cuando encuentra tu mirada "
text5 = "Se vuelve tan valioso el beso de la calma "
text6 = "Mi corazón gritando va cruzando la frontera "
text7 = "Y no saber si vuelven en su compañía "
text8 = "Sigo en еspirales que no diferencian dolor de placer "
text9 = "Estoy en el fondo de todo, acá la luz no llega "
text10 = "Me gusta todo lo que sos, y un poco más "

vec_text = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10]

result = ""
procedencia = 1
for x in vec_text:
    for i in x:
        if i != " ":
            result += i
        else:
            text.append(LineText(result, procedencia))
            result = ""
    procedencia += 1

for i in text:
    print(i.data)

