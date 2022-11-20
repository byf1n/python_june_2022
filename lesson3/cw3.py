# class Bob:
#     __slots__ = ('name', 'surname', 'house')
#     coont = 0
#
#     def __init__(self, name, surname, house):
#         self.house = house
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'{self.name} - {self.surname}'
#
#     def __repr__(self):
#         return f'{self.name} - {self.surname}'
#
#
# bob = Bob('name', 'surname', 'asda')
# print(bob.house)

# class Bob:
#     __slots__ = ('name', 'surname')
#     __count = 0
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'{self.name} - {self.surname}'
#
#
# bob = Bob('name', 'surname', 'asda')
# print(Bob.__count)

# class Main:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def show_user(self):
#         print(self.name + ' - ' + self.surname)
#
#
# class Second(Main):
#     def __init__(self, name, surname, new):
#         self.new = new
#         super().__init__(name, surname)
#
#     def __str__(self):
#         return f'{self.name} - {self.surname} - {self.new}'
#
#
# user = Second('name', 'surname', 'new')
# print(user)
# user.show_user()

# class Calc:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = Calc('kirill')
# print(user.name)
# user.name = 'bobi'
# print(user.name)
# del user.name
# # print(user.name)
