pokemon_enemy = input("Contra que pokemon quieres luchar? Squiertle / Charmander / Bulbasaur: ")
vida_pikachu = 100
enemy_live = 0
pokemon_atack = 0
if pokemon_enemy == "Squiertle":
    enemy_live = 80
    pokemon_name= "squiertle"
    pokemon_atack = 8

elif pokemon_enemy == "Charmander":
    enemy_live = 90
    pokemon_name = "Charmander"
    pokemon_atack = 7

elif pokemon_enemy == "Bulbasaur":
    enemy_live = 100
    pokemon_name = "Bulbasaur"
    pokemon_atack = 10

while vida_pikachu > 0 and enemy_live > 0:
    pikachu_atack = input("¿que ataque vamos a usar? (Chispazo (10 atk) / Bola Voltio (12 atk): ")
    if pikachu_atack == ("Chispazo"):
        enemy_live -= 10
    elif pikachu_atack == ("Bola Voltio"):
        enemy_live -= 12

    print("a {} le restan {} Puntos de vida".format(pokemon_name, enemy_live))

    vida_pikachu -= pokemon_atack
    print("{} te quita {} puntos de vida".format(pokemon_name, pokemon_atack))


    print("a Pikachu le restan {} puntos de vida".format(vida_pikachu))

    if enemy_live <= 0:
        print("pikachu ha Ganado")
    elif vida_pikachu <= 0:
        print ("has perdido")

    print("Combate terminado")

