from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления ' 
          'квадратного корня из заданного числа')
print (message)

def  CalculateSquareRoot (Number):
    """ 
Вычисляет квадратный корень
    """
    return  sqrt(Number)

def calc(your_number) :
     """ 
Вычисляет квадратный корень
    """
    if your_number <= 0:
        return     
    Calculater = Calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          ' Это будет: {Calculater}')


print(message)
calc (25.5)
