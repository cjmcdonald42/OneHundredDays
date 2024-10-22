'''
Day 03
Concatenation of Strings
'''

food = input("What is your favorite food? ")
plant = input("Name a type of plant: ")
cookingMethod = input("Name a cooking method: ")
burned = input("What word describes burned food? : ")
diy = input("Name a DIY item")

print(f"""
    == Today's Menu ==
    {cookingMethod} {food} with {burned} {plant} on a bed of {diy}
    
    Bon appatite!

""")
