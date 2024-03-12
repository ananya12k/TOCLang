from symbol_table_io import SymbolTableIO
from fa_simulator import FASimulator
from pda_simulator import PDASimulator
from fa_visualizer import FAVisualizer


class Interpreter:
    def __init__(self):
        self.symbol_table = SymbolTableIO.load_symbol_table('symbol_table.json')
        self.fas = {}

    def interpret(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("//"):  # Skip comments
                    continue
                if line.startswith("alphabet"):
                    self.handle_alphabet(line)
                elif line.startswith("str"):
                    self.handle_string(line)
                elif line.startswith("fa"):
                    self.handle_fa(line)
                elif line.startswith("simulate"):
                    self.handle_fa_simulation(line)
                elif line.startswith("visualize"):
                    self.handle_fa_visualization(line)
                elif line.startswith("pda"):
                    self.handle_pda(line)

    def handle_alphabet(self, line):
        parts = line.split("=")
        identifier = parts[0].split()[1]
        symbols = parts[1].strip("{}").split(",")
        self.symbol_table.add_symbol(identifier, symbols)
        print(f"Alphabet {identifier} defined with symbols {symbols}")

    def handle_string(self, line):
        parts = line.split("=")
        identifier = parts[0].split()[1]
        value = parts[1].strip("'")
        if identifier in self.symbol_table.get_all_symbols():
            declared_alphabet = self.symbol_table.get_value(identifier)
            for char in value:
                if char not in declared_alphabet:
                    print(f"Semantic Error: Symbol '{char}' in string is not in the declared alphabet")
        else:
            print(f"Semantic Error: Unknown alphabet identifier '{identifier}' in string declaration")

    def handle_fa(self, line):
        parts = line.split()
        fa_name = parts[1]
        states = None
        initial = None
        final = None
        transitions = None
        for subline in parts[2:]:
            if subline == "states:":
                states = parts[parts.index(subline) + 1].strip("{}").split(",")
            elif subline == "initial:":
                initial = parts[parts.index(subline) + 1].strip("{}").split(",")
            elif subline == "final:":
                final = parts[parts.index(subline) + 1].strip("{}").split(",")
            elif subline == "transitions:":
                transitions = []
                for transition in parts[parts.index(subline) + 1:]:
                    if transition.startswith("["):
                        transition = transition.strip("[],")
                        from_state, to_state, on_symbol = transition.split(":")
                        transitions.append((from_state.strip(), to_state.strip(), on_symbol.strip()))
                    else:
                        break
        self.fas[fa_name] = {"states": states, "initial": initial, "final": final, "transitions": transitions}
        print(f"FA {fa_name} defined")

    def handle_fa_simulation(self, line):
        parts = line.split()
        fa_name = parts[1]
        if fa_name in self.fas:
            fa_simulator = FASimulator(self.fas[fa_name]["states"], self.fas[fa_name]["initial"],
                                       self.fas[fa_name]["final"], self.fas[fa_name]["transitions"])
            fa_simulator.simulate()
        else:
            print(f"Semantic Error: FA '{fa_name}' not found")

    def handle_fa_visualization(self, line):
        parts = line.split()
        fa_name = parts[1]
        if fa_name in self.fas:
            fa_visualizer = FAVisualizer(self.fas[fa_name]["states"], self.fas[fa_name]["initial"],
                                         self.fas[fa_name]["final"], self.fas[fa_name]["transitions"])
            fa_visualizer.visualize()
        else:
            print(f"Semantic Error: FA '{fa_name}' not found")

    def handle_pda(self, line):
        # Similar logic to handle_fa, handle_fa_simulation, and handle_fa_visualization for PDAs
        pass


# Usage
interpreter = Interpreter()
interpreter.interpret("myfile.toc")
