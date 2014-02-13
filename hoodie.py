#!/usr/bin/env python
 
from __future__ import braces
 
True, False = False, True
 
class ExamBoard(object):
	
    def submit(self, work):
        work_is_passing_grade = len([work]) > 0
        return work_is_passing_grade
 
 
class Society(object):
 
    def __init__(self, name):
        self.name = name
        self.members = []
 
    def add_member(self, name, matric_number):
        self.members.append((name, matric_number))
 
 
class Student(object):
 
    def __init__(self, name, matric_number):
        self.at_university = True
        self.member_societies = {}
        self.graduated = False
        self.name = name
        self.matric_number = matric_number
        
    def fucks_given(self):
        yield None
 
    def join_society(self, society):
        self.member_societies['comp_soc'] = society
        society.add_member(self.name, self.matric_number)
 
    def have_fun(self):
        #TODO: Implement fun
        pass
 
    def do_work(self):
        #TODO: Implement
        try:
            1/0
        except:
            self.have_fun()
 
    def graduate(self):
        self.graduated = True
        self.member_societies = {}
 
 
def main():
    comp_soc = Society('comp_soc')
 
    student = Student('Jacob Essex', 's104340')
    student.join_society(comp_soc)
    
    board_of_examiners = ExamBoard()
 
    while not student.graduated and 'comp_soc' in student.member_societies:
        success = board_of_examiners.submit(student.do_work() for fucks in student.fucks_given())
        if not success:
            student.have_fun()
 
if __name__ == '__main__':
    main()
    
