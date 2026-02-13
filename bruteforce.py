####################################  get args from shell  #########################################

import argparse  # to get args from the terminal

# add arguments and stuff
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=float, required=True, help="input decimal number")
parser.add_argument("--show-all", action="store_true", help="show all iterations")
parser.add_argument("--show-denom", action="store_true", help="only show denominator increments")

# define args as variables
all_args = parser.parse_args()
num = all_args.n
show_all = all_args.show_all
show_denom = all_args.show_denom

####################################################################################################

import math, humanize, time

# init at floor of num
numer = math.floor(num)
denom = 1

# fun variables
numer_count = 0
denom_count = 0
start_time = time.time()

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
    denom_count += 1
    # numer = math.floor(num) * denom
    numer = latest_num * denom
     
    # increment numerator until it is greater than or equal to number
    while numer / denom < num:
        if numer / denom != num:
            numer += 1
            numer_count += 1
            if show_all:
                show()
    latest_num = numer / denom
    if show_denom or show_all:
        show()

# all done :D
print('-' * (len(str(numer)) + len(str(denom)) + 3))
print(f'{numer} / {denom}')
print('')
print(f'checked {humanize.intcomma(numer_count + denom_count)} iterations in {round((time.time() - start_time),3)} seconds')
