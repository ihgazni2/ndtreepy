import copy
import ndtreepy.ndfunc as ndnd
from ndtreepy.ndfunc import *
from ndtreepy.ndfuncterm import *
tree = ndnd.load('tst.json')
sdfs = ndnd.tree2sdfs(tree)





nd = get_nds_via_attr(tree,'tag','韩文明')[0]

t = copy.deepcopy(tree)


nd = get_nds_via_attr(tree,'tag','张金兴')[0]
dept = ndnd.get_parent(tree,nd)
dept,new_tree,old_tree = ndnd.disconnect(tree,dept)

len(t) == len(old_tree) + len(new_tree)
indent_show_tree(new_tree)
indent_show_tree(old_tree)
