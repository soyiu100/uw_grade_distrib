from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Department, CourseInfo, GradeVisual

from django.urls import reverse
from django.views import generic
from .local_course_oper import get_curr_yrqtr, get_years, base4sub

class IndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'dept_list'
    
    def get_queryset(self):
        # returns a set of names instead of objects
        return Department.objects.values_list('dept', flat=True).order_by('dept').distinct()


# class DeptView(generic.DetailView):
#    model = Department
#    template_name = 'courses/detail.html'

# class CourseVisView(generic.DetailView):
#    model = CourseInfo
#    template_name = 'courses/vis.html'


def dept(request, slug_dept):
    deptmt = get_object_or_404(Department, dept=slug_dept)
    curr_yrqtr = get_curr_yrqtr()
    return render(request, 'courses/dept.html', {'deptmt': deptmt,
    'curr_yrqtr': curr_yrqtr})

def vis_choose(request, slug_dept, crs_num):
    curr_yrqtr = get_curr_yrqtr()
    poss_course = CourseInfo.objects.filter(crs_num=crs_num, slug_dept=slug_dept)[0]
    course = get_object_or_404(CourseInfo, crs_name=poss_course.crs_name)
    qtr_num = len(course.crs_avail)
    course.cross_verif()
    years = get_years(course, qtr_num, curr_yrqtr)
    return render(request, 'courses/vis_choose.html', {'course': course,
        'slug_dept': slug_dept,
        'curr_yrqtr': curr_yrqtr,
        'years': years, })

def selection(request, slug_dept, crs_num):
    curr_yrqtr = get_curr_yrqtr()
    poss_course = CourseInfo.objects.filter(crs_num=crs_num, slug_dept=slug_dept)[0]
    course = get_object_or_404(CourseInfo, crs_name=poss_course.crs_name)
    qtr_num = len(course.crs_avail)
    years = get_years(course, qtr_num, curr_yrqtr)
    try:
        selected = course.gradevisual_set.all().get(chosen_year_qtr=request.POST['year'])
    except (KeyError, GradeVisual.DoesNotExist):
        print("ma ass")
        return render(request, 'courses/vis_choose.html', {'course': course, 'slug_dept': slug_dept,
            'curr_yrqtr': curr_yrqtr, 
            'qtr_num': qtr_num, 
            'years': years, 
            'message': "Choose something",})
    else:
        return HttpResponseRedirect(reverse('courses:course_visualization', args=(slug_dept, crs_num, selected.chosen_year_qtr)))

#TODO: placeholder
def course_vis(request, slug_dept, crs_num, yrqtr):
    return render(request, 'courses/course_vis.html', {})

# vis_cho
#    curr_yrqtr = get_curr_yrqtr()
#    poss_course = CourseInfo.objects.filter(crs_num=crs_num, slug_dept=slug_dept)[0]
#    course = get_object_or_404(CourseInfo, crs_name=poss_course.crs_name)
#    qtr_num = len(course.crs_avail)
#    return render(request, 'courses/vis_choose.html', {'course': course, 'slug_dept': slug_dept,
#    'curr_yrqtr': curr_yrqtr, 'qtr_num': qtr_num})

