class SimpleLangInterpreter:
    def __init__(self):
        self.variables = {}
    
    def parse_and_eval(self, code):
        lines = code.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('let'):
                self.parse_let(line)
            elif line.startswith('print'):
                self.parse_print(line)
    
    def parse_let(self, line):
        # Example: let a = 5;
        parts = line.split('=')
        var_name = parts[0].strip()[4:]  # Remove 'let ' and get the variable name
        expression = parts[1].strip()[:-1]  # Remove the trailing semicolon
        self.variables[var_name] = self.eval_expression(expression)
    
    def parse_print(self, line):
        # Example: print a + b;
        expression = line[6:-1]  # Remove 'print ' and the trailing semicolon
        result = self.eval_expression(expression)
        print(result)
    
    def eval_expression(self, expression):
        # This is a very basic expression evaluator
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            print(f"Error evaluating expression: {expression}")
            print(e)
            return None

# Example usage
code = """
let a = 5;
let b = 10;
let c = a + b;
print c;
"""

interpreter = SimpleLangInterpreter()
interpreter.parse_and_eval(code)
