from nltk import Tree
from collections import defaultdict

def make_nltk_tree(derivation):
    """return a nlt Tree object based on the derivation (list or tuple of Rules)."""
    d = defaultdict(None, ((r.lhs, r.rhs) for r in derivation))
    
    def make_tree(lhs):
        return Tree(lhs[1:-1], (child if child not in d else make_tree(child) for child in d[lhs]))
    
    return make_tree(derivation[0].lhs)