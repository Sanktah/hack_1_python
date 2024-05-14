"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result2 = []
    result = result.replace('a','@')
    result = result.replace('o','0')
    result = result.replace('i','1')
    for i in result:
        i = i.upper()
        result2.append(i)
    result = result2
    return result
