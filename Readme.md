# coc-denite

[denite.nvim](https://github.com/Shougo/denite.nvim) sources for [coc.nvim](https://github.com/neoclide/coc.nvim).

This plugin is optional since you can use builtin list from coc, see `:h coc-list`

## Sources

- `coc-command` command list.
- `coc-diagnostic` diagnostic list.
- `coc-extension` extension list.
- `coc-service` service list.
- `coc-source` source list.
- `coc-symbols` symbols of current buffer.
- `coc-workspace` search symbols of current workspace.
- `link` links of current buffer.

see `:h coc-denite` for detail.

## Install

Use plugin manager, like https://github.com/junegunn/vim-plug by add:

Plug 'neoclide/coc.nvim', {'tag': '\*', 'do': { -> coc#util#install()}}
Plug 'neoclide/coc-denite'

to your `vimrc` and run:

:PlugInstall

## LICENSE

MIT
