import argparse

from catsay import catsay


def cli():
    parser = argparse.ArgumentParser(description="the cat says...")

    parser.add_argument(
        "text",
        nargs="*",
        help="The text to pass to catsay",
    )
    args = parser.parse_args()
    catsay(" ".join(args.text))


if __name__ == "__main__":

    cli()
