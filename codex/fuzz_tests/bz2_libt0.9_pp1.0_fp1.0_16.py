import bz2
bz2.version

# prepare data and label
dir_path = 'Data/img_'+str(num).zfill(5)
test_img = pickle.load(bz2.BZ2File(dir_path+'/imgs_'+str(num).zfill(5)+'.pkl.bz2','rb'))
#test_label = pickle.load(bz2.BZ2File(dir_path+'/labels.pkl.bz2','rb'))

# remove invalid items
# (pil to numpy failed because some of the images are broken)
#for i in range(len(test_img)):
#    try:
#        test_img[i] = trans.to_tensor(trans.to_pil_image(test_img[i]))
#    except:
#        test_img.pop(i)

# padding
test_img_pad = torch.zeros([len(test_img), 128, 128, 128])
for i in range(len(test_img)):
    test_img_
