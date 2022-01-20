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

	def __init__(self, name, sname, marks, econ_accolade):
		super().__init__(name, sname, marks)
		self.econ_accolade = econ_accolade

class stud_Leader(Students):
	def __init__(self, name, sname, marks, stud_jurisdiction = None):
		super().__init__(name, sname, marks)
		if stud_jurisdiction == None:
			self.stud_jurisdiction = []
		else:
			self.stud_jurisdiction = stud_jurisdiction



#==========returns a method resolution order===================

# print(help(EconStudents)) 

# =============================================================
 
econ_1 = EconStudents('Joy', 'Mary',600, 'Bronzeeconomist')
print(econ_1.stud_marks())
print(econ_1.econ_accolade)