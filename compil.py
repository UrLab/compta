#!/usr/bin/python3
from pathlib import Path

FILENAME = "total.csv"
HEADER = "Date,Qui,Quoi,Delta,Total Caisse,Total Coffre,Total Coffre plus Caisse (Cash),Total Banque,Total Urlab,Commentaire du trésorier"

def main():
	with open(FILENAME, "w", encoding='utf-8') as f:
		f.write(HEADER)

	here = Path('.')
	# Get all directories in here but not .git
	dirs = [i for i in here.iterdir() if i.is_dir() and i.name[0] != '.']

	for dir_ in dirs:
		files = [file for file in dir_.iterdir()]

		for file in files:
			with file.open(mode='r', encoding='utf-8') as f:
				file_text = f.readlines()
			file_text = file_text[1:]

			for l in range(len(file_text)):
				line = file_text[l]
				comma = line.find(',')
				line = line[:comma] + f"/{file.name[:2]}/{dir_.name}" + line[comma:]
				file_text[l] = line

			with open(FILENAME, 'a', encoding='utf-8') as f:
				for line in file_text:
					f.write(line)


if __name__ == "__main__":
	main()

