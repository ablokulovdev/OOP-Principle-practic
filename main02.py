
class Product:
    
    def __init__(self,name,price,category):
        
        self.name:str = name
        self.price: float = price
        self.category: str = category
        
    def get_info(self):
        print(f"Maxsulot nomi: {self.name}, price: ${self.price}")
        
        
pr01 = Product("cola",12_500.0,"Ichimlik")
pr02 = Product("non",10_500.0,"FOOD")
pr03 = Product("olma",1_500.0,"fructs")
pr04 = Product("banan",13_500.0,"fructs")
pr05 = Product("go'sht",87_500.0,"FOOD")


PR_LIST = [pr01,pr02,pr03,pr04,pr05]


mx = max(PR_LIST,key=lambda product: product.price)

mx.get_info()


