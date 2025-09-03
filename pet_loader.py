import tomllib
import os
import datetime

class Pet:
  def __init__(
        self,
        pet_type,
        name, 
        sex,
        breed,
        price,
        date_of_birth,
        description, 
        character,
        color=None,
        size=None,
        is_hidden=False
        ):
    self.pet_type = pet_type
    self.name = name
    self.sex = sex
    self.description = description
    self.character = character
    self.breed = breed
    self.date_of_birth = date_of_birth
    self.price = price
    self.color = color
    self.size = size
    self.is_hidden = is_hidden


def load_pets_from_directory(pets_dir):
  '''Gets directory with toml templates and returns list of pet objects'''
  pets_list=[]
  try:
    # For every file in pets_dir open it as toml
    for entry in os.scandir(pets_dir):
      if entry.is_file():
        # Opening a Toml file using tomlib
        with open(entry.path,"rb") as toml:
            toml_dict = tomllib.load(toml)
        # creating pet object
        temp_pet = Pet(
          toml_dict["general"]["type"],
          toml_dict["general"]["name"], 
          toml_dict["general"]["sex"],
          toml_dict["general"]["breed"],
          toml_dict["general"]["price"],
          toml_dict["general"]["date_of_birth"],
          toml_dict["general"]["description"],
          toml_dict["general"]["character"],
          toml_dict["appearance"]["color"],
          toml_dict["appearance"]["size"]
          )
        # Adding pet to the list
        pets_list.append(temp_pet)
  except PermissionError:
    print("Permission denied!")
  except FileNotFoundError:
    print("Directory not found!")
  return pets_list
