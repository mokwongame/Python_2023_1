def unitStep(x):
    if x > 0: return 1
    elif x == 0: return 0.5
    else: return 0
    
y = unitStep(-3)
print(y)