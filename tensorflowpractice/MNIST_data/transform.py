# -*- coding: utf-8 -*-
from PIL import Image
import struct
import csv
import progressbar

def read_image(filename, saveaddr):
	with open(filename, 'rb') as f:
		buf = f.read()

	index = 0
	magic, number, rows, cols = struct.unpack_from('>IIII', buf, index)
	index += struct.calcsize('>IIII')

	readbar = progressbar.ProgressBar('reading images ', number, 0)
	readbar.show()

	for cnt in range(number):
		img = Image.new('L', (cols, rows))

		for x in range(rows):
			for y in range(cols):
				img.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
				index += struct.calcsize('>B')

		img.save(saveaddr + '/' + str(cnt) + '.png')
		readbar.increase()

	readbar.present()
	print('Successfully read all images from ' + filename)

def read_label(filename, savefile):
	with open(filename, 'rb') as f:
		buf = f.read()

	index = 0
	magic, number = struct.unpack_from('>II', buf, index)
	index += struct.calcsize('>II')

	with open(savefile, 'w', newline='') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter = ',')
		csvwriter.writerow(['No', 'label'])

		readbar = progressbar.ProgressBar('reading labels ', number, 0)
		readbar.show()

		for cnt in range(number):
			label = int(struct.unpack_from('>B', buf, index)[0])
			index += struct.calcsize('>B')
			csvwriter.writerow(map(str, [cnt, label]))
			readbar.increase()

		readbar.present()
		print('Successfully read all labels from ' + filename)

def main():
	read_image('train-images-idx3-ubyte', 'train-images-idx3')
	read_label('train-labels-idx1-ubyte', 'train-labels-idx1/train-labels.csv')
	read_image('t10k-images-idx3-ubyte', 't10k-images-idx3')
	read_label('t10k-labels-idx1-ubyte', 't10k-labels-idx1/test-labels.csv')

if __name__ == '__main__':
	main()