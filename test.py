from courses.models import Department, CourseInfo, GradeVisual

# this script is only runnable in shell, as of now
# import subprocess

# has one class, only one with multi-visuals so far
d1 = Department(dept="TST", dept_full="Test")
d1.save()

# has no classes
d2 = Department(dept="NUL")
d2.save()

# has more than one class
d3 = Department(dept="TRS", dept_full="Trash Studies")
d3.save()

d4 = Department(dept="AB BR EV", 
    dept_full="Uhm, we, uhm, just put random letters together just to look cool, lmao")
d4.save()

Department.objects.all()

c1 = d1.courseinfo_set.create(slug_dept=d1, crs_name="Intro to Test",
     crs_num=101, crs_avail="0010")
c3_1 = d3.courseinfo_set.create(slug_dept=d3, crs_name="Trash Can? Or Trash Can't",
    crs_num=206, crs_avail="1111111111111111")
c3_2 = d3.courseinfo_set.create(slug_dept=d3, crs_name="Trash Seminar",
    crs_num=499, crs_avail="00010001")
c4 = d4.courseinfo_set.create(slug_dept=d4, crs_name="Politics Behind Beaning People",
    crs_num=123, crs_avail="00000000")

c1.gradevisual_set.create(visualization="E")
c1.gradevisual_set.create(visualization="L", chosen_year_qtr=20182)

# subprocess.Popen("py manage.py runserver")
