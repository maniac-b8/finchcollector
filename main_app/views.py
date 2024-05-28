from django.shortcuts import render

# Create your views here.
finches = [
  {'name': 'House finch', 'conservation_status': 'LC (Least Concern)', 'location': 'North America', 'age': 4},
  {'name': 'Mangrove finch', 'conservation_status': 'CR (Critically Endangerd)', 'location': 'East Pacific Islands', 'age': 2},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })