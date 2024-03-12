class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, identifier, value):
        if identifier in self.symbols:
            print(f"Semantic Error: Duplicate identifier '{identifier}'")
            return False
        self.symbols[identifier] = value
        return True

    def get_value(self, identifier):
        return self.symbols.get(identifier, None)

    def remove_symbol(self, identifier):
        if identifier in self.symbols:
            del self.symbols[identifier]
            return True
        return False

    def clear(self):
        self.symbols.clear()

    def get_all_symbols(self):
        return self.symbols.copy()

    def __str__(self):
        return str(self.symbols)

# Usage example:
# symbol_table = SymbolTable()
# symbol_table.add_symbol('x', 10)
# symbol_table.add_symbol('y', 20)
# print(symbol_table.get_value('x'))
# print(symbol_table.get_value('z'))  # This will return None
# print(symbol_table)
# symbol_table.remove_symbol('x')
# print(symbol_table)
# symbol_table.clear()
# print(symbol_table)
# symbols = symbol_table.get_all_symbols()
# print(symbols)
