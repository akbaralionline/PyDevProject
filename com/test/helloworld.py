def find_start_point(p, d):
    # Check for if solution exist
    if sum(p) < sum(d):
        print ('Solution do not exist')
        return None
    startpoint, ssum = 0, 0
    for i in range(0, len(p)):
        ssum+=p[i]-d[i]
        if ssum < 0:
            # Petrol pumps will lie in the forward indexes
            startpoint = i+1
            ssum = 0
    return p[startpoint]

if __name__=='__main__':
    p = [6,7,1,4]
    d = [5,8,3,2]
    print(find_start_point(p, d))