import pprint
import argparse
import pandas as pd


def print_cli(namespace: argparse.Namespace) -> None:
    """Just pretty print a table to stdout"""
    df = pd.read_csv(namespace.filename)
    if namespace.verbose:
        # Fully print the dataframe to stdout
        pprint.pprint(df)
        print(df.shape)
    else:
        # Just print the 'shape' of the frame (row & col counts)
        shape = df.shape
        print(f"Table has {shape[0]} rows and {shape[1]} columns")


def parser(subparsers) -> None:
    panda_parser = subparsers.add_parser('pandas')
    # Just like to root level parser we can attach more subparsers to subparsers
    # Building complex CLI logic with multiple options / commands
    pd_subs = panda_parser.add_subparsers()

    simple_print = pd_subs.add_parser('print')
    # namespace.verbose will == True if supplied, basic on/off flagging
    simple_print.add_argument('-v', '--verbose', action='store_true', default=False)
    simple_print.add_argument('-f', '--filename', type=str, required=True)
    # Always remember to 'bind' a function for this parser
    simple_print.set_defaults(func=print_cli)
