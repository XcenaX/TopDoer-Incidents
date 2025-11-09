from django.shortcuts import redirect

def to_docs(request):
    return redirect("/docs/", permanent=False)