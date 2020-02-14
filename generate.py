#!/usr/bin/env python3

from pathlib import Path

LANGUAGES = {
    'c': ['c'],
    'cpp': ['cpp', 'cc', 'cxx', 'C'],
    'cs': ['cs'],
    'go': ['go'],
    'haskell': ['hs'],
    'java': ['java'],
    'javascript': ['js'],
    'lua': ['lua'],
    'ocaml': ['ml', 'mli'],
    'pascal': ['pas'],
    'perl': ['pl'],
    'php': ['php'],
    'prolog': ['pro'],
    'python': ['py'],
    'ruby': ['rb'],
    'rust': ['rs'],
}
JINJA_EXTENSIONS = ['jinja2', 'j2']

VIM_SYNTAX_FILE = """\
if exists("b:current_syntax")
  finish
endif

runtime! syntax/{lang}.vim
unlet b:current_syntax

:syntax include @inJinja syntax/jinja.vim
:syntax region inJinja start="{{{{" end="}}}}" keepend contains=@inJinja
:syntax region inJinja start="{{%" end="%}}" keepend contains=@inJinja
:syntax region inJinja start="{{#" end="#}}" keepend contains=@inJinja

let b:current_syntax = "{lang}jinja"
"""

PROJECT_DIR = Path(__file__).parent

if __name__ == '__main__':
    with (PROJECT_DIR / 'ftdetect/langjinja.vim').open('w') as f:
        for lang, extensions in LANGUAGES.items():
            ftmatch = ['*.{}.{}'.format(e, je)
                       for e in extensions
                       for je in JINJA_EXTENSIONS]
            f.write('au BufNewFile,BufRead {} setf {}jinja\n'.format(
                ','.join(ftmatch), lang))

    for lang, extensions in LANGUAGES.items():
        with (PROJECT_DIR / 'syntax/{}jinja.vim'.format(lang)).open('w') as f:
            f.write(VIM_SYNTAX_FILE.format(lang=lang))
