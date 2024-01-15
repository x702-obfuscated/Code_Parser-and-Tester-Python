import ast, os
'''
for checking if statements, while loops, and for loops
combine parsing with sticking these inside functions to test them
(it may be beneficial for students to see my pre made functions)
build into a Code_Grader class for reuseability and ease of access. 

'''




def readfile(filename):
  file_path = os.path.join(os.getcwd(),filename)

  source_code = ""
  with open(file_path,'r') as file:
    source_code = file.read()

  return source_code


#checks is a variable is declared and its value in the main function
def check_variable_declaration(code, target_variable):
  try:
    #This function takes the input code and returns the root node of the abstract syntax tree representing the structure of the code.
    tree = ast.parse(code)

    #initialized and empty set
    declared_variables = set()

    #track variable values
    variable_values = {}

    for node in ast.walk(tree):

      #check if variable is declared and initialized
      if isinstance(node, ast.Assign):# Checks to see if the node is an Assignment. Use ast.Call for checking if a function was called
        for target in node.targets:
          if isinstance(target, ast.Name): #represents an occurrence of a name, which could be a variable name, function name, or some other identifier in the Python code.
            variable_name = target.id
            declared_variables.add(variable_name)

          #set the variable value in the dictionary 
          if variable_name == target_variable:
            value = ast.literal_eval(node.value)
            variable_values[variable_name] = value
  
    #check if the target variables is declared and provide feedback
    if(target_variable in declared_variables):
      print(f"Variable '{target_variable}' is declared and initialized")

    else:
      print(f"Variable '{target_variable}' is not declared and initialized")


    #check if the target has a value
    if target_variable in variable_values:
      print(f"Value of '{target_variable}': {variable_values[target_variable]}")
    else:
      print(f"Variable '{target_variable}': not found or not assigned a value.")



  except SyntaxError as e:
    print(f"SyntaxError: {e}")
#checks if a function is defined and called
def check_function_definition(code, target_function):
  try:
  #This function takes the input code and returns the root node of the abstract syntax tree representing the structure of the code.
    tree = ast.parse(code)


    #set of defined functions
    defined_functions = set()

    #set of called functions
    called_functions = set()


    for node in ast.walk(tree):
      #check if function is defined
      if isinstance(node,ast.FunctionDef):
        #check if function matches target function
        if node.name == target_function:
          defined_functions.add(target_function)
      
      if isinstance(node,ast.Call):
        if hasattr(node.func,"id") and node.func.id == target_function:
          called_functions.add(target_function)


    #check if the target has a value
    if target_function in defined_functions:
      print(f"Function '{target_function}' is defined")
    else:
      print(f"Function '{target_function}' is not defined")

    if target_function in called_functions:
      print(f"Function '{target_function}' is called")
    else:
      print(f"Function '{target_function}' is not called")

      
  except SyntaxError as e:
    print(f"SyntaxError: {e}")
#checks variables declared and initialized inside of a given function
def check_inside_function(code, target_function,target_variable):
  try:
  #This function takes the input code and returns the root node of the abstract syntax tree representing the structure of the code.
    tree = ast.parse(code)

    declared_variables = set()

    variable_values = {}



    for node in ast.walk(tree):
      #check if function is defined
      if isinstance(node,ast.FunctionDef) and node.name == target_function:
        for function_node in ast.walk(node):
          if isinstance(function_node, ast.Assign):
            for target in function_node.targets:
              if isinstance(target, ast.Name):
                variable_name = target.id
                declared_variables.add(variable_name)

                #set the variable value in the dictionary 
                if variable_name == target_variable:
                  value = ast.literal_eval(function_node.value)
                  variable_values[variable_name] = value


    #check if the target variables is declared and provide feedback
    if(target_variable in declared_variables):
      print(f"Variable '{target_variable}' is declared and initialized in '{target_function}'")

    else:
      print(f"Variable '{target_variable}' is not declared and initialized in '{target_function}'")


    #check if the target has a value
    if target_variable in variable_values:
      print(f"Value of '{target_variable}': {variable_values[target_variable]} in '{target_function}'")
    else:
      print(f"Variable '{target_variable}': not found or not assigned a value in '{target_function}'")

      
  except SyntaxError as e:
    print(f"SyntaxError: {e}")

def check_parameters(code, target_function, required_parameters):
  try:
    tree = ast.parse(code)

    defined_functions_with_parameters = set()

    for node in ast.walk(tree):
      if isinstance(node, ast.FunctionDef) and node.name == target_function:
        parameters = [param.arg for param in node.args.args]

        if set(parameters) == set(required_parameters):
          defined_functions_with_parameters.add(target_function)

        # Check if the target_function is defined with the required parameters
    if target_function in defined_functions_with_parameters:
        print(f"Function '{target_function}' is defined with parameters: {required_parameters}.")
    else:
        print(f"Function '{target_function}' is not defined with the required parameters: {required_parameters}.")
            
  except SyntaxError as e:
      print(f"SyntaxError: {e}")


if __name__ == "__main__":

  source_code = readfile("test_code.py")
  check_variable_declaration(source_code, "x")
  check_variable_declaration(source_code, "a")

  check_function_definition(source_code,"greet")
  check_function_definition(source_code,"square")
  check_function_definition(source_code,"add")
  check_function_definition(source_code,"sub")

  check_inside_function(source_code,'define','b')
  
  check_parameters(source_code,"set_params",["a","b","c"])
  check_parameters(source_code,"not_set_params",["a","b","c"])
  