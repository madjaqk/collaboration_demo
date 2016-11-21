from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		"message": "I hope don't get a merge conflict!",
		"name": "Jack",
	}
	return render(request, "collab/index.html", context)