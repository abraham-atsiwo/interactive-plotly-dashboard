from dash.dcc import Dropdown
from .helpers import label_widget, id_generator
  
def dropdown_with_label(label, 
                    options, 
                    value=None, 
                    multi=False, 
                    style={}, 
                    className=None, 
                    id=None, 
                    kwargs={}
    ):

    id = id_generator(label, id)
    widget = Dropdown(options=options, 
                    value=value, 
                    multi=multi, 
                    style=style, 
                    className=className, 
                    id=id, **kwargs
    )

    return label_widget(label, widget)


