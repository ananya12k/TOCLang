from parsertoc import *
from ast_parser import *
from symbol_table import SymbolTable


class SemanticAnalyzer:
    def __init__(self, ast, symbol_table):
        self.ast = ast
        self.symbol_table = SymbolTable()

    def analyze(self):
        for statement in self.ast:
            if isinstance(statement, AlphabetNode):
                self.analyze_alphabet(statement)
            elif isinstance(statement, STRNode):
                self.analyze_string(statement)
            elif isinstance(statement, FANode):
                self.analyze_fa(statement)
            elif isinstance(statement, PDANode):
                self.analyze_pda(statement)
            elif isinstance(statement, CFGNode):
                self.analyze_cfg(statement)
            # Add more cases for other types of statements as needed

    def analyze_alphabet(self, node):
        # Semantic analysis for the alphabet declaration
        identifier = node.identifier
        alphabet_list = node.alphabet_list

        # Check for duplicate identifier using SymbolTable
        if not self.symbol_table.add_symbol(identifier, alphabet_list):
            print(f"Semantic Error: Duplicate identifier '{identifier}'")
        else:
            print(f"Semantic Analysis: Alphabet {identifier} defined with symbols {alphabet_list}")

    def analyze_string(self, node):
        # Semantic analysis for the string declaration
        identifier = node.identifier
        value = node.value

        # Check if the string value matches the declared alphabet
        declared_alphabet = self.symbol_table.get_value(identifier)
        if declared_alphabet is None:
            print(f"Semantic Error: Unknown alphabet identifier '{identifier}' in string declaration")
        else:
            for char in value:
                if char not in declared_alphabet:
                    print(f"Semantic Error: Symbol '{char}' in string is not in the declared alphabet")

    def analyze_fa(self, node):
        # Semantic analysis for the finite automaton
        identifier = node.identifier
        states = node.states
        initial = node.initial
        final = node.final
        transitions = node.transitions

        # Validate FA properties, such as initial and final states
        if initial.initial_state not in states.states:
            print(f"Semantic Error: Initial state '{initial.initial_state}' not in the set of states")

        for final_state in final.final_states:
            if final_state not in states.states:
                print(f"Semantic Error: Final state '{final_state}' not in the set of states")

        # Additional validation for transitions, if needed

    def analyze_pda(self, node):
        # Semantic analysis for the pushdown automaton
        identifier = node.identifier
        states = node.states
        initial = node.initial
        final = node.final
        transitions = node.transitions

        # Validate PDA properties, such as initial and final states
        if initial.initial_state not in states.states:
            print(f"Semantic Error: Initial state '{initial.initial_state}' not in the set of states")

        for final_state in final.final_states:
            if final_state not in states.states:
                print(f"Semantic Error: Final state '{final_state}' not in the set of states")

        # Additional validation for transitions, if needed

    def analyze_cfg(self, node):
        # Semantic analysis for the context-free grammar
        identifier = node.identifier
        cfg_body = node.cfg_body

        # Validate CFG properties, such as start symbol and rules
        start_symbol = None
        nonterminals = set()
        terminals = set()
        rules = set()

        for cfg_item in cfg_body:
            if isinstance(cfg_item, NonTerminalsNode):
                nonterminals.update(cfg_item.nonterminals_list)
            elif isinstance(cfg_item, TerminalsNode):
                terminals.update(cfg_item.terminals_list)
            elif isinstance(cfg_item, StartNode):
                start_symbol = cfg_item.start_symbol
            elif isinstance(cfg_item, RulesNode):
                rules.update(cfg_item.rules_list)

        # Additional validation, if needed
        if start_symbol not in nonterminals:
            print(f"Semantic Error: Start symbol '{start_symbol}' not in the set of non-terminals")

        # Validate each rule
        for rule in rules:
            left_side = rule.left_side
            right_side = rule.right_side

            if left_side not in nonterminals:
                print(f"Semantic Error: Left side symbol '{left_side}' in rule is not a non-terminal")

            for symbol in right_side:
                if symbol not in nonterminals and symbol not in terminals:
                    print(f"Semantic Error: Symbol '{symbol}' in rule is not a non-terminal or terminal")


# Usage
semantic_analyzer = SemanticAnalyzer(result)
semantic_analyzer.analyze()
