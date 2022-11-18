def main(a):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x1=a%10
    a=a//10
    x2=a%10
    a=a//10
    x3=a%10
    a=a//10
    x4=a%10
    x5=a//10

    return (x1+x2+x3+x4+x5)>2
print(main(10001))