from interactive_dashboard.layout import navbar, plot_types, mainbody
from dash.html import Div, Footer
from interactive_dashboard import app
from interactive_dashboard.callback import init_callback



app.layout = Div([navbar(),
    Div(
    children=[
            plot_types(),
            mainbody(), 
            Footer(className='footer'),
            Div(id='hidden'),

])
    ],
    className='container'
)


init_callback()

if __name__=='__main__':
    app.run_server(debug=True)

