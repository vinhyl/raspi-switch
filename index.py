# coding: utf8
import web
from web import form
# import switch


render = web.template.render('templates/')
urls = ("/", "index")
app = web.application(urls, globals())

myform = form.Form(
    form.Button(u"开锁"),
)


class index:
    def GET(self):
        form = myform()
        return render.index(form)

    def POST(self):
        # switch.open()
        return u"已开锁"


if __name__ == "__main__":
    app.run()
