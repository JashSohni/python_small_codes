import os 
i = 0
addr = raw_input("Enter the address   ")
namee = raw_input("Enter the standard name   ")

for filename in os.listdir(addr):
    strr = filename
    temp_str = strr.split('.')
    dst = namee + str(i) + '.' + temp_str[1]
    src = addr+'/' + filename
    dst = addr+'/' + dst
    os.rename(src , dst)
    i += 1