
class DemoMiddleware:

    #one time initialization
    def __init__(self, get_response):
        self.get_response = get_response
        self.context_response ={"msg" : "demo process_template_response"},
    
    #execute request logic before the view or other request called
    def __call__(self, request):
        
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'view name: {view_func.__name__}')
      

    def process_template_response(self, request, response):
        print(self.context_response)
        return response

