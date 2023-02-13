from django.shortcuts import render
'MAPS VIEWS'
# Create your views here.
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoiYWxpZHVnIiwiYSI6ImNsZGpoanZuazAwaHczcXFrMzBjZnZpbDcifQ.Pk65OCZgC5O4Zq4f7YI86g'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })


