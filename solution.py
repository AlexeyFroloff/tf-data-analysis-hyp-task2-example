import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 423200009 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = anderson_ksamp([x, y]).pvalue 
    alpha = 0.09
    return p_value < alpha
    
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False
