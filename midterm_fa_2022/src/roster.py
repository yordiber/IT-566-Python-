"""Implements Team Roster Operations"""

import json


class Roster(object):
    """Implements Team Roster Operations"""
    def __init__(self):
        self.roster ={}

    def load_roster(self):
        filename = input("enter filepath and name:")
        with open(filename, 'r', encoding ='UTf-8') as f:
            self.roster = json.loads(f.read())
            print(self.roster)

    def print_roster(self):
        print(json.dumps(self.roster))

    def add_members(self):
      keep_going = 'y'
      while keep_going == 'y':
        member_name = input("Enter member name:")
        member_age =int(input("Enter Age:"))
        self.roster['members'].append({'name':member_name,'age':member_age})
        keep_going = input("Add another? (y/n)")
    
    def save_roster(self):
        _file_name = input("Enter path and filename:")
        with open(_file_name, 'w', encoding='UTF-8') as f: 
            f.write(json.dumps(self.roster))

