"""
https://github.com/jromo2/csci102-12-git
Jacob Romo
CSCI 102 Section A
Week 12 Part A
"""

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
    x = False
    for player in list1:
        if player.casefold() == string0.casefold():
            i = list1.index(player)
            score = list2[i]
            x = True
            return ('OUTPUT %s got a score of %d' % (player, score))
    if x == False:
        return ('OUTPUT player not found')
        
def Union(list_1,list_2):
    list_3 = []
    for item in list_1:
        for obj in list_2:
            if item == obj:
                list_2.remove(obj)
    list_3 = list_1 + list_2
    return list_3
def Intersection(a_list1,a_list2):
    list_3 = []
    for item in a_list1:
        for obj in a_list2:
            if item == obj:
                list_3.append(item)
    return list_3
def NotIn(another_list,another_other_list):
    list_3 = []
    for item in another_list:
        if item not in another_other_list:
            list_3.append(item)
    return list_3
    
 

