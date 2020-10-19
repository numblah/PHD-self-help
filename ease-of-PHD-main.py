def convertImg(filename):
	"""Requires: pillow

	pip install pillow
	from PIL import Image

	

	"""

	#opens the image based on the input filename
	img = Image.open(filename)
	#converts the image to RGBA, the difference with RBG here is that there is a fourth value between 0-1 that defines opacity (zero-transparent, 1-opaque)
	img = img.convert("RGBA")
	#.getdata() reads the images and puts information for each pixel in a sequence object (like a list)
	datas = img.getdata()
	#define a new list which will act as the new image
	newData =[]

	#iterate over each pixel and if it is 'white' add an entry to the new list replacing 'white transparent'
	#to 'white opaque'
	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2]==255:
			newData.append((255,255,255,1))
		else:
			newData.append(item) # if it wasn't white then just add the pixel as is to the new lsit
	#converts the new list into an image
	img.putdata(newData)
	# saves the image in the same file format (defined by the old file extension)
	img.save(filename)
	print("done")

