from collections import defaultdict

from itertools import product
inputFile = open("D://traff_light/inputs/a.txt","r");   #your file directory

firstLine = inputFile.readline();
L = list(map(int, firstLine.split()));

T1 = L[0];
intersection = L[1];
streets = L[2];
cars = L[3];
points = L[4];

streetsdict = defaultdict(list)
for i in range(streets):
    streetsdict['streetinfo' +str(i)] = [];
    
for i in range(streets):
    streetsdict['streetinfo' +str(i)].extend(list(map(str,inputFile.readline().strip().split())));
    
    
carroute = defaultdict(list)
for i in range(cars):
    carroute['carrouteinfo' +str(i)] = [];
    
for i in range(cars):
    carroute['carrouteinfo' +str(i)].extend(list(map(str,inputFile.readline().strip().split())));


trafficlightcount = [];
for i,j in product(range(streets), range(cars)):
    for k in range(1,int(carroute['carrouteinfo' +str(j)][0])):
        if (carroute['carrouteinfo' +str(j)][k] == streetsdict['streetinfo' +str(i)][2]):
            trafficlightcount.append(streetsdict['streetinfo' +str(i)][1]);
        else:
            pass
    
#for i in range(streets):
#    for j in range(cars):
#        for k in range(1,int(carroute['carrouteinfo' +str(j)][0])):
#            if (carroute['carrouteinfo' +str(j)][k] == streetsdict['streetinfo' +str(i)][2]):
#                trafficlightcount.append(streetsdict['streetinfo' +str(i)][1]);
#            else:
#                pass
            
            
light_count = set(trafficlightcount)

if (int(T1/len(light_count)) > 0):
    w = int(T1/len(light_count));
else:
    w = 1;


print(len(light_count));
trafficcity=[];

for i in light_count:
    for j in range(streets):
        if i == streetsdict['streetinfo' +str(j)][1]:
            trafficcity.append(streetsdict['streetinfo' +str(j)][2])
    print(i);
    print(len(trafficcity));
    for k in trafficcity:
        print(k,w);
    trafficcity=[]