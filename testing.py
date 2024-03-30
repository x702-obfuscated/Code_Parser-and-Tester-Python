'''
Module: Represents the entire Python module.
FunctionDef: Represents a function definition.
ClassDef: Represents a class definition.
Assign: Represents an assignment statement.
Name: Represents a variable or identifier.
Call: Represents a function or method call.
BinOp: Represents a binary operation (e.g., addition, subtraction).
Num: Represents a numeric literal.
Str: Represents a string literal.
List, Tuple, Dict: Represent list, tuple, and dictionary literals, respectively.
If, While, For: Represent control flow statements such as if statements, while loops, and for loops.
Return: Represents a return statement.
Attribute: Represents an attribute access (e.g., object.attribute).
Expr: Represents an expression statement.
'''


import ast
import os
from file_handler import File_Handler


code = File_Handler.readfile(".\\main.py")

tree = ast.parse(code)
# print(ast.dump(tree))




# For Unix/Linux
if os.name == 'posix':
  os.system('clear')
# For Windows
elif os.name == 'nt':
  os.system('cls')

expected_functions = {
  "greet" : "",
  "square": "",
  "define": "",
  "set_params": "",
  "not_set_params":""
}

def walk(tree):
  for node in ast.walk(tree):
    check_Assign(node)
    check_FunctionDef(node)
    check_FunctionCall(node)

def check_Assign(node):
  if(isinstance(node,ast.Assign)):
    for name in node.targets:
      print(f"Variable Declared: {name.id}")

def check_FunctionDef(node):
    if(isinstance(node,ast.FunctionDef)):
      string = f"'{node.name}' function defined"
      if(hasattr(node,"args")):
        parameters = [param.arg for param in node.args.args]
        string += f" with the parameter(s) {tuple(parameters)}"
      print(f"{string}.")

def check_FunctionCall(node):
    if(isinstance(node,ast.Call)):
      string = ""
      if(hasattr(node.func,"id")):
        string += f"'{node.func.id}' function called"
      # if(hasattr(node,"args")):
      #   arguments = [ast.dump(arg) for arg in node.args]
  
        # string += f" with the argument(s) {tuple(arguments)}"
        print(f"{string}.")


walk(tree)







    # def evaluate_expression(node):
    #     left = evaluate_operand(node.left)
    #     right = evaluate_operand(node.right)

    #     if isinstance(node.op, ast.Add):
    #         return left + right
    #     elif isinstance(node.op, ast.Sub):
    #         return left - right
    #     elif isinstance(node.op, ast.Mult):
    #         return left * right
    #     elif isinstance(node.op, ast.Div):
    #         return left / right
    #     elif isinstance(node.op, ast.FloorDiv):
    #         return left // right
    #     elif isinstance(node.op, ast.Mod):
    #         return left % right
    #     elif isinstance(node.op, ast.Pow):
    #         return left ** right
    #     else:
    #         raise ValueError("Unsupported operator")


    # def evaluate_operand(operand):
    #     if isinstance(operand, ast.Constant):
    #         return operand.value
    #     elif isinstance(operand, ast.Name):
    #         # Lookup the value of the variable in the current environment
    #         return eval(operand.id)
    #     else:
    #         raise ValueError("Unsupported operand type")













'''
Module(
  body=[
    Assign(
      targets=[Name(id='x', ctx=Store())], 
      value=Constant(value=10)
    ), 
    
    Assign(
      targets=[Name(id='y', ctx=Store())], 
      value=Constant(value='Hello, World!')
    ),
    
    Assign(
      targets=[Name(id='z', ctx=Store())], 
      value=Constant(value=3.14)
    ), 
    
    Expr(
      value=Call(func=Name(id='print', ctx=Load()), 
      args=[BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Name(id='z', ctx=Load()))], 
      keywords=[])
    ), 
    
    FunctionDef(
      name='greet', args=arguments(posonlyargs=[], args=[arg(arg='name')], kwonlyargs=[], kw_defaults=[], defaults=[]), 
      body=[
        Expr(
          value=Call(func=Name(id='print', ctx=Load()), 
          args=[JoinedStr(values=[Constant(value='Hello, '
        ), 
        FormattedValue(
          value=Name(id='name', ctx=Load()), conversion=-1), Constant(value='!')])], keywords=[]))], 
          decorator_list=[]
    ), 
    
    FunctionDef(
      name='square', args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), 
      body=[Return(value=BinOp(left=Name(id='x', ctx=Load()), op=Pow(), right=Constant(value=2)))], 
      decorator_list=[]
    ), 

    FunctionDef(
      name='define', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), 
      body=[Expr(value=Call(func=Name(id='greet', ctx=Load()), args=[Constant(value='Mike')], keywords=[])), 
        Assign(targets=[Name(id='b', ctx=Store())], value=Constant(value=2))], 
      decorator_list=[]
    ), 
    
    FunctionDef(
      name='set_params', args=arguments(posonlyargs=[], args=[arg(arg='a'), arg(arg='b'), arg(arg='c')], kwonlyargs=[], kw_defaults=[], defaults=[]), 
      body=[Return()], 
      decorator_list=[]
    ), 

    FunctionDef(name='not_set_params', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return()], decorator_list=[])], type_ignores=[])

'''
