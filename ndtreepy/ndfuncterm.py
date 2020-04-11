import ndtreepy.ndfunc as ndfunc

def indent_show_tree(tree,k='_id'):
    sdfs = ndfunc.tree2sdfs(tree)
    for i in range(len(sdfs)):
        indents = '    ' * ndnd.get_depth(tree,sdfs[i])
        k = sdfs[i][k]
        print(indents+k)


        
