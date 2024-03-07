import math
from typing import List

class toanhoc:
    def __init__(self):
        pass
    #tính ước chung lớn nhất
    def gcd(self,a,b) -> int :
        while(b > 0):
            r = a % b
            a = b
            b = r
        return a
    #kiểm tra số nguyên tố
    def isPrime(self,a) -> bool:
        if a < 2:
            return False
        for i in range(2,int(math.sqrt(a))+1):
            if a % i == 0:
                return False
        return True
    #kiễm tra số nguyên tố cùng nhau gcd(a,b)=1.
    def isCoPrime(self,a,b) -> bool:
        if self.gcd(a,b) == 1:
            return True
        return False
    #tìm ucln bằng thuật toán euclide mờ rộng
    """
    1759x + 550y = 1
        Hay 550^(-1) mod 1759 = 355
            1759(-1) mod 550 = -111
    Điều cần và đủ để có nghịch đảo là d = 1 và khi đó x là nghịch đảo của a mod b và y là nghịch đảo của b mod a

    """
    """
    
    """
    def extendedEuclid(self,a,b) -> List[int]:
        d = x = y = 0
        if b == 0: #hệ thức trở thành ax = d
            d = a
            x = 1
            y = 0
        else: #hệ thức là ax + by = d
            d, x, y = self.extendedEuclid(b, a%b)
            temp = x
            x = y
            y = temp - (a//b)*y
        return [d,x,y]
    
    # #Hàm pheta(n)
    # def pheta(self,n,power) -> int:
    #     if self.isPrime(n):
    #         return n-1
    #     else:
    #         #tách số
    #         a = 1
    #         b = n
    #         i = 0
    #         for i in range(2,int(math.sqrt(n))+1):
    #             while(b % i == 0):
    #                 a = i
    #                 b = b/i    
    #             if(i != 0): 
    #                 break
    #         return self.pheta(n,i)*self.pheta(b,1)
        

