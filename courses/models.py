from django.db import models
from .local_course_oper import get_curr_yrqtr, yearsub, base4sub

class Department(models.Model):
    # e.g. J SIS B
    # TODO: maybe there are longer ones???
    dept = models.CharField(max_length=7)
    dept_full = models.CharField(max_length=100)

    def __str__(self):
        return self.dept

class CourseInfo(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    slug_dept = models.SlugField()
    # e.g. Intro to Computer Programming II... or something
    crs_name = models.CharField(max_length=200)
    crs_num = models.IntegerField(default=100)
    # string of 0s and 1s to show availability of the course
    # 1 = available, 0 = not available
    # the first digit is the current quarter
    crs_avail = models.CharField(max_length=400)

    def __str__(self):
        return self.crs_name

    # this method exists, because it could be possible that a 
    # grade distribution visualization exists, but isn't marked as
    # being taught for some reason, hence cross-verification
    # however, a class could be taught, but not have a 
    # grade visualization, so to cross-verify in the other direction
    # doesn't really work
    def cross_verif(self):
        new_avail = list(self.crs_avail)
        curr_yq = get_curr_yrqtr()
        len_crs_av = len(self.crs_avail)
        for vis in self.gradevisual_set.all():
            targ_yq = vis.chosen_year_qtr
            excess = (curr_yq - targ_yq) - len_crs_av
            if targ_yq == 99999:
                i = 0
                while new_avail[i] == "1":
                    i += 1
                    if i >= curr_yq - targ_yq:
                        new_avail[i] = "P"
                        break
                new_avail[i] = "1"
                vis.chosen_year_qtr = curr_yq - i
                vis.save()
            elif len_crs_av < curr_yq - targ_yq:
                for i in range(0, excess - 1):
                    new_avail += "0"
                new_avail += "1"
            else:
                index = yearsub(curr_yq, targ_yq)
                new_avail[index] = "1"
        self.crs_avail = "".join(new_avail)
        self.save()


class GradeVisual(models.Model):
    course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    chosen_year_qtr = models.IntegerField(default=99999)
    # TODO: placeholder
    visualization = models.CharField(max_length=10)
