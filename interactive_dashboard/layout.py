from dash.html import Div, Label
from dash.dcc import Dropdown, Graph, Store

from .components.shared_components.layout_components import create_component
from .components.shared_components import slider_with_label
from .utils import data_sources, plot_types
data_options = list(data_sources.keys())
plt_options = list(plot_types.keys())

sample_size = [slider_with_label('data_size', min=0, max=100, step=10, value=20)]
tmp_components = list(create_component())
sample_size.extend(tmp_components)
all_components = sample_size
n = len(all_components)//2
sidebar_comp, dataarea_comp = all_components[:16], all_components[16:]


sidebar_header = Div(Div('Sidebar'), className='mainbody-header')
def sidebar():
    sidebar = Div(
                children = sidebar_comp, 
                className='sidebar-container mainbody-item', 
                id='sidebar'
    )
    return sidebar


def dataarea():
    sidebar = Div(
                children = dataarea_comp, 
                className='dataarea-container mainbody-item', id='dataarea'
    )

    return sidebar


header = Div(Div('Plot Area'), className='mainbody-header')
def plotarea():
    plot_area = Div(
                children = [header, 
                            Div(Graph(id='plotarea'), className='graph'),
                            Div(id='table', style={'marginTop':'10px'})
                ], 
                className='plotarea-container mainbody-item'
    )

    return plot_area


def mainbody():
    main_body = Div(children=[sidebar(), plotarea(), dataarea()], 
                className='mainbody-container'
    )

    return main_body

def plot_types():
    plot_types = Div(Div(
        children=[Label('Plot types', style={'color':'white', 'fontWeight':'bold', 'marginBottom':'25px'}),
                Dropdown(options=plt_options, value='scatter', style={'background':'black', 'color':'black'}, id='plot-types'), 
                Label('Data', style={'color':'white', 'fontWeight':'bold', 'marginBottom':'25px'}),
                Dropdown(options=data_options, value='iris', style={'background':'black', 'color':'black'}, id='data'),
                Store(id='store'),
                Div(id='hidden-field')
                ],
        className='plot-types', style={'marginTop':'100px'}
    ),  className='plot-types-container')

    return plot_types



def navbar():
    navbar = Div(
        children = [Div("Interactive Dashboard (ID) Explorer", 
                        className='navbar-interactive-dashboard navbar-item'),  
                    Div("Plotly | Dash", className='navbar-item')
        ],
        className="navbar-container"
    )
    return navbar