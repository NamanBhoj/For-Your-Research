from django.http import HttpResponse, JsonResponse

import subprocess
import os

def showPaper(request):
    return 

def run_spider(request):
    if request.method == 'GET':
        # Get the query parameter from the request
        query = request.GET.get('query', '')
        
        os.chdir("../scrapy_project")
        print(os.getcwd())
        
        subprocess.Popen(["scrapy", "crawl", "example", "-a", f"query={query}"])  

        return HttpResponse(f"Spider started for query: {query}")
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
