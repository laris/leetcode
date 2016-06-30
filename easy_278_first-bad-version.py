#!/usr/bin/python

from random import randint

latest_version = int(raw_input("How many version of your latest version?"))
print "latest version = "+str(latest_version)
badict_version = randint(1,latest_version)
print "Bad Version = "+str(badict_version)

print range(1,latest_version)

dict_ver = {}
for d_index in range(1,latest_version):
    if d_index < badict_version:
#	print "d_index = "+str(d_index)+", type(d_index) = "+str(type(d_index))
	dict_ver[d_index]=True # good
#	dict_ver.update({d_index:"True"}) # good
#	dict_ver.update(d_index='True') #bad way
#	dict_ver.update(dict(d_index='True')) #bad way
#	dict_ver.update(dict(eval(d_index)='True')) # bad way ( key cann SyntaxError keyword can't be an expression )
#	print d_index
#	print dict_ver
#	print "update key="+str(d_index)+", value="+str(dict_ver[d_index])+", type(value[key])="+str(type(dict_ver[d_index]))
    else:
#	print "d_index="+str(d_index)
	#dict_ver.update(d_index="False")
	dict_ver[d_index]=False
#	print "update key="+str(d_index)+", value="+str(dict_ver[d_index])+", type(value[key])="+str(type(dict_ver[d_index]))

#for key in dict_ver:
#    print "key = "+str(key)+", value = "+str(dict_ver[key])

start = 1
end = latest_version
bad_ver=0
while start+1 < end:
    mid = start + (end - start)/2
#    print "--debug-1--start = "+str(start)+", mid = "+str(mid)+", end = "+str(end)+"dict_ver[mid] = "+str(dict_ver[mid])
    if dict_ver[mid] == False:
        end = mid
#        print "-d2-start = "+str(start)+", mid = "+str(mid)+", end = "+str(end)
    else:
        start = mid
#        print "-d3-start = "+str(start)+", mid = "+str(mid)+", end = "+str(end)
#    print "The Bad Version = "+str(mid)
    bad_ver=mid

print "The Bad Version = "+str(bad_ver)

