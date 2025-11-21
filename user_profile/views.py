from django.shortcuts import render

# Create your views here.
def test(request):
    context = {
        "title":"Hello world",
    }
    return render(request, "profile_templates/profile.html", context)