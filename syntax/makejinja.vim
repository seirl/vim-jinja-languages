if exists("b:current_syntax")
  finish
endif

runtime! syntax/make.vim
unlet b:current_syntax

:syntax include @inJinja syntax/jinja.vim
:syntax region inJinja start="{{" end="}}" keepend contains=@inJinja
:syntax region inJinja start="{%" end="%}" keepend contains=@inJinja
:syntax region inJinja start="{#" end="#}" keepend contains=@inJinja

let b:current_syntax = "makejinja"
