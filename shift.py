def shift(bit,d):
    if d=='L':
        return bit[2:]+bit[:2]
    else:
        return bit[-2:]+bit[:-2]

if __name__=="__main__":
    bit=input('Enter binary string:')
    d=input('Enter L for LEFT rotation and R for RIGHT:')
    print(shift(bit,d))