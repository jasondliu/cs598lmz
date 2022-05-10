import bz2
bz2.decompress?
img_decomp = bz2.decompress(img_comp)
#Now we can check that the decompressed image is the same as the original.
Image(data=img_decomp)

#
#Check that the decoded image is still the same.
#
#The image is displayed as its filename
display(Image(uri="imgs/bird_small.png"))

#Your code here
img_bird = io.BytesIO(img_decomp)

img_bird_array = img_bird
display(Image(img_bird))


#Now that the image is loaded, we can test our compression routine using k-means.

#Step 0: Rewrite the helper functions from the assignement in week3
#your code here...
def find_closest_centroids(X,initial_centroids):
    centroids = initial_centroids
    m=X.shape[0]
    idx = np.zeros(m)
    for i in range(m):
        distance = np.sqrt(np.sum
