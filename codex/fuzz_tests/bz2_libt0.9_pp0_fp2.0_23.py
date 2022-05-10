import bz2
bz2_output = bz2.BZ2File('output.bin','wb')
bz2_output.write(imgbin)
bz2_output.close()
 
# Display the blob across different scales (do not worry about
# seeing the full figures, just the effect of scaling).

blob.blobs['found'].plot_scales(colors=['red'],save='/tmp/blob.png')

blob.blobs['found'].make_image(img_shape=(360,480),color='gray')

blob.blobs['found'].plot(save='/tmp/blob.png')

blob.blobs['found'].plot(labels=True,save='/tmp/blob.png')

blob.blobs['found'].plot(bbox=True,save='/tmp/blob.png')
