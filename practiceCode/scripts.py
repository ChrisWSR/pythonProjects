fh = open("example.txt","w")
#fh.write("this is a high level secret of my self i love coconuts,\n" )
#fh.write("this is a high level secret of my self i love coconuts")
for i in range(1,10):
    fh.write("%d \n" %i) 
fh.close 
