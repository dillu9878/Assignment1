def cal(fileName = 'input.txt'):
    print('<first name> <hourly rate> <hours worked> <payable amount>')
    file = open(fileName, 'r')
    line = file.readline()
    while line:
        d = line.split()
        print(d[0],d[1],d[2],int(d[1])*int(d[2]))
        line = file.readline()


if __name__ == '__main__':
    fileName=input('Enter file name:')
    cal(fileName)
    exit()