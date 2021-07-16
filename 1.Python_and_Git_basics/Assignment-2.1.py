# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:40:20 2021

@author: PiyushBhujbal
"""

import numpy as np

target  = int(50)

numbers = np.array(input())

class MyClass:
    
    def show(self,n,array):
        ans = np.array([[0,0]])
        for i in range(0,len(array)-1):
            for j in range(0,len(array)-1):
                if n == array[i]+array[j]:
                    ans = np.append(ans,[[i,j]],axis = 0)
                    
        dic = dict(zip(range(1,len(ans)+1),ans))
        print(dic)
       
C = MyClass()
C.show(target,numbers)