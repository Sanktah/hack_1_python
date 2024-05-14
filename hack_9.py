"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    contador = 0
    while contador < len(result):
        result.insert(contador + 1, "@")
        contador += 2
    return result  