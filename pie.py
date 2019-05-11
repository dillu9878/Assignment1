def pie(n):
    # This is function for calculating value of Pie up-to n iteration.
    s = 0
    for i in range(n):
        s += ((-1)**i)*(1/(2*i+1))
    return s*4


if __name__ == "__main__":
    # This is main function
    n=int(input('Enter he number of iterations:'))
    print('Value of Pie is:',pie(n))