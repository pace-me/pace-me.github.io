from django.shortcuts import render

def home(request):
#     if request.user.is_anonymous:
#         return redirect('/accounts/login/')
#   
          
    context = {
#         "show_count": show_count,
#         "show_count012": show_count012,
#         "show_count345": show_count345,
#         "show_top": show_top,
#         "show_bottom": show_bottom,    
    }    

    return render(request, 'index.html', {'context': context})