# method - a function associated with a class
#attributes - 
# class - blueprint for creating instances
# instances - each student is an instance of this class
# intance variables- contain data that is unique to each variable.
#  class variables - variables that are shared by all instances of a class


class Students():
	#==============================================class variables============================================
	standard_mark = 0.60 
	stud_reg_no = '00000'

	def __init__(self, name, sname, marks): #constructor/initializer

		# ===================================instance variables==============================================
		self.name = name
		self.sname = sname
		self.email = name + '.' + sname + '@school.com' 
		self.marks = marks
		Students.stud_reg_no += '1' 


	def fullname(self):
		return '{} {}'.format(self.name,self.sname)

	def stud_marks(self):
		return '{}'.format(self.marks * self.standard_mark)

	# ================================dunder methods==============================================

	# dunder repr for debugging

	def __repr__(self):
		return 'Student details: "{}", "{}", "{}", "{}"'.format(self.name, self.sname, self.marks, self.school)



	# end user 

	def __str__(self):
		return '"{}" -> "{}"'.format(self.fullname(), self.marks)

	# other inbuilt ones

	def __add__(self, other):
		return self.marks + other.marks



	def __len__(self):
		return len(self.fullname())



	# =============================class methods and static methods==================================================

	@classmethod
	def set_standard_mark(cls, mark):
		cls.standard_mark = mark


	# ================================class methods as alternative constructors===============================

	@classmethod
	def from_data_input(cls, stud_rec):
		fname, s_name, smarks = stud_rec.split('-')
		return cls(fname, s_name, smarks)


	# ===================================static methods==========================================

	@staticmethod
	def school_day(date):
		if date.weekday() == 5 or date.weekday() == 6:  # the weekday() function is a datetime method
			return 'Weekend'
		return 'School day'


# ====================================================================================

stud_1 = Students('Jared', 'Kamran', 390)
print(stud_1.stud_marks())

print(Students.fullname(stud_1))

print(stud_1.stud_reg_no)


# =====================================================applying class methods====================================================


Students.set_standard_mark(0.80)
print(stud_1.stud_marks())


# ================================applying class methods as alternative constructors==============================================

stud_rec_1 = 'John-Sanaipei-400'
stud_rec_2 = 'Jane-Sonia-420'
stud_rec_3 = 'Loise-Lila-401'

# fname, form_level, s_name, smarks = stud_rec_1.split('-')
# stud_01 =  Students(fname, form_level, s_name, smarks)

stud_01  = Students.from_data_input(stud_rec_1)
print(stud_01.fullname())

# =============================applying static methods=========================================

import datetime

today_date = datetime.date(2022, 1, 23)

date = Students.school_day(today_date)
print(date)


# =======================================inheritance and subclasses=================================================

class EconStudents(Students):
	standard_mark = 0.85

	def __init__(self, name, sname, marks, school):
		super().__init__(name, sname, marks)
		self.school = school

class stud_Leader(Students):
	def __init__(self, name, sname, marks, stud_jurisdiction = None):
		super().__init__(name, sname, marks)
		if stud_jurisdiction == None:
			self.stud_jurisdiction = []
		else:
			self.stud_jurisdiction = stud_jurisdiction
	def add_jurisdiction(self, schl):
		if schl not in self.stud_jurisdiction:
			self.stud_jurisdiction.append(schl)
		
	def remove_jurisdiction(self,schl):
		if schl in self. stud_jurisdiction:			
			self.stud_jurisdiction.remove(schl)

	def print_jurisdictions(self):
		for schl in self.stud_jurisdiction:
			print('-->', schl.school)




#==========returns a method resolution order===================

# print(help(EconStudents)) 

# =============================================================
 
econ_1 = EconStudents('Joy', 'Mary',600, 'Economics')
maths_1 = EconStudents('Karimi', 'John', 800, 'Pure Sciences')
print(econ_1.stud_marks())
print(econ_1.school)


lead_1 = stud_Leader('Janet', 'Monae', 700, [econ_1])
lead_1.add_jurisdiction(maths_1)

lead_1.print_jurisdictions()


# ===========================isinstance and issubclass=========================

print(isinstance(lead_1, stud_Leader))
print(issubclass(stud_Leader, Students))

# ==============================special methods=================================

print(econ_1)


print(econ_1 + lead_1) # adding total marks for two students

print(len(econ_1))  #length of each student's fullname


# ===============================property decorators: getter, setter, deleter=========================


class Employees():
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	@property
	def email(self):
		return "{}.{}@company.com".format(self.first, self.last)

	@property
	def fullname(self):
		return self.first + " " + self.last

	#setters

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	def __str__(self):
		return '{} - {} - {}'.format(self.first, self.last, self.email)

	#deleters


	@fullname.deleter
	def fullname(self):
		self.first = None
		self.last = None
		print('Name has been deleted!')


#================================================================================================================

emp_1 = Employees('Sara', 'Kombucha', 70000)
emp_2 = Employees('James', 'Kangari', 50000)

emp_2.fullname = 'Janet Mutua'

print(emp_1.fullname)
print(emp_1.email)
print(emp_2)


del emp_2.fullname

emp_2.fullname = 'James Kangari'

print(emp_2)


