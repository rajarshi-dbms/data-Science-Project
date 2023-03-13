
    #Create the instances of the dataset, download
    data = Dataset(annotation_file=annotation_file, transforms= transforms )
    load = Download()

    #Print image names and their captions from annotation file using dataset object
    for idx in data.lt :
        print ("file :"+idx["file_name"]+"\n")
        print (idx["captions"])
    i=0
    #Download images to ./data/imgs/ folder using download object

    while i < 10 :
        x =data.__getann__(i)
        load(x[0] ,x[1] )
        i+=1

    #Transform the required image (roll number mod 10) and save it seperately
    item =data.__transformitem__("data/imgs/0.jpg")
    i = 0
    for im in item:
        s = "% s" % i
        x = im.save(outputs+"0"+s+".jpg")
        i+=1
