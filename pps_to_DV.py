import re
import math


def find_string(line, reg_expr):
    if re.findall(reg_expr, line):
        return True


def read_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line

def add_pashr(line):
    return '$PITER,TT2,'+ line

def gps_to_utc(time):
    hh = int(time[0:2])
    mm = int(time[3:5])
    ss = int(time[6:8])
    time_sec_gps = hh*3600 + mm*60 + ss
    time_sec_utc = time_sec_gps - 18
    if time_sec_utc < 0:
        time_sec_utc = time_sec_utc + 86400
    hh_utc = time_sec_utc/3600
    mm_utc = (hh_utc - int(hh_utc))*60
    ss_utc = round((mm_utc - int(mm_utc))*60)
    if ss_utc == 60:
        ss_utc = 0
        mm_utc = (hh_utc - int(hh_utc)) * 60 + 1

    if int(mm_utc) == 59 and ss_utc == 60:
        ss_utc = 0
        mm_utc = 0
        hh_utc = time_sec_utc / 3600 + 1

    time_sec_utc = str(int(hh_utc)).rjust(2, '0')+str(int(mm_utc)).rjust(2, '0') +str(int(ss_utc)).rjust(2, '0')
    return time_sec_utc


data = open(rf'C:\python\pps\mb2_from_comnav.log22222', 'a')

cnt = 0

for line in read_file(rf'C:\python\pps\mb2_from_comnav.log'):
    if find_string(line, r'\$PASHR,TTT,.*:\d{2}\.(\d*)\*'):
        message = re.match(r'\$PASHR,TTT,(.,)\d{2}:\d{2}:\d{2}', line).group(1)
        time = re.match(r'\$PASHR,TTT,.,(\d{2}:\d{2}:\d{2})', line).group(1)
        time = gps_to_utc(time)
        time = time + '.00'
        delta = re.match(r'\$PASHR,TTT,.*:\d{2}\.(\d*)\*', line).group(1)

        # if int(delta) < 999999000:  # filter value jumps
        #     cnt += 1
        #     print(line)
        #     continue


        # if len(str(int(delta))) < 9:  # to handle transition through 0
        #     delta = int(delta) + 1000000000
        pashr_tt3 = add_pashr(message + time+','+ str(delta))
        data.write(pashr_tt3+'\n')
    else:
        continue
print (cnt)


