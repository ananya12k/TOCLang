import ply.yacc as yacc

# Get the token list from the lexer
from lexertoc import tokens


# Parsing rules
def p_statement_alphabet(p):
    '''statement : ALPHABET ID EQUALS LBRACE alphabet_list RBRACE'''
    p[0] = ('alphabet', p[2], p[5])


def p_alphabet_list(p):
    '''alphabet_list : ID
                     | alphabet_list COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_statement_str(p):
    '''statement : STR ID EQUALS SINGLEQUOTE STRING SINGLEQUOTE'''
    p[0] = ('str', p[2], p[4])


def p_statement(p):
    '''statement : fa_statement
                 | pda_statement
                 | cfg_statement'''
    p[0] = p[1]


def p_fa_statement(p):
    '''fa_statement : FA ID LPAREN RPAREN LBRACE fa_body RBRACE'''
    p[0] = ('fa', p[2], p[6])


def p_pda_statement(p):
    '''pda_statement : PDA ID LPAREN RPAREN LBRACE pda_body RBRACE'''
    p[0] = ('pda', p[2], p[6])


# FA grammar rules

def p_fa_body(p):
    '''fa_body : states
               | initial
               | final
               | transitions'''
    p[0] = p[1]


def p_states(p):
    '''states : STATES COLON LBRACE states_list RBRACE'''
    p[0] = ('states', p[3])


def p_states_list(p):
    '''states_list : ID
                   | states_list COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_initial(p):
    '''initial : INITIAL COLON LBRACE ID RBRACE'''
    p[0] = ('initial', p[4])


def p_final(p):
    '''final : FINAL COLON LBRACE final_list RBRACE'''
    p[0] = ('final', p[3])


def p_final_list(p):
    '''final_list : ID
                  | final_list COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_transitions(p):
    '''transitions : TRANSITIONS COLON LBRACE transitions_list RBRACE'''
    p[0] = ('transitions', p[3])


def p_transitions_list(p):
    '''transitions_list : transition
                        | transitions_list COMMA transition'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_transition(p):
    '''transition : LSQUARE FROM COLON ID COMMA TO COLON ID COMMA ONN COLON ID RSQUARE
                  | LSQUARE FROM COLON ID COMMA TO COLON ID COMMA ONN COLON ID COMMA POP COLON ID COMMA PUSH COLON ID COMMA STACK COLON ID RSQUARE'''
    if len(p) == 11:
        p[0] = (p[4], p[7], p[10])
    else:
        p[0] = (p[4], p[7], p[10], p[13], p[16])


# PDA grammar rules

def p_pda_body(p):
    '''pda_body : states
                | initial
                | stack_init
                | final
                | transitions'''
    p[0] = p[1]


def p_stack_init(p):
    '''stack_init : STACK_INIT COLON ID'''
    p[0] = ('stack_init', p[3])


# grammar rule for defining transitions for a FA
#  transitions: [
#         {from: q0, to: q1, on: a},
#         {from: q1, to: q1, on: b},
#         {from: q1, to: q2, on: c}
#     ]

# grammar rule for transition for a PDA
#      transitions: [
#     {from: q0, to: q1, on: a, pop: A, push: AB},
#     {from: q1, to: q1, on: b, pop: A, push: BC},
#     {from: q1, to: q2, on: c, pop: B, push: ε}
# ]
# grammar rule for defining transitions for a FA


# grammar rule for defining a FA
# definition will be like
# fa myfa() {
#     // Define the states
#     states: {q1, q2},

#     // Define the initial state
#     initial: {q1},

#     // Define the final state
#     final: {q2},

#     // Define the transitions
#     transitions: [
#         {from :q1 ,to :q2 ,on: a}
#     ]
# }


# grammar rule for defining a PDA
# initially stack empty
# stack_alphabet is same as alphabet, so no need to define it
# definition will be like
# pda mypda {
#     states: {q0, q1, q2},
#     alphabet: {a, b, c},
#     initial: q0,
#     stack_init:ε,
#     final: q2,
#     transitions: [
#         {from: q0, to: q1, on: a, pop: ε, push: a,stack: a},
#         {from: q1, to: q1, on: b, pop: ε, push: a,stack:aa },
#         {from: q1, to: q2, on: c, pop: ε, push: ε,stack:aa}
#     ]
# }


# grammar rule for defining a context free grammar
# cfg MyGrammar() {
#     nonterminals: A, B, C;
#     terminals: a, b, c;
#     start: A;
#     rules: {
#         A -> B C;
#         B -> a B | ε;
#         C -> b C | c;
#     }
# }

# rules should be like
# rules: {
#         A -> B C;
#         B -> a B | ε;
#         C -> b C | c;
#     }
# use ARROW for -> and PIPE for |

def p_cfg_statement(p):
    '''cfg_statement : CFG ID LPAREN RPAREN LBRACE cfg_body RBRACE'''
    p[0] = ('cfg', p[2], p[6])


def p_cfg_body(p):
    '''cfg_body : nonterminals_statement
                | terminals_statement
                | start_statement
                | rules_statement
                | cfg_body nonterminals_statement
                | cfg_body terminals_statement
                | cfg_body start_statement
                | cfg_body rules_statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_nonterminals_statement(p):
    '''nonterminals_statement : NONTERMINALS COLON LBRACE nonterminals_list RBRACE'''
    p[0] = ('nonterminals', p[3])


def p_nonterminals_list(p):
    '''nonterminals_list : ID
                         | nonterminals_list COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_terminals_statement(p):
    '''terminals_statement : TERMINALS COLON LBRACE terminals_list RBRACE'''
    p[0] = ('terminals', p[3])


def p_terminals_list(p):
    '''terminals_list : ID
                      | terminals_list COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_start_statement(p):
    '''start_statement : START COLON ID'''
    p[0] = ('start', p[3])


def p_rules_statement(p):
    '''rules_statement : RULES COLON LBRACE rules_list RBRACE'''
    p[0] = ('rules', p[3])


def p_rules_list(p):
    '''rules_list : rule
                  | rules_list rule'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_rule(p):
    '''rule : ID ARROW rule_rhs SEMICOLON'''
    p[0] = (p[1], p[3])


def p_rule_rhs(p):
    '''rule_rhs : ID
                | rule_rhs PIPE ID
                | rule_rhs PIPE EPSILON'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_statement_re(p):
    '''statement : RE ID EQUALS SINGLEQUOTE REGEX SINGLEQUOTE'''
    p[0] = ('re', p[2], p[4])


def p_REGEX(p):
    '''REGEX : REGEX_CONTENT'''
    p[0] = p[1]


def p_REGEX_CONTENT(p):
    '''REGEX_CONTENT : REGEX_CONTENT REGEX_CHAR
                     | REGEX_CHAR'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


def p_REGEX_CHAR(p):
    '''REGEX_CHAR : REGEX_SPECIAL_CHAR
                  | REGEX_LITERAL_CHAR'''
    p[0] = p[1]


def p_REGEX_SPECIAL_CHAR(p):
    '''REGEX_SPECIAL_CHAR : STAR
                          | PLUS
                          | OR
                          | DOT
                          | CARET
                          | DOLLAR
                          | QUESTION
                          | LPAREN
                          | RPAREN
                          | LBRACE
                          | RBRACE'''
    p[0] = p[1]


# grammar rule for minimize(myfa) statement


def p_statement_minimize(p):
    '''statement : MINIMIZE LPAREN ID RPAREN'''
    p[0] = ('minimize', p[3])


# grammar rule for simulate(myfa, mystring) statement


def p_statement_simulate(p):
    '''statement : SIMULATE LPAREN ID COMMA ID RPAREN'''
    p[0] = ('simulate', p[3], p[5])


# grammar rule for visualize(myfa) statement
def p_statement_visualize(p):
    '''statement : VISUALIZE LPAREN ID RPAREN'''
    p[0] = ('visualize', p[3])


# grammar rule for concat(myfa1, myfa2) statement


def p_statement_concat(p):
    '''statement : CONCAT LPAREN ID COMMA ID RPAREN'''
    p[0] = ('concat', p[3], p[5])


# grammar rule for power(myfa, n) statement


def p_statement_power(p):
    '''statement : POWER LPAREN ID COMMA NUMBER RPAREN'''
    p[0] = ('power', p[3], p[5])


# grammar rule for kleene(myfa) statement


def p_statement_kleene(p):
    '''statement : KLEENE LPAREN ID RPAREN'''
    p[0] = ('kleene', p[3])


# grammar rule for convert(myfa, mytype) statement
# mytype can be DFA, NFA, DPDA, NPDA,PDA,FA


def p_statement_convert(p):
    '''statement : CONVERT LPAREN ID COMMA ID RPAREN'''
    p[0] = ('convert', p[3], p[5])


# grammmar rule for checkpumpinglemmareg(myfa) statement


def p_statement_checkpumpinglemmareg(p):
    '''statement : CHECKPUMPINGLEMMAREG LPAREN ID RPAREN'''
    p[0] = ('checkpumpinglemmareg', p[3])


# grammar rule for checkpumpinglemmacfl(myfa) statement


def p_statement_checkpumpinglemmacfl(p):
    '''statement : CHECKPUMPINGLEMMACFL LPAREN ID RPAREN'''
    p[0] = ('checkpumpinglemmacfl', p[3])


# grammar rule for isequivalent(myfa1, myfa2) statement


def p_statement_isequivalent(p):
    '''statement : ISEQUIVALENT LPAREN ID COMMA ID RPAREN'''
    p[0] = ('isequivalent', p[3], p[5])


# grammar rule for show(yes/no/regular/isnotregular/cfl/isnotcfl) statement
def p_show_type(p):
    '''show_type : YES
                    | NO
                    | REGULAR
                    | ISNOTREGULAR
                    | CFL
                    | ISNOTCFL
                    | ACCEPT
                    | REJECT'''
    p[0] = p[1]


def p_statement_show(p):
    '''statement : SHOW LPAREN show_type RPAREN'''
    p[0] = ('show', p[3])


# grammar rule for union(myfa1, myfa2) statement
def p_statement_union(p):
    '''statement : UNION LPAREN ID COMMA ID RPAREN'''
    p[0] = ('union', p[3], p[5])


# grammar rule for intersect(myfa1, myfa2) statement
def p_statement_intersect(p):
    '''statement : INTERSECT LPAREN ID COMMA ID RPAREN'''
    p[0] = ('intersect', p[3], p[5])


# grammar rule for complement(myfa) statement
def p_statement_complement(p):
    '''statement : COMPLEMENT LPAREN ID RPAREN'''
    p[0] = ('complement', p[3])


# grammar rule for difference(myfa1, myfa2) statement
def p_statement_difference(p):
    '''statement : DIFF LPAREN ID COMMA ID RPAREN'''
    p[0] = ('difference', p[3], p[5])


# grammar rule for isDFA(myfa) statement
def p_statement_isDfa(p):
    '''statement : ISDFA LPAREN ID RPAREN'''
    p[0] = ('isDFA', p[3])


# grammar rule for isNFA(myfa) statement
def p_statement_isNFA(p):
    '''statement : ISNFA LPAREN ID RPAREN'''
    p[0] = ('isNFA', p[3])


# grammar rule for isDpda(myfa) statement


def p_statement_isDPDA(p):
    '''statement : ISDPDA LPAREN ID RPAREN'''
    p[0] = ('isDPDA', p[3])


# grammar rule for isNpda(myfa) statement


def p_statement_isNPDA(p):
    '''statement : ISNPDA LPAREN ID RPAREN'''
    p[0] = ('isNPDA', p[3])


# grammar rule for if-else statement
# if (condition) {statement} else {statement}
# if (condition) {statement}
# if (condition) {statement} else if (condition) {statement}
# if (condition) {statement} else if (condition) {statement} else {statement}
def p_statement_if_else(p):
    '''statement : IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE
                 | IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE IF LPAREN condition RPAREN LBRACE statement RBRACE
                 | IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE
                 | IF LPAREN condition RPAREN LBRACE statement RBRACE'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    elif len(p) == 13:
        p[0] = ('if-else', p[3], p[6], p[10], p[13])
    elif len(p) == 15:
        p[0] = ('if-else-if-else', p[3], p[6], p[10], p[13], p[16])
    else:
        p[0] = ('if', p[3], p[6])


# grammar rule for condition statement
# condition can be any expression that evaluates to true or false like checkpumpinglemmareg(myfa), checkpumpinglemmacfl(myfa), isequivalent(myfa1, myfa2), isDFA(myfa), isNFA(myfa), isDpda(myfa), isNpda(myfa)
def p_condition(p):
    '''condition : CHECKPUMPINGLEMMAREG
                    | CHECKPUMPINGLEMMACFL
                    | ISEQUIVALENT
                    | ISDFA
                    | ISNFA
                    | ISDPDA
                    | ISNPDA'''
    p[0] = p[1]


# Parsing rules
def p_statement_comment(p):
    '''statement : SLCOMMENT
                  | MLCOMMENT
                  | DOCCOMMENT'''
    pass  # Comments are ignored in parsing


def find_column(lexpos, lexdata):
    last_cr = lexdata.rfind('\n', 0, lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (lexpos - last_cr) + 1
    return column


# Modify the error function to access lexer
def p_error(p):
    if p:
        # Access lexer using p.lexer
        print(
            f"Syntax error at line {p.lineno}, position {find_column(p.lexpos, p.lexer.lexdata)}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")


# Error rule for syntax errors
# Define custom error messages for production rules
parser = yacc.yacc()

# Modify find_column function to accept lexer data

#
# # Test the parser
data = '''
alphabet my_alphabet = {a, b, c}
str my_string = ababac
initial: {q1}
final: {q2, q3}
re my_regex = 'a|(b|x)*'
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

# Parse the input using the parser object
result = parser.parse(data)

# Print the result
for statement in result:
    print(statement)
