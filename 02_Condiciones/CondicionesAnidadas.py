if __name__ == '__main__':
    n = int(raw_input().strip())


if n%2:
 print ("Weird")
else:
    if n>=2 and n<=5:
        print ("Not Weird")
    else:
        if n>=6 and n<=20:
            print ("Weird")
        else:
            if n>20:
                print ("Not Weird")