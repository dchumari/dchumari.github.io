from fasthtml.common import *


app, rt = fast_app(
	Live=False,
	debug=True,
	pico=False,
	hdrs=(Link(rel='stylesheet',href='/static/output.css')))

navbar = Div(cls='bg-blue-600 flex justify-between')(
	P(Img(src='/assets/adv.png', cls='h-[2px] w-[2px] flex'),'Derrick'),
	Ul(Li('Home'),Li("About"),Li("Projects"),Li('Blog'), cls='flex'),
	Img(src='/assets/10 D.png', cls='h-[2px] w-[2px] flex'))

@rt
def index():
	index = Div("Contents")
	return navbar
 
serve()