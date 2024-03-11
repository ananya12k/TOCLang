from ply import lex

# Reserved keywords for a language
reserved = {
    'alphabet': 'ALPHABET',
    'str': 'STR',
    'lang': 'LANG',
    're': 'RE',
    'initial': 'INITIAL',
    'final': 'FINAL',
    'transition': 'TRANSITION',
    'states': 'STATES',
    'dfa': 'DFA',
    'nfa': 'NFA',
    'minimize': 'MINIMIZE',
    'isequivalent': 'ISEQUIVALENT',
    'show': 'SHOW',
    'if': 'IF',
    'else': 'ELSE',
    'visualize': 'VISUALIZE',
    'simulate': 'SIMULATE',
    'dpda': 'DPDA',
    'npda': 'NPDA',
    'pda': 'PDA',
    'stack': 'STACK',
    'pop': 'POP',
    'push': 'PUSH',
    'accept': 'ACCEPT',
    'reject': 'REJECT',
    'convert': 'CONVERT',
    'concat': 'CONCAT',
    'diff': 'DIFF',
    'kleene': 'KLEENE',
    'power': 'POWER',
    'union': 'UNION',
    'intersect': 'INTERSECT',
    'complement': 'COMPLEMENT',
    'operation': 'OPERATION',
    'closure': 'CLOSURE',
    'yes': 'YES',
    'no': 'NO',
    'regular': 'REGULAR',
    'isnotregular': 'ISNOTREGULAR',
    'cfl': 'CFL',
    'isnotcfl': 'ISNOTCFL',
    'checkpumpinglemmacfl': 'CHECKPUMPINGLEMMACFL',
    'checkpumpinglemmareg': 'CHECKPUMPINGLEMMAREG',
    'define': 'DEFINE',
    'nextstate': 'NEXTSTATE',
    'symbol': 'SYMBOL',
    'fa': 'FA',
    'from': 'FROM',
    'on': 'ONN',
    'to': 'TO',
    'export': 'EXPORT',
    'nonterminals': 'NONTERMINALS',
    'terminals': 'TERMINALS',
    'start': 'START',
    'rules': 'RULES',
    'cfg': 'CFG',
}

# List of token names
tokens = list(reserved.values()) + [
    'NUMBER',
    'ID',
    'LBRACE',
    'RBRACE',
    'COLON',
    'EQUALS',
    'LSQUARE',
    'RSQUARE',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'SLCOMMENT',  # Single line comment //
    'MLCOMMENT',  # Multiline comment /* */
    'DOCCOMMENT',  # Documentation comment """ """
    'ARROW',
    'PIPE',
    'SEMICOLON',
    'EPSILON'
]

# Define regular expressions for tokens
t_NUMBER = r'\d+'

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_EQUALS = r'='
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ARROW = r'->'
t_PIPE = r'\|'
t_SEMICOLON = r';'
t_EPSILON=r'ε'


# Define a rule for single-line comments
def t_SLCOMMENT(t):
    r'//.*'
    pass  # Single-line comments are ignored


# Define a rule for multi-line comments
def t_MLCOMMENT(t):
    r'/\*(.|\n)*?\*/'
    pass  # Multi-line comments are ignored


# Define a rule for documentation comments
def t_DOCCOMMENT(t):
    r'\"{3}[\s\S]*?\"{3}'
    pass  # Documentation comments are ignored


# Define a rule for identifiers (IDs)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')  # Check if the ID is a reserved word
    return t


# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Define a rule to ignore whitespace
t_ignore = ' \t'


# Define a rule for tracking errors
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test the lexer
# data = '''
# alphabet str lang re initial final transition states dfa nfa minimize
# isequivalent show if else visualize simulate dpda npda pda stack pop push
# accept reject convert concat diff kleene power union intersect complement
# operation closure yes no regular isnotregular cfl isnotcfl
# checkpumpinglemmacfl checkpumpinglemmareg from fa on to export define : , [](){} =
#
# // This is a single-line comment
#
# /*
# This is a multi-line comment
# */
#
# """
# This is a documentation comment
# """
# cfg MyGrammar {
#     nonterminals: A, B, C;
#     terminals: a, b, c;
#     start: A;
#     rules: {
#         A -> B C;
#         B -> a B | ε;
#         C -> b C | c;
#     }
# }
#
#
# '''
data = '''

// Define the alphabet
alphabet = {a, b, c}

// Define the string
string = "ababac"

// Define a finite automaton (FA) named myfa
fa 


() {
    // Define the states
    states: {q1, q2},

    // Define the initial state
    initial: {q1},

    // Define the final state
    final: {q2},

    // Define the transitions
    transitions: [
        {from q1 to q2 on a}
    ]
}

// Simulate the FA
simulate(myfa)

// Visualize the FA
visualize(myfa)

pda mypda {
    states: {q0, q1, q2},
    alphabet: {a, b, c},
    stack_alphabet: {A, B, C},
    initial: q0,
    final: q2,
    transitions: [
        {from: q0, to: q1, on: a, pop: A, push: AB},
        {from: q1, to: q1, on: b, pop: A, push: BC},
        {from: q1, to: q2, on: c, pop: B, push: ε}
    ]
}



'''
lexer.input(data)

# Tokenize
for tok in lexer:
    print(tok)
