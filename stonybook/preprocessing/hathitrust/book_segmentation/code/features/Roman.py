### using code and data from https://github.com/tedunderwood/DataMunging

import sys,re,os
from os import listdir
from os.path import isfile, join


class Roman:
	def __init__(self):
		self.romannumerals = set(['ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx', 'xxi', 'xxii', 'xxiii', 'xxiv', 'xxv', 'xxvi', 'xxvii', 'xxviii', 'xxix', 'xxx', 'xxxi', 'xxxii', 'xxxiii', 'xxxiv', 'xxxv', 'xxxvi', 'xxxvii', 'xxxviii', 'xxxix', 'xl', 'xli', 'xlii', 'xliii', 'xliv', 'xlv', 'xlvi', 'xlvii', 'xlviii', 'xlix', 'l', 'li', 'lii', 'liii', 'liv', 'lv', 'lvi', 'lvii', 'lviii', 'lix', 'lx', 'lxi', 'lxii', 'lxiii', 'lxiv', 'lxv', 'lxvi', 'lxvii', 'lxviii', 'lxix', 'lxx', 'lxxi', 'lxxii', 'lxxiii', 'lxxiv', 'lxxv', 'lxxvi', 'lxxvii', 'lxxviii', 'lxxix', 'lxxx', 'lxxxi', 'lxxxii', 'lxxxiii', 'lxxxiv', 'lxxxv', 'lxxxvi', 'lxxxvii', 'lxxxviii', 'lxxxix', 'xc', 'xci', 'xcii', 'xciii', 'xciv', 'xcv', 'xcvi', 'xcvii', 'xcviii', 'xcix', 'c', 'ci', 'cii', 'ciii', 'civ', 'cv', 'cvi', 'cvii', 'cviii', 'cix', 'cx', 'cxi', 'cxii', 'cxiii', 'cxiv', 'cxv', 'cxvi', 'cxvii', 'cxviii', 'cxix', 'cxx', 'cxxi', 'cxxii', 'cxxiii', 'cxxiv', 'cxxv', 'cxxvi', 'cxxvii', 'cxxviii', 'cxxix', 'cxxx', 'cxxxi', 'cxxxii', 'cxxxiii', 'cxxxiv', 'cxxxv', 'cxxxvi', 'cxxxvii', 'cxxxviii', 'cxxxix', 'cxl', 'cxli', 'cxlii', 'cxliii', 'cxliv', 'cxlv', 'cxlvi', 'cxlvii', 'cxlviii', 'cxlix', 'cl', 'cli', 'clii', 'cliii', 'cliv', 'clv', 'clvi', 'clvii', 'clviii', 'clix', 'clx', 'clxi', 'clxii', 'clxiii', 'clxiv', 'clxv', 'clxvi', 'clxvii', 'clxviii', 'clxix', 'clxx', 'clxxi', 'clxxii', 'clxxiii', 'clxxiv', 'clxxv', 'clxxvi', 'clxxvii', 'clxxviii', 'clxxix', 'clxxx', 'clxxxi', 'clxxxii', 'clxxxiii', 'clxxxiv', 'clxxxv', 'clxxxvi', 'clxxxvii', 'clxxxviii', 'clxxxix', 'cxc', 'cxci', 'cxcii', 'cxciii', 'cxciv', 'cxcv', 'cxcvi', 'cxcvii', 'cxcviii', 'cxcix', 'cc', 'cci', 'ccii', 'cciii', 'cciv', 'ccv', 'ccvi', 'ccvii', 'ccviii', 'ccix', 'ccx', 'ccxi', 'ccxii', 'ccxiii', 'ccxiv', 'ccxv', 'ccxvi', 'ccxvii', 'ccxviii', 'ccxix', 'ccxx', 'ccxxi', 'ccxxii', 'ccxxiii', 'ccxxiv', 'ccxxv', 'ccxxvi', 'ccxxvii', 'ccxxviii', 'ccxxix', 'ccxxx', 'ccxxxi', 'ccxxxii', 'ccxxxiii', 'ccxxxiv', 'ccxxxv', 'ccxxxvi', 'ccxxxvii', 'ccxxxviii', 'ccxxxix', 'ccxl', 'ccxli', 'ccxlii', 'ccxliii', 'ccxliv', 'ccxlv', 'ccxlvi', 'ccxlvii', 'ccxlviii', 'ccxlix', 'ccl', 'ccli', 'cclii', 'ccliii', 'ccliv', 'cclv', 'cclvi', 'cclvii', 'cclviii', 'cclix', 'cclx', 'cclxi', 'cclxii', 'cclxiii', 'cclxiv', 'cclxv', 'cclxvi', 'cclxvii', 'cclxviii', 'cclxix', 'cclxx', 'cclxxi', 'cclxxii', 'cclxxiii', 'cclxxiv', 'cclxxv', 'cclxxvi', 'cclxxvii', 'cclxxviii', 'cclxxix', 'cclxxx', 'cclxxxi', 'cclxxxii', 'cclxxxiii', 'cclxxxiv', 'cclxxxv', 'cclxxxvi', 'cclxxxvii', 'cclxxxviii', 'cclxxxix', 'ccxc', 'ccxci', 'ccxcii', 'ccxciii', 'ccxciv', 'ccxcv', 'ccxcvi', 'ccxcvii', 'ccxcviii', 'ccxcix', 'ccc', 'ccci', 'cccii', 'ccciii', 'ccciv', 'cccv', 'cccvi', 'cccvii', 'cccviii', 'cccix', 'cccx', 'cccxi', 'cccxii', 'cccxiii', 'cccxiv', 'cccxv', 'cccxvi', 'cccxvii', 'cccxviii', 'cccxix', 'cccxx', 'cccxxi', 'cccxxii', 'cccxxiii', 'cccxxiv', 'cccxxv', 'cccxxvi', 'cccxxvii', 'cccxxviii', 'cccxxix', 'cccxxx', 'cccxxxi', 'cccxxxii', 'cccxxxiii', 'cccxxxiv', 'cccxxxv', 'cccxxxvi', 'cccxxxvii', 'cccxxxviii', 'cccxxxix', 'cccxl', 'cccxli', 'cccxlii', 'cccxliii', 'cccxliv', 'cccxlv', 'cccxlvi', 'cccxlvii', 'cccxlviii', 'cccxlix', 'cccl', 'cccli', 'ccclii', 'cccliii', 'cccliv', 'ccclv', 'ccclvi', 'ccclvii', 'ccclviii', 'ccclix', 'ccclx', 'ccclxi', 'ccclxii', 'ccclxiii', 'ccclxiv', 'ccclxv', 'ccclxvi', 'ccclxvii', 'ccclxviii', 'ccclxix', 'ccclxx', 'ccclxxi', 'ccclxxii', 'ccclxxiii', 'ccclxxiv', 'ccclxxv', 'ccclxxvi', 'ccclxxvii', 'ccclxxviii', 'ccclxxix', 'ccclxxx', 'ccclxxxi', 'ccclxxxii', 'ccclxxxiii', 'ccclxxxiv', 'ccclxxxv', 'ccclxxxvi', 'ccclxxxvii', 'ccclxxxviii', 'ccclxxxix', 'cccxc', 'cccxci', 'cccxcii', 'cccxciii', 'cccxciv', 'cccxcv', 'cccxcvi', 'cccxcvii', 'cccxcviii', 'cccxcix', 'cd', 'cdi', 'cdii', 'cdiii', 'cdiv', 'cdv', 'cdvi', 'cdvii', 'cdviii', 'cdix', 'cdx', 'cdxi', 'cdxii', 'cdxiii', 'cdxiv', 'cdxv', 'cdxvi', 'cdxvii', 'cdxviii', 'cdxix', 'cdxx', 'cdxxi', 'cdxxii', 'cdxxiii', 'cdxxiv', 'cdxxv', 'cdxxvi', 'cdxxvii', 'cdxxviii', 'cdxxix', 'cdxxx', 'cdxxxi', 'cdxxxii', 'cdxxxiii', 'cdxxxiv', 'cdxxxv', 'cdxxxvi', 'cdxxxvii', 'cdxxxviii', 'cdxxxix', 'cdxl', 'cdxli', 'cdxlii', 'cdxliii', 'cdxliv', 'cdxlv', 'cdxlvi', 'cdxlvii', 'cdxlviii', 'cdxlix', 'cdl', 'cdli', 'cdlii', 'cdliii', 'cdliv', 'cdlv', 'cdlvi', 'cdlvii', 'cdlviii', 'cdlix', 'cdlx', 'cdlxi', 'cdlxii', 'cdlxiii', 'cdlxiv', 'cdlxv', 'cdlxvi', 'cdlxvii', 'cdlxviii', 'cdlxix', 'cdlxx', 'cdlxxi', 'cdlxxii', 'cdlxxiii', 'cdlxxiv', 'cdlxxv', 'cdlxxvi', 'cdlxxvii', 'cdlxxviii', 'cdlxxix', 'cdlxxx', 'cdlxxxi', 'cdlxxxii', 'cdlxxxiii', 'cdlxxxiv', 'cdlxxxv', 'cdlxxxvi', 'cdlxxxvii', 'cdlxxxviii', 'cdlxxxix', 'cdxc', 'cdxci', 'cdxcii', 'cdxciii', 'cdxciv', 'cdxcv', 'cdxcvi', 'cdxcvii', 'cdxcviii', 'cdxcix'])

	def extractFeatures(self, pages, pagenums):
		feats=[]
		for i in range(len(pages)):
			feats.append({})
			
		for i in range(len(pages)):
			page=pages[i]

			for idx, line in enumerate(page):
				if idx > 4:
					continue

				line = line.strip().lower().split(" ")
				for word in line:
					if word in self.romannumerals:
						feats[i]["roman:header"]=1


			for idx, line in enumerate((reversed(page))):

				if idx > 4:
					continue

				line = line.strip().lower().split(" ")
				for word in line:
					if word in self.romannumerals:
						feats[i]["roman:footer"]=1

		return feats


