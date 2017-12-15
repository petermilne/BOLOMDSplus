#!/usr/bin/env python

import argparse
from MDSplus import *

def make_bolo_tree(args):
	tree = Tree(args.tree[0], -1, "NEW")
	for site in range(1, args.bolo8_count+1):
		bname = ".BOLO%d" % (site)
		module = tree.addNode(bname)
		for ch in range(1, 24+1):
			chn = module.addNode("CH%02d" % (ch), "SIGNAL")
			br = 1 + (ch - 1)/3
			id = (ch - 1)%3
			idnames = ("MAG_%d", "phi_%d", "PWR_%d" )
			idnamefmt = idnames[id]
			#print("addTag %s" % idnamefmt % (br))
			chn.addTag(idnamefmt % (br))
	tree.write()

def run_main():
	parser = argparse.ArgumentParser(description="make_bolo_tree")
	parser.add_argument('--bolo8_count', default=1, help = "number of bolo8 modules" )
	parser.add_argument('tree', nargs=1, help = "tree name")
	make_bolo_tree(parser.parse_args())
# execution starts here

if __name__ == '__main__':
    run_main()

