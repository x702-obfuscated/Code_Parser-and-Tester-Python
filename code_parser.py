import ast,os,time
#class for grading a single file
class Code_Parser:

  def __init__(self,code):
    #abstract syntax tree
    self.set_tree(code)
    
    #Values to be checked
    self.variables = {} #name: (value, function name)
    self.functions = {} #name: (parameters, arguments)

    #Results
    self.declared_variables = {} #name : (value, function name)
    self.defined_functions = {} #name : parameters
    self.called_functions = {} #name : arguments
    self.feedback = set()
    self.score = 0

  #Parses the provided code 
  def parse (self):
    try:
      for node in ast.walk(self.tree):

        #checks defined function and variables defined inside of functions
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
          #Add function definition to defined_functions list
          self.handle_functions(node)

          for function_node in node.body:
            if isinstance(function_node, ast.Assign):
              self.handle_variables(function_node)
        

        #Check function calls at module level
        elif isinstance(node,ast.Call):
          self.handle_functions(node)
        
        #Check variables declaration and assignment
        elif isinstance(node,ast.Assign):
          self.handle_variables(node)



    except SyntaxError as e:
      print(f"SyntaxError: {e}")

  #Checks defined variables and thier values at the module level
  #Checks defined variables and thier values at the function level
  def handle_variables(self, node):
    for target in node.targets:
      if isinstance(target, ast.Name):
        variable_name = target.id
        
        #Checks the value of the variable
        value = ast.literal_eval(node.value)
        if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
          self.declared_variables[variable_name] = (value, node.name)
        else:
          self.declared_variables[variable_name] = (value, None)

  #Checks defined Functions and their parameters
  #Checks called Functions and their arguments
  def handle_functions(self, node):
    if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef))
      if len(node.args.args) > 0:
        self.defined_functions[node.name] = [param.arg for param in node.args.args]
      else:
        self.defined_functions[node.name] = None
    elif isinstance(node,ast.Call):
      if hasattr(node.func, "id"):
        self.called_functions[node.func.id] = [arg for arg in node.args]

  def check_variables(self):
    for variable in self.variables:
      expected_value = self.variables[variable][0]
      expected_scope = self.variables[variable][1]

      #Checks if variables is declared
      if variable in self.declared_variables:
        
        actual_value = self.declared_variables[variable][0]
        actual_scope = self.declared_variables[variable][1]

        #Correct
        feedback = f"'{variable}' is declared. "
        
        #Checks if the variable is in the correct function
        if expected_scope != None or actual_scope != None:
          if expected_scope == None:
            feedback += f"'{variable}' is inside a function, but should not be inside a function. "
          elif expected_scope == actual_scope:
            #Correct
            feedback += f"'{variable}' is in the function '{actual_scope}'. "
          else:
            feedback += f"'{variable}' is in the wrong place. Expected declaration in '{expected_scope}' but found in '{actual_scope}'. "
        

        #Checks if the variable has the correct value
        if expected_value == actual_value :
          #Correct
          feedback += f"It has the value: {actual_value}"
        else:
          feedback += f"It has the wrong value. Expected '{expected_value}' but got '{actual_value}'"

        self.feedback.add(feedback)
      else:
        self.feedback.add(f"{variable} is not found")




  def check_functions(self):
    pass
  def set_variables(self, variables):
    self.variables = variables

  def set_functions(self, functions):
    self.functions = functions

  #This function takes the input code and returns the root node of the abstract syntax tree representing the structure of the code.
  def set_tree(self, code):
    try:
      self.tree = ast.parse(code)
    except SyntaxError as e:
      print(f"SyntaxError: {e}")


if __name__ == "__main__":
    
  #Testing
  code = '''    
    x = 10
    y = "Hello, World!"
    z = 3.14

    print(x + z)

    def greet(name):
        print(f"Hello, {name}!")

    def square(x):
        return x ** 2

    def define():
        greet("Mike")
        b = 2

    def set_params(a,b,c):
        return

    def not_set_params():
        return

  '''

  parser = Code_Parser(code)



