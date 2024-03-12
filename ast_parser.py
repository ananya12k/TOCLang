class ASTNode:
    def __init__(self, *args):
        self.children = args


class AlphabetNode(ASTNode):
    def __init__(self, identifier, alphabet_list):
        self.identifier = identifier
        self.alphabet_list = alphabet_list


class STRNode(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value


class FANode(ASTNode):
    def __init__(self, identifier, states, initial, final, transitions):
        self.identifier = identifier
        self.states = states
        self.initial = initial
        self.final = final
        self.transitions = transitions


class PDANode(ASTNode):
    def __init__(self, identifier, states, initial, final, transitions):
        self.identifier = identifier
        self.states = states
        self.initial = initial
        self.final = final
        self.transitions = transitions


class StateListNode(ASTNode):
    def __init__(self, states):
        self.states = states


class InitialNode(ASTNode):
    def __init__(self, initial_state):
        self.initial_state = initial_state


class FinalNode(ASTNode):
    def __init__(self, final_states):
        self.final_states = final_states


class TransitionsNode(ASTNode):
    def __init__(self, transitions):
        self.transitions = transitions


class TransitionNode(ASTNode):
    def __init__(self, from_state, to_state, on_input, pop=None, push=None, stack=None):
        self.from_state = from_state
        self.to_state = to_state
        self.on_input = on_input
        self.pop = pop
        self.push = push
        self.stack = stack


class CFGNode(ASTNode):
    def __init__(self, identifier, cfg_body):
        self.identifier = identifier
        self.cfg_body = cfg_body


class NonTerminalsNode(ASTNode):
    def __init__(self, nonterminals_list):
        self.nonterminals_list = nonterminals_list


class TerminalsNode(ASTNode):
    def __init__(self, terminals_list):
        self.terminals_list = terminals_list


class StartNode(ASTNode):
    def __init__(self, start_symbol):
        self.start_symbol = start_symbol


class RulesNode(ASTNode):
    def __init__(self, rules_list):
        self.rules_list = rules_list


class RuleNode(ASTNode):
    def __init__(self, left_side, right_side):
        self.left_side = left_side
        self.right_side = right_side


class StatementNode(ASTNode):
    def __init__(self, statement_type, *args):
        self.statement_type = statement_type
        self.args = args


class ConditionNode(ASTNode):
    def __init__(self, condition_type):
        self.condition_type = condition_type
