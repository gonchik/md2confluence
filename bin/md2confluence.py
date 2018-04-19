import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../lib'))
import mdparser


def _help():
    """
    :return:
    """
    print(
        """
        {} [markdown file]
        """.format(sys.argv[0]))
    pass


def upload(html, id=None, pid=None, user=None, password=None):
    """
    This method related to push Confluence
    :param html:
    :param id:
    :param pid:
    :param user:
    :param password:
    :return:
    """
    pass


def main():
    """
    :return:
    """

    parser = argparse.ArgumentParser(description='Convert markdown to confluence html.')
    parser.add_argument('file', type=str)
    parser.add_argument('--user', help="Username for push into Confluence")
    parser.add_argument('--pass', help="Password for push into Confluence")
    parser.add_argument('--id', help="Page id for update page")
    parser.add_argument('--parent-id', help="Parent page id")
    parser.add_argument('--show-in-console', action="store_true", default=True, help="Show in console")

    args = parser.parse_args()
    # print(args.accumulate(args.integers))

    html = mdparser.parse(open(args.file).read())
    if args.show_in_console:
        print(html)


if __name__ == "__main__":
    main()
