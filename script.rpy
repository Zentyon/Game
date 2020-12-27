# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define a = Character("Adrien" , who_color="#0035FF" , image="adrien")

define z = Character("Zentyon" , who_color="#A755F0" , imege="zention" )


# El juego comienza aquí.


label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg room with fade

    play music "uno.mp3" fadeout 1.0 fadein 1.0

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show adrien at left

    # Presenta las líneas del diálogo.

    a """hola, y bienvenido

    al parecer mi llamada si funciono"""

    show adrien fear at right
    show zentyon angry with dissolve

    z "ahora que hiciste con..."

    show zentyon

    z "huh?, compañia?"

    show adrien

    a "sip, asi que comportate zt... ejem. bienvenido al Seishi el lugar que separa tu mundo y el nuestro"

label boom:

    scene explotion

    "BOOOM!!" with vpunch

    scene bg static
menu:

    "Que demonios eh descargado?.":
        jump game

    "Quienes son ustedes.":
        jump you

label game:

    a "el peor malweare que jamas haya visto la humanidad owo."

    jump marry

label you:

    a "Ya veras..."

    jump marry

label marry:

    "Solo no preocupes a tu pequeña cabezita, pronto habra respuestas..."

    extend " muy... muy pronto"


label continuacion:

scene bg room

show zentyon

z "uh... listo, volvió la señal, disculpa la interferencia..."

extend "  si, todavía hay inestabilidad en ésta cosa"

show zentyon think

z """ ahora, si nos disculpas, estamos trabajando en este código...

    ...mjm... esto no es ni una alfa... y a este paso...
"""

z @ angry "bueno qué esperabas? sigue clickando o vete al diablo"


z " sabes? mejor vayamos a alcanzar a adwi en casa"

menu:

    "ok?":
        jump home


## window show - shows the window with the default transition, if any.
#pause       # the window is shown during this pause.
#window hide # hides the window.
#pause       # the window is hidden during this pause.

#window show dissolve # shows the window with dissolve.
#pause                # the window is shown during this pause.
#window hide dissolve # hides the window with dissolve.
#pause                # the window is hidden during this pause.
##



label home:

scene bg habitacion  # the window is hidden before the scene change.
with dissolve

play music "dos.mp3" fadeout 1.0 fadein 1.0

pause

window auto show     # Shows the window before it normally would be shown.

show adrien think at right
with dissolve

a explain "asi que...raro la verdad."

a explain "tomando en cuenta nuestro nulo presupuesto no esperes mucho"

a proud "trataremos de crear una historia interesante almenos, vale la pena probar no?"

a shrug "oh como sea la cosa yo que se"

a explain "solo soy escritor y dibujante la verdad no le se a estas cosas del codigo y que se yo"

show zentyon smile at left with dissolve

z " es bueno saber que funciona almenos no? "

z @ think "unos ajustes y podras conectarte por largos periodos de tiempo uwu"

a proud "pronto ok?, no te preocupes, por ahora solo queda esperar"

    # Finaliza el juego:

return
