import hashlib
import argparse


def compute_hash(hashing_algorithmn: str, input_filename: str) -> str:
    """
    Compute a hash of an input file (core functionality we want to expose via CLI)
    """
    hasher = hashlib.new(hashing_algorithmn)
    with open(input_filename, 'rb') as file_handle:
        hasher.update(file_handle.read())
        return hasher.hexdigest()


def hash_cli(namespace: argparse.Namespace) -> None:
    """
    This is what argparse is bound to under the hood, it will receive the arguments to the program via the namespace
    """
    # Grab the filename CLI arg from the provided namespace
    filename = namespace.filename

    # Grab the hashing algo to use 
    algo = namespace.alogrithmn

    # Print the hash, calling the main logic function to do it.
    print(compute_hash(algo, filename))


def parser(subparsers) -> None:
    """
    This function is called by the top-level `cli.py` to bind all the `hash` commands to the cli
    """
    # Create a parser for `hash`
    hash_parser = subparsers.add_parser('hash')

    # Add the needed CLI args
    hash_parser.add_argument('-a', '--alogrithmn', type=str, required=False, default='sha256', help='Which hashing algorithmn to use (defaults to sha256)')
    hash_parser.add_argument('-f', '--filename', type=str, required=True, help='File to create a hash for')

    # When `hash` is called, bind the `hash_cli` as what needs to be called. 
    hash_parser.set_defaults(func=hash_cli)
