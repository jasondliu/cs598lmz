import mmapi

m = mmapi.mmFrame()

s = mmapi.mmScreen()

p = s.getProfile()

mb = p.getMeasurementBundle()

m.addMeasurementBundle(mb)

c = mmapi.mmColladaConfiguration()

c.calculatestats = True

m.save("C:\\temp\\poo.dae",c)

m.load("c:\\temp\\poo.dae")



If I load the file again anything that I create has its original id's restored. So I conclude there is no new point comning in. But of course if I rename a point q, foo or something else, then save and reload, it does work. You can do this if you can tag your points that you want to export by some other mechanism (can you delete all the points and then re-export?)



I am sure that this is a tricky bug and will require further looking at. I will write you again when it has bee fixed. If you have any more details or things you want to try, no hurry of course, let me know. I will also
