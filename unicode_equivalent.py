
from argparse import ArgumentParser, RawTextHelpFormatter
from bs4 import BeautifulSoup
from itertools import product
from unicodedata import normalize
import urllib.parse


def decode_unicode_hex(data: str) -> str:
    """
    It's help to represent some unicode entity
    For example represent "&#xff1e;" as ＞ but meanwhile represent "&#x3e;" as "&gt;"
    """
    return BeautifulSoup(data, "html.parser")


def urlencode_unicode(data: str) -> str:
    """
    Url encode the unicode characters
    """
    return urllib.parse.quote(decode_unicode_hex(data).encode())


def unicode_equivalent(desired_char: str, normalization_form: list = ["NFKC", "NFKD", "NFC", "NFD"]) -> list:
    """
    Return a unique list that contains unicode equivalent characters
    """

    unicode_chars = list(map(''.join, product('0123456789ABCDEF', repeat=4)))
    result = set()
    for char in unicode_chars:
        template = f"&#x{char};"
        for form in normalization_form: 
            if normalize(form, urllib.parse.unquote(urlencode_unicode(template))) == desired_char:
                # If character is not equal to the desired character: add it
                if urllib.parse.unquote(urlencode_unicode(template)) != desired_char:
                    result.add(template)
    return list(result)


def parse_result(data: list):
    for template in data:
        print(f"Representation: {decode_unicode_hex(template)}")
        print(f"Unicode: {template}")
        print(f"Url encoded: {urlencode_unicode(template)}")
        print()


def main():

    if __name__ == "__main__":
        parser = ArgumentParser(
            prog="unicode_equivalent.py",
            description="Attacking Unicode Normalization by finding unicode equivalent characters",
            epilog='Examples:\r\n\tunicode-equivalent.py -i ">"\r\n\tunicode-equivalent.py -i "<" -f NFKD',
            formatter_class=RawTextHelpFormatter,
        )
        parser._optionals.title = "Options"
        parser.add_argument("-i", "--input", metavar="character", nargs="?", help="Your desired character")
        parser.add_argument("-f", "--form", metavar="normalization_form", nargs="?", help="Unicode normalization form NFKC, NFKD, NFC, NFD: default all")
        args = parser.parse_args()

        if args.input:
            if args.form:
                if args.form in ["NFKC", "NFKD", "NFC", "NFD"]:
                    result = unicode_equivalent(desired_char=args.input, normalization_form=[args.form])
                else:
                    exit(f"Unicode normalization form {args.form} is not correct")
            else:
                result = unicode_equivalent(desired_char=args.input)

            parse_result(result)
        else:
            parser.print_help()

main()
