# ============================================================================
# FILE: workspace.py
# AUTHOR: Qiming Zhao <chemzqm@gmail.com>
# License: MIT license
# ============================================================================
# pylint: disable=E0401,C0411
import re
from denite.kind.file import Kind as FileKind
from denite.source.base import Base
from os.path import relpath

def getKind(num):
    if num == 1:
        return 'File'
    if num == 2:
        return 'Module'
    if num == 3:
        return 'Namespace'
    if num == 4:
        return 'Package'
    if num == 5:
        return 'Class'
    if num == 6:
        return 'Method'
    if num == 7:
        return 'Property'
    if num == 8:
        return 'Field'
    if num == 9:
        return 'Constructor'
    if num == 10:
        return 'Enum'
    if num == 11:
        return 'Interface'
    if num == 12:
        return 'Function'
    if num == 13:
        return 'Variable'
    if num == 14:
        return 'Constant'
    if num == 15:
        return 'String'
    if num == 16:
        return 'Number'
    if num == 17:
        return 'Boolean'
    if num == 18:
        return 'Array'
    if num == 19:
        return 'Object'
    if num == 20:
        return 'Key'
    if num == 21:
        return 'Null'
    if num == 22:
        return 'EnumMember'
    if num == 23:
        return 'Struct'
    if num == 24:
        return 'Event'
    if num == 25:
        return 'Operator'
    if num == 26:
        return 'TypeParameter'
    return 'Unknown'

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'coc-workspace'
        self.kind = FileKind(vim)

    def define_syntax(self):
        self.vim.command('syntax case ignore')
        self.vim.command(r'syntax match deniteSource_WorkspaceHeader /\v^.*$/ containedin=' + self.syntax_name)
        self.vim.command(r'syntax match deniteSource_WorkspaceName /\v^\s*\S+/ contained '
                         r'containedin=deniteSource_WorkspaceHeader')
        self.vim.command(r'syntax match deniteSource_WorkspaceKind /\[\w\+\]/ contained '
                         r'containedin=deniteSource_WorkspaceHeader')
        self.vim.command(r'syntax match deniteSource_WorkspaceFile /\f\+$/ contained '
                         r'containedin=deniteSource_WorkspaceHeader')


    def highlight(self):
        self.vim.command('highlight default link deniteSource_WorkspaceName Normal')
        self.vim.command('highlight default link deniteSource_WorkspaceKind Typedef')
        self.vim.command('highlight default link deniteSource_WorkspaceFile Comment')

    def gather_candidates(self, context):
        context['is_interactive'] = True
        cwd = self.vim.call('getcwd')
        items = self.vim.call('CocAction', 'getWorkspaceSymbols', context['input'])
        if items is None or items is 0:
            return []
        candidates = []
        for item in items:
            location = item['location']
            filepath = location['uri']
            if filepath.startswith('file://'):
                filepath = filepath[7:]
            filepath = relpath(filepath, start=cwd)
            candidates.append({
                'word': item['name'],
                'abbr':'%s [%s] %s' % (item['name'], getKind(item['kind']), filepath),
                'action__path': filepath,
                'action__col': item['location']['range']['start']['character'] + 1,
                'action__line': item['location']['range']['start']['line'] + 1,
                })

        return candidates
