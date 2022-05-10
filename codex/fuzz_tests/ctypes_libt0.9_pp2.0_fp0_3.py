import ctypes
ctypes.windll.user32.MessageBoxW(0, "Processing Complete", "Final Message", 1)
#Writing to kml file
f = open('point.kml', 'w')
#Begin writing kml file
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://www.opengis.net/kml/2.2'>\n")
f.write("<Document>\n")
#write multiple placemarks based on number of elements in array
for i in range (len(name)):
    f.write("<Placemark>\n")
    f.write("  <name>" + name[i] + "</name>\n")
    f.write("  <description>" + address[i] + "</description>\n")
    f.write("  <Point>\n")
    f.write("   <coordinates>" + longi[i] + "," + lat[i]  + "</coordinates>\n")
    f.write(" 
