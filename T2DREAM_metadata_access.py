#!/usr/bin/env python3

import argparse
import os
import sys
import json


EPILOG = '''
%(prog)s GET the results of a search from an T2DREAM server metadata in JSON or TSV format

Basic Useage:

    %(prog)s --infile file.txt
    %(prog)s --infile TSTSR112545
    
    A single column file listing the  identifiers of the objects desired
    Search accession

    The output file format either JSON or TSV
    This can be changed with '--format'

'''

def getArgs():
    parser = argparse.ArgumentParser(
        description=__doc__, epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        )
    parser.add_argument('--infile',
                        help="File containing single column of accessions " +
                        "or a single accession")
    parser.add_argument('--outfile',
                        help="Output file name", default='report.txt')
    parser.add_argument('--format',
                        help="Output format can be either JSON or TSV.  Default is JSON",
                         default='JSON')
    args = parser.parse_args()

class get_metadata():
        def __init__(self, args):
            self.infile = args.infile
            self.outfile = args.outfile
            self.format = args.format

def main():
    args = getArgs()

if __name__ == "__main__":
    main()
