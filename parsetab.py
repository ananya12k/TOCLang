
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACCEPT ALPHABET ARROW CARET CFG CFL CHECKPUMPINGLEMMACFL CHECKPUMPINGLEMMAREG COLON COMMA COMPLEMENT CONCAT CONVERT DIFF DOCCOMMENT DOLLAR DOT ELSE EPSILON EQUALS FA FINAL FROM ID IF INITIAL INTERSECT ISDFA ISDPDA ISEQUIVALENT ISNFA ISNOTCFL ISNOTREGULAR ISNPDA KLEENE LBRACE LPAREN LSQUARE MINIMIZE MLCOMMENT NO NONTERMINALS NUMBER ONN OR PDA PIPE PLUS POP POWER PUSH QUESTION RBRACE RE REGEX_LITERAL_CHAR REGULAR REJECT RPAREN RSQUARE RULES SEMICOLON SHOW SIMULATE SINGLEQUOTE SLCOMMENT STACK STACK_INIT STAR START STATES STR STRING TERMINALS TO TRANSITIONS UNION VISUALIZE YESstatement : ALPHABET ID EQUALS LBRACE alphabet_list RBRACEalphabet_list : ID\n                     | alphabet_list COMMA IDstatement : STR ID EQUALS SINGLEQUOTE STRING SINGLEQUOTEstatement : INITIAL COLON LBRACE ID RBRACEstatement : FINAL COLON LBRACE final_list RBRACEfinal_list : ID\n                  | final_list COMMA IDstatement : STATES COLON LBRACE states_list RBRACEstates_list : ID\n                   | states_list COMMA IDstatement : TRANSITIONS COLON LBRACE transitions_list RBRACEtransitions_list : transition\n                        | transitions_list COMMA transitiontransition : LSQUARE FROM COLON ID COMMA TO COLON ID COMMA ONN COLON ID RSQUARE\n                   | LSQUARE FROM COLON ID COMMA TO COLON ID COMMA ONN COLON ID COMMA POP COLON ID COMMA PUSH COLON ID COMMA STACK COLON ID RSQUAREstatement : FA ID LPAREN RPAREN LBRACE statement_list_fa RBRACEstatement_list_fa : statement\n                      | statement_list_fa statementstatement : PDA ID LPAREN RPAREN LBRACE statement_list_pda RBRACEstatement_list_pda : statement\n                          | statement_list_pda statementstatement : STACK_INIT COLON IDstatement : CFG ID LPAREN RPAREN LBRACE statement_list_cfg RBRACEstatement_list_cfg : statement\n                      | statement_list_cfg statementstatement : NONTERMINALS COLON LBRACE nonterminals_list RBRACEnonterminals_list : ID\n                   | nonterminals_list COMMA IDstatement : TERMINALS COLON LBRACE terminals_list RBRACEterminals_list : ID\n                   | terminals_list COMMA IDstatement : START COLON IDstatement : RULES COLON LBRACE rules_list RBRACErules_list : rule\n                  | rules_list rulerule : ID ARROW rule_rhs SEMICOLONrule_rhs : ID\n                | rule_rhs PIPE ID\n                | rule_rhs PIPE EPSILONstatement : RE ID EQUALS SINGLEQUOTE REGEX SINGLEQUOTEREGEX : REGEX_CONTENTREGEX_CONTENT : REGEX_CONTENT REGEX_CHAR\n                     | REGEX_CHARREGEX_CHAR : REGEX_SPECIAL_CHAR\n                  | REGEX_LITERAL_CHARREGEX_SPECIAL_CHAR : STAR\n                          | PLUS\n                          | OR\n                          | DOT\n                          | CARET\n                          | DOLLAR\n                          | QUESTION\n                          | LPAREN\n                          | RPAREN\n                          | LBRACE\n                          | RBRACEstatement : MINIMIZE LPAREN ID RPARENstatement : SIMULATE LPAREN ID COMMA ID RPARENstatement : VISUALIZE LPAREN ID RPARENstatement : CONCAT LPAREN ID COMMA ID RPARENstatement : POWER LPAREN ID COMMA NUMBER RPARENstatement : KLEENE LPAREN ID RPARENstatement : CONVERT LPAREN ID COMMA ID RPARENstatement : CHECKPUMPINGLEMMAREG LPAREN ID RPARENstatement : CHECKPUMPINGLEMMACFL LPAREN ID RPARENstatement : ISEQUIVALENT LPAREN ID COMMA ID RPARENshow_type : YES\n                    | NO\n                    | REGULAR\n                    | ISNOTREGULAR\n                    | CFL\n                    | ISNOTCFL\n                    | ACCEPT\n                    | REJECTstatement : SHOW LPAREN show_type RPARENstatement : UNION LPAREN ID COMMA ID RPARENstatement : INTERSECT LPAREN ID COMMA ID RPARENstatement : COMPLEMENT LPAREN ID RPARENstatement : DIFF LPAREN ID COMMA ID RPARENstatement : ISDFA LPAREN ID RPARENstatement : ISNFA LPAREN ID RPARENstatement : ISDPDA LPAREN ID RPARENstatement : ISNPDA LPAREN ID RPARENstatement : IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE\n                 | IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE IF LPAREN condition RPAREN LBRACE statement RBRACE\n                 | IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE\n                 | IF LPAREN condition RPAREN LBRACE statement RBRACEcondition : CHECKPUMPINGLEMMAREG\n                    | CHECKPUMPINGLEMMACFL\n                    | ISEQUIVALENT\n                    | ISDFA\n                    | ISNFA\n                    | ISDPDA\n                    | ISNPDAstatement : SLCOMMENT\n                  | MLCOMMENT\n                  | DOCCOMMENT'
    
_lr_action_items = {'ALPHABET':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[2,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,2,2,2,-27,-30,-34,2,-1,-4,2,-18,2,-21,2,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,2,-85,2,-86,2,-87,]),'STR':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[3,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,3,3,3,-27,-30,-34,3,-1,-4,3,-18,3,-21,3,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,3,-85,3,-86,3,-87,]),'INITIAL':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[4,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,4,4,4,-27,-30,-34,4,-1,-4,4,-18,4,-21,4,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,4,-85,4,-86,4,-87,]),'FINAL':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[5,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,5,5,5,-27,-30,-34,5,-1,-4,5,-18,5,-21,5,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,5,-85,5,-86,5,-87,]),'STATES':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[6,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,6,6,6,-27,-30,-34,6,-1,-4,6,-18,6,-21,6,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,6,-85,6,-86,6,-87,]),'TRANSITIONS':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[7,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,7,7,7,-27,-30,-34,7,-1,-4,7,-18,7,-21,7,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,7,-85,7,-86,7,-87,]),'FA':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[8,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,8,8,8,-27,-30,-34,8,-1,-4,8,-18,8,-21,8,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,8,-85,8,-86,8,-87,]),'PDA':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[9,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,9,9,9,-27,-30,-34,9,-1,-4,9,-18,9,-21,9,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,9,-85,9,-86,9,-87,]),'STACK_INIT':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[10,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,10,10,10,-27,-30,-34,10,-1,-4,10,-18,10,-21,10,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,10,-85,10,-86,10,-87,]),'CFG':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[11,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,11,11,11,-27,-30,-34,11,-1,-4,11,-18,11,-21,11,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,11,-85,11,-86,11,-87,]),'NONTERMINALS':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[12,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,12,12,12,-27,-30,-34,12,-1,-4,12,-18,12,-21,12,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,12,-85,12,-86,12,-87,]),'TERMINALS':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[13,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,13,13,13,-27,-30,-34,13,-1,-4,13,-18,13,-21,13,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,13,-85,13,-86,13,-87,]),'START':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[14,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,14,14,14,-27,-30,-34,14,-1,-4,14,-18,14,-21,14,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,14,-85,14,-86,14,-87,]),'RULES':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[15,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,15,15,15,-27,-30,-34,15,-1,-4,15,-18,15,-21,15,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,15,-85,15,-86,15,-87,]),'RE':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[16,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,16,16,16,-27,-30,-34,16,-1,-4,16,-18,16,-21,16,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,16,-85,16,-86,16,-87,]),'MINIMIZE':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[17,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,17,17,17,-27,-30,-34,17,-1,-4,17,-18,17,-21,17,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,17,-85,17,-86,17,-87,]),'SIMULATE':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[18,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,18,18,18,-27,-30,-34,18,-1,-4,18,-18,18,-21,18,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,18,-85,18,-86,18,-87,]),'VISUALIZE':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[19,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,19,19,19,-27,-30,-34,19,-1,-4,19,-18,19,-21,19,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,19,-85,19,-86,19,-87,]),'CONCAT':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[20,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,20,20,20,-27,-30,-34,20,-1,-4,20,-18,20,-21,20,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,20,-85,20,-86,20,-87,]),'POWER':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[21,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,21,21,21,-27,-30,-34,21,-1,-4,21,-18,21,-21,21,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,21,-85,21,-86,21,-87,]),'KLEENE':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[22,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,22,22,22,-27,-30,-34,22,-1,-4,22,-18,22,-21,22,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,22,-85,22,-86,22,-87,]),'CONVERT':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[23,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,23,23,23,-27,-30,-34,23,-1,-4,23,-18,23,-21,23,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,23,-85,23,-86,23,-87,]),'CHECKPUMPINGLEMMAREG':([0,37,38,39,74,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,259,263,267,271,276,280,],[24,-96,-97,-98,118,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,24,24,24,-27,-30,-34,24,-1,-4,24,-18,24,-21,24,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,24,118,-85,24,-86,24,-87,]),'CHECKPUMPINGLEMMACFL':([0,37,38,39,74,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,259,263,267,271,276,280,],[25,-96,-97,-98,119,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,25,25,25,-27,-30,-34,25,-1,-4,25,-18,25,-21,25,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,25,119,-85,25,-86,25,-87,]),'ISEQUIVALENT':([0,37,38,39,74,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,259,263,267,271,276,280,],[26,-96,-97,-98,120,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,26,26,26,-27,-30,-34,26,-1,-4,26,-18,26,-21,26,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,26,120,-85,26,-86,26,-87,]),'SHOW':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[27,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,27,27,27,-27,-30,-34,27,-1,-4,27,-18,27,-21,27,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,27,-85,27,-86,27,-87,]),'UNION':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[28,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,28,28,28,-27,-30,-34,28,-1,-4,28,-18,28,-21,28,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,28,-85,28,-86,28,-87,]),'INTERSECT':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[29,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,29,29,29,-27,-30,-34,29,-1,-4,29,-18,29,-21,29,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,29,-85,29,-86,29,-87,]),'COMPLEMENT':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[30,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,30,30,30,-27,-30,-34,30,-1,-4,30,-18,30,-21,30,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,30,-85,30,-86,30,-87,]),'DIFF':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[31,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,31,31,31,-27,-30,-34,31,-1,-4,31,-18,31,-21,31,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,31,-85,31,-86,31,-87,]),'ISDFA':([0,37,38,39,74,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,259,263,267,271,276,280,],[32,-96,-97,-98,121,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,32,32,32,-27,-30,-34,32,-1,-4,32,-18,32,-21,32,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,32,121,-85,32,-86,32,-87,]),'ISNFA':([0,37,38,39,74,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,259,263,267,271,276,280,],[33,-96,-97,-98,122,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,33,33,33,-27,-30,-34,33,-1,-4,33,-18,33,-21,33,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,33,122,-85,33,-86,33,-87,]),'ISDPDA':([0,37,38,39,74,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,259,263,267,271,276,280,],[34,-96,-97,-98,123,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,34,34,34,-27,-30,-34,34,-1,-4,34,-18,34,-21,34,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,34,123,-85,34,-86,34,-87,]),'ISNPDA':([0,37,38,39,74,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,259,263,267,271,276,280,],[35,-96,-97,-98,124,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,35,35,35,-27,-30,-34,35,-1,-4,35,-18,35,-21,35,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,35,124,-85,35,-86,35,-87,]),'IF':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,254,257,263,267,271,276,280,],[36,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,36,36,36,-27,-30,-34,36,-1,-4,36,-18,36,-21,36,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,256,36,-85,36,-86,36,-87,]),'SLCOMMENT':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[37,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,37,37,37,-27,-30,-34,37,-1,-4,37,-18,37,-21,37,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,37,-85,37,-86,37,-87,]),'MLCOMMENT':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[38,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,38,38,38,-27,-30,-34,38,-1,-4,38,-18,38,-21,38,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,38,-85,38,-86,38,-87,]),'DOCCOMMENT':([0,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,177,178,179,180,182,184,211,212,214,219,220,221,222,223,224,229,231,232,233,234,235,236,237,238,242,243,244,245,246,247,250,257,263,267,271,276,280,],[39,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,39,39,39,-27,-30,-34,39,-1,-4,39,-18,39,-21,39,-25,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-19,-20,-22,-24,-26,-88,39,-85,39,-86,39,-87,]),'$end':([1,37,38,39,83,87,146,148,151,153,154,156,159,161,162,163,164,169,170,172,174,180,182,184,212,214,229,231,232,233,234,235,236,237,238,242,244,246,250,263,271,280,],[0,-96,-97,-98,-23,-33,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-5,-6,-9,-12,-27,-30,-34,-1,-4,-41,-59,-61,-62,-64,-67,-77,-78,-80,-17,-20,-24,-88,-85,-86,-87,]),'ID':([2,3,8,9,11,16,48,52,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,77,78,79,85,86,88,125,142,143,147,149,152,155,157,158,160,171,173,181,183,185,186,213,218,248,249,258,268,277,283,287,],[40,41,46,47,49,54,83,87,90,91,92,93,94,95,96,97,98,99,109,110,111,112,113,114,115,116,127,129,131,139,141,144,166,144,-35,203,204,206,207,208,209,210,215,216,225,226,-36,227,240,241,-37,252,261,270,279,284,288,]),'COLON':([4,5,6,7,10,12,13,14,15,176,255,266,275,282,286,],[42,43,44,45,48,50,51,52,53,218,258,268,277,283,287,]),'LPAREN':([17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,46,47,49,145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,256,],[55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,81,82,84,199,199,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,259,]),'RBRACE':([37,38,39,83,87,127,128,129,130,131,132,133,138,139,140,141,142,143,145,146,148,151,153,154,156,159,161,162,163,164,166,167,169,170,172,174,180,182,184,185,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,212,214,215,216,217,219,220,221,222,223,224,225,226,229,230,231,232,233,234,235,236,237,238,239,240,242,243,244,245,246,247,248,250,260,263,269,271,273,278,280,289,],[-96,-97,-98,-23,-33,169,170,-7,172,-10,174,-13,180,-28,182,-31,184,-35,202,-58,-60,-63,-65,-66,-76,-79,-81,-82,-83,-84,-2,212,-5,-6,-9,-12,-27,-30,-34,-36,202,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-1,-4,-8,-11,-14,242,-18,244,-21,246,-25,-29,-32,-41,-43,-59,-61,-62,-64,-67,-77,-78,-80,250,-3,-17,-19,-20,-22,-24,-26,-37,-88,263,-85,271,-86,-15,280,-87,-16,]),'EQUALS':([40,41,54,],[75,76,89,]),'LBRACE':([42,43,44,45,50,51,53,75,135,136,137,145,165,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,254,265,274,],[77,78,79,80,85,86,88,125,177,178,179,201,211,201,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,257,267,276,]),'YES':([65,],[101,]),'NO':([65,],[102,]),'REGULAR':([65,],[103,]),'ISNOTREGULAR':([65,],[104,]),'CFL':([65,],[105,]),'ISNOTCFL':([65,],[106,]),'ACCEPT':([65,],[107,]),'REJECT':([65,],[108,]),'SINGLEQUOTE':([76,89,168,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[126,145,214,229,-42,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'LSQUARE':([80,175,],[134,134,]),'RPAREN':([81,82,84,90,92,95,97,98,100,101,102,103,104,105,106,107,108,111,113,114,115,116,117,118,119,120,121,122,123,124,145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,230,262,],[135,136,137,146,148,151,153,154,156,-68,-69,-70,-71,-72,-73,-74,-75,159,161,162,163,164,165,-89,-90,-91,-92,-93,-94,-95,200,200,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,231,232,233,234,235,236,237,238,-43,265,]),'COMMA':([91,93,94,96,99,109,110,112,128,129,130,131,132,133,138,139,140,141,166,167,215,216,217,225,226,240,241,261,270,273,279,284,289,],[147,149,150,152,155,157,158,160,171,-7,173,-10,175,-13,181,-28,183,-31,-2,213,-8,-11,-14,-29,-32,-3,251,264,272,-15,281,285,-16,]),'STRING':([126,],[168,]),'FROM':([134,],[176,]),'ARROW':([144,],[186,]),'REGEX_LITERAL_CHAR':([145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[191,191,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'STAR':([145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[192,192,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'PLUS':([145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[193,193,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'OR':([145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[194,194,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'DOT':([145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[195,195,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'CARET':([145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[196,196,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'DOLLAR':([145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[197,197,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'QUESTION':([145,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,230,],[198,198,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-43,]),'NUMBER':([150,],[205,]),'SEMICOLON':([227,228,252,253,],[-38,248,-39,-40,]),'PIPE':([227,228,252,253,],[-38,249,-39,-40,]),'EPSILON':([249,],[253,]),'ELSE':([250,271,],[254,274,]),'TO':([251,],[255,]),'ONN':([264,],[266,]),'RSQUARE':([270,288,],[273,289,]),'POP':([272,],[275,]),'PUSH':([281,],[282,]),'STACK':([285,],[286,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,177,178,179,211,219,221,223,257,267,276,],[1,220,222,224,239,243,245,247,260,269,278,]),'show_type':([65,],[100,]),'condition':([74,259,],[117,262,]),'final_list':([78,],[128,]),'states_list':([79,],[130,]),'transitions_list':([80,],[132,]),'transition':([80,175,],[133,217,]),'nonterminals_list':([85,],[138,]),'terminals_list':([86,],[140,]),'rules_list':([88,],[142,]),'rule':([88,142,],[143,185,]),'alphabet_list':([125,],[167,]),'REGEX':([145,],[187,]),'REGEX_CONTENT':([145,],[188,]),'REGEX_CHAR':([145,188,],[189,230,]),'REGEX_SPECIAL_CHAR':([145,188,],[190,190,]),'statement_list_fa':([177,],[219,]),'statement_list_pda':([178,],[221,]),'statement_list_cfg':([179,],[223,]),'rule_rhs':([186,],[228,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ALPHABET ID EQUALS LBRACE alphabet_list RBRACE','statement',6,'p_statement_alphabet','parsertoc.py',9),
  ('alphabet_list -> ID','alphabet_list',1,'p_alphabet_list','parsertoc.py',14),
  ('alphabet_list -> alphabet_list COMMA ID','alphabet_list',3,'p_alphabet_list','parsertoc.py',15),
  ('statement -> STR ID EQUALS SINGLEQUOTE STRING SINGLEQUOTE','statement',6,'p_statement_str','parsertoc.py',23),
  ('statement -> INITIAL COLON LBRACE ID RBRACE','statement',5,'p_statement_initial','parsertoc.py',28),
  ('statement -> FINAL COLON LBRACE final_list RBRACE','statement',5,'p_statement_final','parsertoc.py',33),
  ('final_list -> ID','final_list',1,'p_final_list','parsertoc.py',38),
  ('final_list -> final_list COMMA ID','final_list',3,'p_final_list','parsertoc.py',39),
  ('statement -> STATES COLON LBRACE states_list RBRACE','statement',5,'p_statement_states','parsertoc.py',49),
  ('states_list -> ID','states_list',1,'p_states_list','parsertoc.py',54),
  ('states_list -> states_list COMMA ID','states_list',3,'p_states_list','parsertoc.py',55),
  ('statement -> TRANSITIONS COLON LBRACE transitions_list RBRACE','statement',5,'p_statement_transitions','parsertoc.py',77),
  ('transitions_list -> transition','transitions_list',1,'p_transitions_list','parsertoc.py',82),
  ('transitions_list -> transitions_list COMMA transition','transitions_list',3,'p_transitions_list','parsertoc.py',83),
  ('transition -> LSQUARE FROM COLON ID COMMA TO COLON ID COMMA ONN COLON ID RSQUARE','transition',13,'p_transition','parsertoc.py',91),
  ('transition -> LSQUARE FROM COLON ID COMMA TO COLON ID COMMA ONN COLON ID COMMA POP COLON ID COMMA PUSH COLON ID COMMA STACK COLON ID RSQUARE','transition',25,'p_transition','parsertoc.py',92),
  ('statement -> FA ID LPAREN RPAREN LBRACE statement_list_fa RBRACE','statement',7,'p_statement_fa','parsertoc.py',117),
  ('statement_list_fa -> statement','statement_list_fa',1,'p_statement_list_fa','parsertoc.py',122),
  ('statement_list_fa -> statement_list_fa statement','statement_list_fa',2,'p_statement_list_fa','parsertoc.py',123),
  ('statement -> PDA ID LPAREN RPAREN LBRACE statement_list_pda RBRACE','statement',7,'p_statement_pda','parsertoc.py',147),
  ('statement_list_pda -> statement','statement_list_pda',1,'p_statement_list_pda','parsertoc.py',152),
  ('statement_list_pda -> statement_list_pda statement','statement_list_pda',2,'p_statement_list_pda','parsertoc.py',153),
  ('statement -> STACK_INIT COLON ID','statement',3,'p_statement_stack_init','parsertoc.py',161),
  ('statement -> CFG ID LPAREN RPAREN LBRACE statement_list_cfg RBRACE','statement',7,'p_statement_cfg','parsertoc.py',179),
  ('statement_list_cfg -> statement','statement_list_cfg',1,'p_statement_list_cfg','parsertoc.py',184),
  ('statement_list_cfg -> statement_list_cfg statement','statement_list_cfg',2,'p_statement_list_cfg','parsertoc.py',185),
  ('statement -> NONTERMINALS COLON LBRACE nonterminals_list RBRACE','statement',5,'p_statement_nonterminals','parsertoc.py',193),
  ('nonterminals_list -> ID','nonterminals_list',1,'p_nonterminals_list','parsertoc.py',198),
  ('nonterminals_list -> nonterminals_list COMMA ID','nonterminals_list',3,'p_nonterminals_list','parsertoc.py',199),
  ('statement -> TERMINALS COLON LBRACE terminals_list RBRACE','statement',5,'p_statement_terminals','parsertoc.py',207),
  ('terminals_list -> ID','terminals_list',1,'p_terminals_list','parsertoc.py',212),
  ('terminals_list -> terminals_list COMMA ID','terminals_list',3,'p_terminals_list','parsertoc.py',213),
  ('statement -> START COLON ID','statement',3,'p_statement_start','parsertoc.py',221),
  ('statement -> RULES COLON LBRACE rules_list RBRACE','statement',5,'p_statement_rules','parsertoc.py',235),
  ('rules_list -> rule','rules_list',1,'p_rules_list','parsertoc.py',240),
  ('rules_list -> rules_list rule','rules_list',2,'p_rules_list','parsertoc.py',241),
  ('rule -> ID ARROW rule_rhs SEMICOLON','rule',4,'p_rule','parsertoc.py',249),
  ('rule_rhs -> ID','rule_rhs',1,'p_rule_rhs','parsertoc.py',254),
  ('rule_rhs -> rule_rhs PIPE ID','rule_rhs',3,'p_rule_rhs','parsertoc.py',255),
  ('rule_rhs -> rule_rhs PIPE EPSILON','rule_rhs',3,'p_rule_rhs','parsertoc.py',256),
  ('statement -> RE ID EQUALS SINGLEQUOTE REGEX SINGLEQUOTE','statement',6,'p_statement_re','parsertoc.py',264),
  ('REGEX -> REGEX_CONTENT','REGEX',1,'p_REGEX','parsertoc.py',269),
  ('REGEX_CONTENT -> REGEX_CONTENT REGEX_CHAR','REGEX_CONTENT',2,'p_REGEX_CONTENT','parsertoc.py',274),
  ('REGEX_CONTENT -> REGEX_CHAR','REGEX_CONTENT',1,'p_REGEX_CONTENT','parsertoc.py',275),
  ('REGEX_CHAR -> REGEX_SPECIAL_CHAR','REGEX_CHAR',1,'p_REGEX_CHAR','parsertoc.py',283),
  ('REGEX_CHAR -> REGEX_LITERAL_CHAR','REGEX_CHAR',1,'p_REGEX_CHAR','parsertoc.py',284),
  ('REGEX_SPECIAL_CHAR -> STAR','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',289),
  ('REGEX_SPECIAL_CHAR -> PLUS','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',290),
  ('REGEX_SPECIAL_CHAR -> OR','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',291),
  ('REGEX_SPECIAL_CHAR -> DOT','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',292),
  ('REGEX_SPECIAL_CHAR -> CARET','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',293),
  ('REGEX_SPECIAL_CHAR -> DOLLAR','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',294),
  ('REGEX_SPECIAL_CHAR -> QUESTION','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',295),
  ('REGEX_SPECIAL_CHAR -> LPAREN','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',296),
  ('REGEX_SPECIAL_CHAR -> RPAREN','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',297),
  ('REGEX_SPECIAL_CHAR -> LBRACE','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',298),
  ('REGEX_SPECIAL_CHAR -> RBRACE','REGEX_SPECIAL_CHAR',1,'p_REGEX_SPECIAL_CHAR','parsertoc.py',299),
  ('statement -> MINIMIZE LPAREN ID RPAREN','statement',4,'p_statement_minimize','parsertoc.py',307),
  ('statement -> SIMULATE LPAREN ID COMMA ID RPAREN','statement',6,'p_statement_simulate','parsertoc.py',315),
  ('statement -> VISUALIZE LPAREN ID RPAREN','statement',4,'p_statement_visualize','parsertoc.py',321),
  ('statement -> CONCAT LPAREN ID COMMA ID RPAREN','statement',6,'p_statement_concat','parsertoc.py',329),
  ('statement -> POWER LPAREN ID COMMA NUMBER RPAREN','statement',6,'p_statement_power','parsertoc.py',337),
  ('statement -> KLEENE LPAREN ID RPAREN','statement',4,'p_statement_kleene','parsertoc.py',345),
  ('statement -> CONVERT LPAREN ID COMMA ID RPAREN','statement',6,'p_statement_convert','parsertoc.py',354),
  ('statement -> CHECKPUMPINGLEMMAREG LPAREN ID RPAREN','statement',4,'p_statement_checkpumpinglemmareg','parsertoc.py',362),
  ('statement -> CHECKPUMPINGLEMMACFL LPAREN ID RPAREN','statement',4,'p_statement_checkpumpinglemmacfl','parsertoc.py',370),
  ('statement -> ISEQUIVALENT LPAREN ID COMMA ID RPAREN','statement',6,'p_statement_isequivalent','parsertoc.py',378),
  ('show_type -> YES','show_type',1,'p_show_type','parsertoc.py',384),
  ('show_type -> NO','show_type',1,'p_show_type','parsertoc.py',385),
  ('show_type -> REGULAR','show_type',1,'p_show_type','parsertoc.py',386),
  ('show_type -> ISNOTREGULAR','show_type',1,'p_show_type','parsertoc.py',387),
  ('show_type -> CFL','show_type',1,'p_show_type','parsertoc.py',388),
  ('show_type -> ISNOTCFL','show_type',1,'p_show_type','parsertoc.py',389),
  ('show_type -> ACCEPT','show_type',1,'p_show_type','parsertoc.py',390),
  ('show_type -> REJECT','show_type',1,'p_show_type','parsertoc.py',391),
  ('statement -> SHOW LPAREN show_type RPAREN','statement',4,'p_statement_show','parsertoc.py',396),
  ('statement -> UNION LPAREN ID COMMA ID RPAREN','statement',6,'p_statement_union','parsertoc.py',402),
  ('statement -> INTERSECT LPAREN ID COMMA ID RPAREN','statement',6,'p_statement_intersect','parsertoc.py',408),
  ('statement -> COMPLEMENT LPAREN ID RPAREN','statement',4,'p_statement_complement','parsertoc.py',414),
  ('statement -> DIFF LPAREN ID COMMA ID RPAREN','statement',6,'p_statement_difference','parsertoc.py',420),
  ('statement -> ISDFA LPAREN ID RPAREN','statement',4,'p_statement_isDfa','parsertoc.py',426),
  ('statement -> ISNFA LPAREN ID RPAREN','statement',4,'p_statement_isNFA','parsertoc.py',432),
  ('statement -> ISDPDA LPAREN ID RPAREN','statement',4,'p_statement_isDPDA','parsertoc.py',440),
  ('statement -> ISNPDA LPAREN ID RPAREN','statement',4,'p_statement_isNPDA','parsertoc.py',448),
  ('statement -> IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE','statement',11,'p_statement_if_else','parsertoc.py',458),
  ('statement -> IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE IF LPAREN condition RPAREN LBRACE statement RBRACE','statement',15,'p_statement_if_else','parsertoc.py',459),
  ('statement -> IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE IF LPAREN condition RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE','statement',19,'p_statement_if_else','parsertoc.py',460),
  ('statement -> IF LPAREN condition RPAREN LBRACE statement RBRACE','statement',7,'p_statement_if_else','parsertoc.py',461),
  ('condition -> CHECKPUMPINGLEMMAREG','condition',1,'p_condition','parsertoc.py',475),
  ('condition -> CHECKPUMPINGLEMMACFL','condition',1,'p_condition','parsertoc.py',476),
  ('condition -> ISEQUIVALENT','condition',1,'p_condition','parsertoc.py',477),
  ('condition -> ISDFA','condition',1,'p_condition','parsertoc.py',478),
  ('condition -> ISNFA','condition',1,'p_condition','parsertoc.py',479),
  ('condition -> ISDPDA','condition',1,'p_condition','parsertoc.py',480),
  ('condition -> ISNPDA','condition',1,'p_condition','parsertoc.py',481),
  ('statement -> SLCOMMENT','statement',1,'p_statement_comment','parsertoc.py',487),
  ('statement -> MLCOMMENT','statement',1,'p_statement_comment','parsertoc.py',488),
  ('statement -> DOCCOMMENT','statement',1,'p_statement_comment','parsertoc.py',489),
]
