from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		"message": "I like collaborating, with collaborators!",
	}
	return render(request, "collab/index.html", context)
