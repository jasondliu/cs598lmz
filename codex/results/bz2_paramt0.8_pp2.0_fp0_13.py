from bz2 import BZ2Decompressor
BZ2Decompressor

print "loading packets"
packet_objects = []
for packet in packets:
    packet_objects.append(Packet(packet[0], packet[1], packet[2]))

print "loading bodies"
body_objects = []
for body in bodies:
    body_objects.append(Body(body[1], body[2], [None], [body[3]]))

print "loading orbiters"
orbiter_objects = []
for orbiter in orbiters:
    orbiter_objects.append(Orbiter(orbiter[0], orbiter[1], orbiter[2],
                                   orbiter[3], orbiter[4], orbiter[5],
                                   orbiter[6], orbiter[7], orbiter[8]))

#print "loading feature vectors"
#features = []
#for feature in features_file:
#    features.append(feature)

print "loading raw features"
raw_features = []
for feature in raw_features_file:
    raw_features.append(feature)

print "done"


#@profile
