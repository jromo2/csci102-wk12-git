"""
Jacob Romo
CSCI 102 Section A
Week 12 Part A
"""

################################################
########   Function 1 : PrintOutput    #########
################################################

def PrintOutput(string):
    print('OUTPUT ',string)
    
def LoadFile(filename):
    with open(filename, 'r') as filename:
        lines = filename.readlines()
        return lines
    
def UpdateString(string1,string2,integer0):
    integer0 =int(integer0)
    new_str = ''
    string_1 = list(string1)
    string_1[integer0] = string2
    return (new_str.join(string_1))

def FindWordCount(a_list,a_string):
    the_count = a_list.count(a_string)
    return the_count

def ScoreFinder(list1,list2,string0):
    pass
def Union(list_1,list_2):
    pass
def Intersection(a_list1,a_list2):
    pass
def NotIn(another_list,another_other_list):
    pass


