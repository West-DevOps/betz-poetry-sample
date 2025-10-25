# standard library imports
import argparse
import sys 

# Import the crypto argparser from the relevant sub-module
from src.tools.cryptography import parser as crypto_parser
from src.tools.tabulardata import parser as pandas_parser

def no_op_error(*args) -> None:
    """The (no-operation) function, called when garbage is entered on the CLI"""
    raise EnvironmentError("Need to supply a valid command to run!")


def parser(args: list[str]) -> argparse.Namespace:
    """
    Main function for parsing the CLI arguments. 
    """
    # Create the main arg parser (a.k.a. root level parser)
    arg_parser = argparse.ArgumentParser()

    # Bind the 'no_op' function the the main parser so if no subcommands are given it will just throw the exception
    # which is not caught 'blowing the stack' as it's known in programming languages
    # which in turn will exit the program non-0 (fail). 
    arg_parser.set_defaults(func=no_op_error)

    # Add subparsers (sub commands in the cli)
    subparsers = arg_parser.add_subparsers(help="Supported commands / operations")

    # Call submodule parsers
    # First I will bind a very basic example, the `hash` subcommand for the program. 
    crypto_parser(subparsers)

    # This one is a bit more complex
    pandas_parser(subparsers)

    # Parse all CLI args, returning what is known in `argparse` land as the arg `Namespace` which is basically a python dict with extra bells and whistles.
    return arg_parser.parse_args(args)


def main() -> None:
    """Main entry point for poetry"""
    # Call the argparser function
    parsed_args = parser(sys.argv[1:])

    # Dispatch execution to the bound function (here be the magic)
    parsed_args.func(parsed_args)
    

if __name__ == '__main__':
    main()
