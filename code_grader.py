import ast,os,time
#class for grading a single file
class Code_Parser:

  def __init__(self):
    self.variables = {}
    self.functions = set()
    self.tree = None
    self.feedback = []

  
 
  #checks variable declaration and value
  def parse_variable(self,in_function = False, outer_function = None):
    declared_variables = {}
    if(in_function):
      pass
    else:
      for node in ast.walk(self.tree):
        if isinstance(node, ast.Assign):
          for target in node.targets:
            if isinstance(target,ast.Name):
              variable_name = target.id
              
              if variable_name == target_variable:
                value = ast.literal_eval(node.value)
                declared_variables[variable_name] = value
              else:
                declared_variables[variable_name] = None
              

  def parse_function_definition(self,target_function,required_parameters = None):
    pass

  def parse_function_call(self,target_function, in_function = False, outer_function = None):
    pass

  
  



  def set_variables(self, variables):
    self.variables = variables

  def set_functions(self, functions):
    self.functions = functions

  def set_tree(self, code):
    self.tree = ast.parse(code)

  if __name__ == "__main__":
    pass



