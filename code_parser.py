import ast
from file_handler import File_Handler


class Code_Parser:

  def __init__(self,code,key):
    #abstract syntax tree
    self.set_tree(code)
    # print(ast.dump(self.tree))
    
    
    #Values to be checked
    self.variables = {} #name: (value, function name)
    self.functions = {} #name: (parameters, arguments)

    #Results
    self.declared_variables = {} #name : (value, function name)
    self.defined_functions = {} #name : parameters
    self.called_functions = {} #name : arguments
    self.feedback = list()
    self.score = 0

    self.parse()
    self.set_variables(key['variables'])
    self.set_functions(key['functions'])
    self.check_variables()
    self.check_functions()
    self.display_results()


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
    if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
    if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
      if len(node.args.args) > 0:
        self.defined_functions[node.name] = [param.arg for param in node.args.args]
      else:
        self.defined_functions[node.name] = None
    elif isinstance(node,ast.Call):
      if hasattr(node.func, "id"):
        if len(node.args) > 0:
          self.called_functions[node.func.id] = [arg for arg in node.args]
        else:
          self.called_functions[node.func.id] = None

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
          feedback += f"'{variable}'has the value: {actual_value}"
        else:
          feedback += f"'{variable}'has the wrong value. Expected '{expected_value}' but got '{actual_value}'"

        self.feedback.append(feedback)
      else:
        self.feedback.append(f"{variable} is not found")


  def check_functions(self):
    try:
      for function in self.functions:
        expected_parameters = function[0]
        expected_arguments = function[1]

        #check definition
        if function in self.defined_functions:
          actual_parameters = self.defined_functions[function]
          
          feedback = f"'{function}' is defined. "

          if expected_parameters == actual_parameters:
            feedback += f"It has the parameters {actual_parameters}. "
          else:
            feedback += f"But, has the wrong parameters. Expected '{expected_parameters}' but got '{actual_parameters}'."
          
          self.feedback.append(feedback)

        else:
          self.feedback.append(f"'{function}' is not defined.")

        if function in self.called_functions:
          actual_arguments = self.called_functions[function]
          
          feedback = f"'{function}' was called. "

          if expected_arguments == actual_arguments:
            feedback += f"It was called with the arguments '{actual_arguments}'. "
          else:
            feedback += f"But, with the wrong arguments. Expected '{expected_arguments}', but got '{actual_arguments}'."
          self.feedback.append(feedback)
        else:
          self.feedback.append(f"'{function}' was not called.")

        

    except SyntaxError as e:
      print(f"SyntaxError: {e}")
  
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


  def display_results(self):
    for elem in self.feedback:
      print(elem)
if __name__ == "__main__":

  # variables --> #name: (value, function name)
  # functions -->  #name: (parameters, arguments)
  key = {
    "variables":{
      "x": [10, None],
      "y": ["Hello, World!", None],
      "z": [3.14, None],

    },
    "functions":{
      "greet": ["name","Student"]
      
    }
  }


  code = File_Handler.readfile('.\main.py')

    


  Code_Parser(code,key)
  
  
 

'''

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


