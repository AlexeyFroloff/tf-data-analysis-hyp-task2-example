import pandas as pd
import numpy as np
from scipy import stats

chat_id = 423200009 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, p_value = stats.ks_2samp(x, y, alternative='two-sided')
    alpha = 0.03
    return p_value < alpha
    
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False
