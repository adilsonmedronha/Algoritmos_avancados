from utils import *

def k(A, B):

    if len(str(A)) == 1 and len(str(B)) == 1:
        return int(A) * int(B)
    else:
        a1, a_e1, a2, a_e2, a3 = split_by_3(A)
        b1, b_e1, b2, b_e2, b3 = split_by_3(B)

        x1 = k(a1, b1)
        x2 = k(a1, b2)
        x3 = k(a1, b3)
        x4 = k(a2, b1)
        x5 = k(a2, b2)
        x6 = k(a2, b3)

        x7 = k(a3, b1)
        x8 = k(a3, b2)
        x9 = k(a3, b3)

        r1 = x1*10**(a_e1+b_e1) + x2*10**(a_e1+b_e2) + x3*10**(a_e1)
        r2 = x4*10**(a_e2+b_e1) + x5*10**(a_e2+b_e2) + x6*10**(a_e2) 
        r3 = x7*10**(b_e1) + x8*10**(b_e2) + x9
        
        return r1 + r2 + r3