# tenho_frio = False

# if tenho_frio:
#     print("agua")

# else:
#     print("comer")

#____________________________________________________________________

tenho_sede = False
tenho_fome = False

# if tenho_sede or tenho_fome:
#     print("vou para cozinha")

# else:
#     print("ficar na sala")

if tenho_sede and tenho_fome:
    print("comer pastel e beber agua")

elif tenho_sede and not(tenho_fome):
    print("beber agua")

elif not(tenho_sede) and tenho_fome:
    print("comer pastel")

else: 
    print("nao fazer nada")

#__________________________________________________________________

