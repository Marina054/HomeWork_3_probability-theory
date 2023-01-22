# Задача 2. В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?

import numpy as np

box1 = 8         # всего мячи в первом ящике
box2 = 12        # всего мячи во втором ящике
a = 5            # белые мячи в первом ящике
b = 5            # белые мячи во втором ящике
x = 2            # достали из первого ящика
y = 4            # достали из второго ящика
factorial = 1
n = (np.math.factorial(box1 ) / (np.math.factorial(a) * np.math.factorial(box1 - a)) * np.math.factorial(box2 ) / (np.math.factorial(b) * np.math.factorial(box2 - b))) # n = C8, 5 * C12, 5
print(float(n)) # 44352
m = (np.math.factorial(a ) / (np.math.factorial(x) * np.math.factorial(a - x))) * \
        (np.math.factorial(b ) / (np.math.factorial(1) * np.math.factorial(b - 1))) * \
            (np.math.factorial(3 ) / (np.math.factorial(1) * np.math.factorial(3 - 1)) + \
                np.math.factorial(7 ) / (np.math.factorial(1) * np.math.factorial(7 - 1)))# m = C5, 2 * C5, 1 * (C3, 1 + C7, 1)
print(float(m)) # 500
P = m / n
print(float(P)) # 0.011273448773448774


