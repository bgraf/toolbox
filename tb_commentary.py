#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser('tb_commentary')
    parser.add_argument('-w', '--width', type=int, default=50,
                        help='number of columns')
    parser.add_argument('text', type=str, nargs='+',
                        help='text')
    args = parser.parse_args()

    text = ' '.join(args.text)
    columns = args.width

    def make_box(delimiter, inlet=3):
        sep_line = '// ' + delimiter * (columns - 3)
        print(sep_line)

        text_line = (delimiter * inlet) +  text.center(columns - 3 - 2 * inlet) + (delimiter * inlet)
        print('// ' + text_line)
        print(sep_line)

    make_box('=')
    print()
    make_box('~')
    print()
    make_box('-')




