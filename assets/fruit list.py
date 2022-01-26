class Product:
    def __init__(self, Fruit, Price, Weight):
        self.Fruit = Fruit
        self.Price = Price
        self.Weight = Weight

def main():
    Product = [('Banana',12,4),('Apple',13,5),('Strawberry',11,6),('Mango',20,7)
               ,('Orange',21,8)]

    file = open('fruit.txt', 'w')
    file.write('\'fruit\',Price,Weight\n')
    for i in Product:
        file.write(str(i)+'\n')
    print("debug")    
        
    file.close()

main()
