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
    
    # #Hàm phi(n) --> OK
    # Phi hàm euler sẽ bẳng tích n*(của n chia hết cho p (p|n)) * (1 - 1/p)
    # với p là số nguyên tố
    # mỗi p chỉ xuất hiện 1 lần
    def phi(self, n):
        res = n
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                while(n%i==0):
                    n = n // i
                res = res - res//i
        if n >  1:
            res -= res//n
        return res

