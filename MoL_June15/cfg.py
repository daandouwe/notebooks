from collections import defaultdict, deque
from symbol import is_terminal
from rule import Rule
import math


class WCFG(object):

    def __init__(self, rules=[]):
        self._rules = []
        self._rules_by_lhs = defaultdict(list)
        self._terminals = set()
        self._nonterminals = set()
        for rule in rules:
            self.add(rule)

    def add(self, rule):
        self._rules.append(rule)
        self._rules_by_lhs[rule.lhs].append(rule)
        self._nonterminals.add(rule.lhs)
        for s in rule.rhs:
            if is_terminal(s):
                self._terminals.add(s)
            else:
                self._nonterminals.add(s)

    def update(self, rules):
        for rule in rules:
            self.add(rule)

    @property
    def nonterminals(self):
        return self._nonterminals

    @property
    def terminals(self):
        return self._terminals

    def __len__(self):
        return len(self._rules)

    def __getitem__(self, lhs):
        return self._rules_by_lhs.get(lhs, frozenset())

    def get(self, lhs, default=frozenset()):
        return self._rules_by_lhs.get(lhs, frozenset())

    def can_rewrite(self, lhs):
        """Whether a given nonterminal can be rewritten.

        This may differ from ``self.is_nonterminal(symbol)`` which returns whether a symbol belongs
        to the set of nonterminals of the grammar.
        """
        return lhs in self._rules_by_lhs

    def __iter__(self):
        return iter(self._rules)
    
    def iteritems(self):
        return self._rules_by_lhs.iteritems()
    
    def __str__(self):
        lines = []
        for lhs, rules in self.iteritems():
            for rule in rules:
                lines.append(str(rule))
        return '\n'.join(lines)


def read_grammar_rules(istream):
    """
    Reads grammar rules in cdec format.


    >>> import math
    >>> istream = ['[S] ||| [X] ||| 1.0', '[X] ||| [X] [X] ||| 0.5'] + ['[X] ||| %d ||| 0.1' % i for i in range(1,6)]
    >>> rules = list(read_grammar_rules(istream, transform=log))
    >>> rules
    [[S] -> [X] (0.0), [X] -> [X] [X] (-0.69314718056), [X] -> 1 (-2.30258509299), [X] -> 2 (-2.30258509299), [X] -> 3 (-2.30258509299), [X] -> 4 (-2.30258509299), [X] -> 5 (-2.30258509299)]
    """
    for line in istream:
        lhs, rhs, log_prob = line.strip().split(' ||| ')
        rhs = rhs.split()
        log_prob = math.log(float(log_prob))
        yield Rule(lhs, rhs, log_prob)

