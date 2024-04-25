from line_text import LineText
from binary_tree import BinaryTree


text = []
text1 = "un condenado a muerte con su cuaderno esperando algo que lo salve del suplicio eterno "
text2 = "Abrí la jaula y me olvidé de cómo ser libre "
text3 = "Pasando del remordimiento del hecho pasado "
text4 = "Ya no se esconde "
text5 = "Se vuelve tan asoroso aquello que nos calma "
text6 = "Mi corazón gritando como si nada me pasara posando "
text7 = "y no saber si vuelven "
text8 = "Sigo en еspirales que no diferencian dolor de placer "
text9 = "Estoy en el fondo de todo aca la luz no llega todo quema "
text10 = "Me gusta todo lo que sos y un poco más el barrio quedo sin luz cuando no estas "

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

arbol = BinaryTree()
for i in text:
    arbol.insertar(i.data, str(i.procedencia))

arbol.Preorder()
