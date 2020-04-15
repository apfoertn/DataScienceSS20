
class ListKeeper ():

    '''List wird als Dictionary deklariert'''
    list = {}

    def __init__(self):
      self.list["example"] = [1,2,3,4,5]

    def show (self):
      '''This function returns all list names'''
      return self.list.keys()

    def add (self, name, newlist):
      '''This function adds a new list to the dictionary'''
      self.list[name] = newlist

    def delete (self, name):
      '''This function deletes the list with the given name'''
      self.list.pop(name)

    def sort (self, name):
      '''This function returns the list with the given name in a sorted order'''
      self.list[name].sort()
      return self.list[name]

    def append (self, name, applist):
      '''This functions appends a list to the list with the given name'''
      self.list[name].append(applist)
      return self.list[name]

