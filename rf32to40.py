#!/usr/bin/env python3

"""Script to update Robot Framework data syntax to be compatible with RF 4.0.

Updates old FOR loop syntax as well as list and dictionary variable item access.

  Usage: rf32to40.py path [path ...]

Paths support recursive glob patterns like 'tests/**/*.robot' regardless the
operating system.
"""

import glob
import re
import sys

from robot.parsing import get_model, ModelVisitor, Token
from robot.parsing.model import Statement


class Updater(ModelVisitor):

    def visit_ForLoop(self, node):
        node.header.get_token(Token.FOR).value = 'FOR'
        for item in node.body:
            for token in item.get_tokens(Token.OLD_FOR_INDENT):
                token.value = ''
        if not (node.end and node.end.get_token(Token.END).value == 'END'):
            node.end = Statement([Token(Token.SEPARATOR, '    '),
                                  Token(Token.END, 'END'),
                                  Token(Token.EOL, '\n')])
        self.generic_visit(node)

    def visit_Statement(self, node):
        for token in node.get_tokens(Token.ARGUMENT):
            token.value = re.sub(r'[@&](\{.*?}\[.*?])', r'$\1', token.value)


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args or '--help' in args:
        sys.exit(__doc__)
    print(args)
    for item in args:
        for path in glob.glob(item, recursive=True):
            model = get_model(path)
            Updater().visit(model)
            model.save()
