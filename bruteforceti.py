import math

# get the number and stuff
num = float(input("enter decimal number"))
show_denom = True if ("y" in input("show only denominators? y/n ").lower()) else False
show_all = True if ("y" in input("show all iterations? y/n ").lower()) else False

# init at floor of num
numer = math.floor(num)
denom = 1

def show():
    print(f'{numer} / {denom}')

# start at floor/1
#   increment denominator
#   set numerator to num * denominator
#   increment numerator until greater than num

while numer / denom != num:
    
    latest_num = math.floor(num)
    
    # increment denominator and set to floor of num with the new denominator
    denom += 1
    # numer = math.floor(num) * denom
    numer = latest_num * denom
     
    # increment numerator until it is greater than or equal to number
    while numer / denom < num:
        if numer / denom != num:
            numer += 1
            if show_all:
                show()
    latest_num = numer / denom
    if show_denom or show_all:
        show()

# all done :D
print('-' * (len(str(numer)) + len(str(denom)) + 3))
print(f'{numer} / {denom}')
