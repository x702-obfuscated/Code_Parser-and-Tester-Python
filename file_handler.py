import os
import json

class File_Handler:

  def __init__(self):
    self.dir_path = os.getcwd()
    self.files = set()

  #adds the path of each file in the path to the self.files set
  def set_files(self,folder_path):
    try:
      files = os.listdir(folder_path)
      for file in files:
        self.files.add(os.path.join(folder_path,file))
    except Exception as e:
      print(f"Error: {e}")

  #reads a file and returns its contents as a string
  def readfile(file_path):
    content = ""
    with open(file_path,'r') as file:
      content = file.read()

    return content
  
  def read_json(file_path):
    json_dict = {}
    with open(file_path, "r") as file:
      json_dict = json.load(file)
    return json_dict
