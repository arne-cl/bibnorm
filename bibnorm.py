#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser, FileType
import bibtexparser


def normalize(input_file, output_file):
    """
    read a *.bib file, change every 'title' and 'booktitle' field to only
    use uppercase for the first letter and write the changes to the output
    file.
    
    Parameters
    ----------
    input_file : file
        the *.bib file to normalized
    output_file : file
        the *.bib output file
    """
    bibtex_str = input_file.read()
    bib_database = bibtexparser.loads(bibtex_str)

    for entry in bib_database.entries:
        for field in ('title', 'booktitle'):
            if field in entry:
                new_title = entry['title'].capitalize()
                entry['title'] = new_title

    new_bibstr = bibtexparser.dumps(bib_database)
    output_file.write(new_bibstr.encode('utf-8'))


if __name__ == '__main__':
    parser = ArgumentParser(prog='bibnorm')

    parser.add_argument(
        dest='input_file', default=sys.stdin, nargs='?', type=FileType('r'),
        help=('Specify the *.bib input file. If no input file is specified, '
              'bibnorm will try to read from STDIN'))

    parser.add_argument(
        dest='output_file', default=sys.stdout, nargs='?', type=FileType('w'),
        help=('Specify the *.bib output file. If no output file is specified, '
              'bibnorm will write to STDOUT'))

    args = parser.parse_args(sys.argv[1:])
    normalize(args.input_file, args.output_file)
