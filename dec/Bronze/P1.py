import math
for i in range(1, 16):
    fname ="p1data/"+str(i)+".in"
    fhand = open(fname, "r")

    def dist(x1, y1, x2, y2):
        manhattan=abs(x2-x1)+abs(y2-y1)
        return manhattan

    coordlist=list()
    counter=0

    for line in fhand:
        coord = line.split(" ")
        if len(coord)==1:
            n=int(line.split(" ")[0])
        else:
            coordlist.append(int(coord[0]))
            coordlist.append(int(coord[1]))
            counter+=1

    check=0
    totaldist=0
    savedist=0

    while check<counter:
        if check<counter-1:
            x1=coordlist[2*check]
            y1=coordlist[2*check+1]
            x2=coordlist[2*check+2]
            y2=coordlist[2*check+3]
            
            totaldist+=dist(x1, y1, x2, y2)
        if check!=n-1 and check!=0:
            testA=dist(coordlist[2*check-2], coordlist[2*check-1], coordlist[2*check], coordlist[2*check+1])
            testB=dist(coordlist[2*check], coordlist[2*check+1], coordlist[2*check+2], coordlist[2*check+3])
            testC=dist(coordlist[2*check-2], coordlist[2*check-1], coordlist[2*check+2], coordlist[2*check+3])
            red=testA+testB-testC
            #print(red)
            if red>savedist:
                savedist=red
        check+=1
    print(totaldist-savedist)
    fhand.close()


    