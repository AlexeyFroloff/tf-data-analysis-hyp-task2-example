import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 423200009 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = MMD(compute_kernel="laplacian", gamma=1).test(x, y)[1]
    alpha = 0.03
    return p_value < alpha
    
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False
