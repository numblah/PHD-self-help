def convertImg(filename):
	"""Requires: pillow

	pip install pillow
	from PIL import Image

	

	"""

	#opens the image based on the input filename
	img = Image.open(filename)
	#converts the image to RGBA, the difference with RBG here is that there is a fourth value between 0-1 that defines opacity (zero-transparent, 1-opaque)
	img = img.convert("RGBA")
	#.getdata() reads the images and puts 
	datas = img.getdata()

	newData =[]

	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2]==255:
			newData.append((255,255,255,1))
		else:
			newData.append(item)
	img.putdata(newData)
	img.save(filename)
	print("done")

