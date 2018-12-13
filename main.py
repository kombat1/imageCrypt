import argparse 


args = argparse.ArgumentParser()
args.add_argument('-n','--name',help='Name Crypt File',metavar='')
args.add_argument('--image',help='image',metavar='')
args.add_argument('--zip',help='ZipFile',metavar='')




group = args.add_mutually_exclusive_group()
group.add_argument('--scan',help='scan site Using: --scan -u [url] ',action="store_true")
args = args.parse_args()

def main():
	if not args.name:

		try:
			file1 = open(args.image, 'rb')
			b_file1 = file1.read()
		except FileNotFoundError:
			print("Файл "+args.image+" не найден")
		try:	
			file2 = open(args.zip, 'rb')
			b_file2 = file2.read()
		except FileNotFoundError:
			print("Файл "+args.zip+" не найден")

		file3 = open(args.image, 'wb')
		file3.write(b_file1)
		file3.write(b_file2)
		print("\x0a\x0a\x00[+] Complite")

	elif args.name != "\x00":

		try:
			file1 = open(args.image, 'rb')
			b_file1 = file1.read()
		except FileNotFoundError:
			print("Файл "+args.image+" не найден")
		try:	
			file2 = open(args.zip, 'rb')
			b_file2 = file2.read()
		except FileNotFoundError:
			print("Файл "+args.zip+" не найден")

		file3 = open(args.name, 'wb')
		file3.write(b_file1)
		file3.write(b_file2)
		print("\x0a\x0a\x00[+] Complite")

if __name__ == '__main__':
	main()		
