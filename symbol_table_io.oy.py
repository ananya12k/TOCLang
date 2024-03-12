import json
from symbol_table import SymbolTable


class SymbolTableIO:
    @staticmethod
    def save_symbol_table(symbol_table, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(symbol_table.get_all_symbols(), file)
            print(f"Symbol table saved to {filename}")
        except Exception as e:
            print(f"Error while saving symbol table: {e}")

    @staticmethod
    def load_symbol_table(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                symbol_table = SymbolTable()
                for identifier, value in data.items():
                    symbol_table.add_symbol(identifier, value)
            print(f"Symbol table loaded from {filename}")
            return symbol_table
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error while loading symbol table: {e}")

# Usage example:
# symbol_table = SymbolTable()
# symbol_table.add_symbol('x', 10)
# symbol_table.add_symbol('y', 20)
# SymbolTableIO.save_symbol_table(symbol_table, 'symbol_table.json')
# loaded_symbol_table = SymbolTableIO.load_symbol_table('symbol_table.json')
# if loaded_symbol_table:
#     print(loaded_symbol_table.get_all_symbols())
