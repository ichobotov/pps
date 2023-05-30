import re


def find_string(line, reg_expr):
    if re.findall(reg_expr, line):
        return True


def read_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line

def add_pashr(line):
    return '$PASHR,TT2,'+ line

# BOARD = 'BD940'
# BOARD = 'Bynav'
# BOARD = 'Comnav'
# BOARD = 'MB2'
# BOARD = 'A20'
#
delta_list = []

data = open(rf'C:\python\pps\stability\mb2_fromA20_pps.log', 'a')
data.write('Deltas'+'\n')

cnt = 0

for line in read_file(rf'C:\python\pps\stability\mb2_fromA20_ttt.log'):
    if find_string(line, r'\$PASHR,TTT,.*:\d{2}\.(\d*)\*'):
        delta = re.match(r'\$PASHR,TTT,.*:\d{2}\.(\d*)\*', line).group(1)
        # delta = 1000000000 - int(delta)
        # tmp = list(delta)
        # tmp.insert(3,'.')
        # delta = float(''.join(tmp))
        # data.write(str(delta)+'\n')
        # delta_list.append(delta)
        # if int(delta) < 999999100:
        #     cnt += 1
        #     continue
        delta = add_pashr(str(delta))
        data.write(delta+'\n')
    else:
        continue
print (cnt)


# data.write(f'data={delta_list}')

