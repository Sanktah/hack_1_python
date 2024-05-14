"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    result = result.replace('a','@')
    result = result.replace('o','0')
    result = result.replace('i','1')
    return result