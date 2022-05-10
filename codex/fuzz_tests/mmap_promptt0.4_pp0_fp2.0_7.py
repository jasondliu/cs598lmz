import mmap
# Test mmap.mmap.read()

# Write a string to a file
with open('lorem.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
            'Phasellus vulputate mauris at orci ornare, in rutrum justo '
            'sodales. Vivamus sit amet sollicitudin urna. Cras eget '
            'sodales odio. Praesent eget diam sit amet elit aliquet '
            'euismod. Sed condimentum, nunc quis tincidunt fringilla, '
            'quam libero efficitur nisi, sed euismod nisl nisl at '
            'risus. Donec auctor nisi ut diam rutrum, eu porta nisi '
            'vulputate. Aliquam erat volutpat. Nunc ut leo quis mi '
            'elementum porta. Curabitur euismod, velit vel dignissim '
           
