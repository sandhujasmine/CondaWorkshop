import argparse


def hello(user):
    print('Hello ' + user)


def cli():
    parser = argparse.ArgumentParser(description='Hello world! Example')
    parser.add_argument('-n', '--name', type=str,
                        help="Enter name",
                        default="World!")
    args = parser.parse_args()

    hello(args.name)


if __name__ == "__main__":
    cli()
