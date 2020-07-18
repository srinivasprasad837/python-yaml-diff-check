import bios
import json
from deepdiff import DeepDiff
from pprint import pprint


def load_yml(input_path):
  """
    Load yml
    :param input_path: input file path
  """
  input = bios.read(input_path, file_type='yaml')
  # print('load_yml::input_path::'+ input_path + '::' + json.dumps(input))
  return input

def check_for_diff(input_file_path_1,input_file_path_2):
  """
    check for difference
    :param input_file_path_1: input file path
    :param input_file_path_2: input file path
  """
  input_dict_1 = load_yml(input_file_path_1)
  input_dict_2 = load_yml(input_file_path_2)
  ddiff = DeepDiff(input_dict_1, input_dict_2, view='tree',ignore_order=True)
  pprint(ddiff.to_json(), indent=2)


if __name__ == '__main__':
  cf_input_1_path = './cfInput1.yml'
  cf_input_2_path = './cfInput2.yml'
  # load_yml(cf_input_2_path)
  check_for_diff(cf_input_1_path, cf_input_2_path)
