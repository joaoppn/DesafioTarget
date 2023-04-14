

def calc_fibonacci(max):
    i=[0,1]
    if(max == 0):
        return True
    else:
        while(i[0]<=max):
            temp = i[1]
            i[1] = i[0] + i[1]
            i[0] = temp
            if(i[0]  == max):
                return True
            else:
                continue
        return False





num = input("Digite um valor:")
if(calc_fibonacci(int(num))==True):
    print("Número pertence a sequência Fibonacci! :)")
else:
    print("Número não pertence a sequência Fibonacci! :(")