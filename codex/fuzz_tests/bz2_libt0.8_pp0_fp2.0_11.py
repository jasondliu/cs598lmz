import bz2
bz2file = bz2.BZ2File(path2data+'train_img.bz2','w')
bz2file.write(img_df.to_csv(header=True,index=True,sep=',').encode('utf-8'))
bz2file.close()
 
# write image label data to bz2 file 
bz2file = bz2.BZ2File(path2data+'train_label.bz2','w')
bz2file.write(lbl_df.to_csv(header=True,index=True,sep=',').encode('utf-8'))
bz2file.close()

# write image label data to bz2 file 
bz2file = bz2.BZ2File(path2data+'test_label.bz2','w')
bz2file.write(test_df.to_csv(header=True,index=True,sep=',').encode('utf-8'))
bz2file.close()

# write image data
