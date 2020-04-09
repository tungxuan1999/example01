import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! My name Meo Meo cute !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
