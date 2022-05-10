import _struct

#Read gracesr.bdf as a list of strings
bdf1=open('example6.bdf','r')
line1 = bdf1.readlines()
bdf1.close

#Write it as a binary file which can be read by the Spice subcircuit
bdf2=open('example6.dat','wb')

#Set initial conditions
node1=1 #Ref node
node2=node1+7 #Piston node
node3=node2+12 #Piston tappet
node4=555
be=1 #Ref node = 1
i=0 #Line counter
while i < len(line1):
    #Convert lines of the bdf to binary and write them to the binary file
    if len(line1[i]) > 3:
        
        #Find and replace the node numbers the binary equivalent
        if line1[i].split()[1] == 'NODE1':
            line1[i]=line1[i].replace(line1[i].split()[3],str(node1))
        if line1[i].split()[
