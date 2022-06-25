from dash.dcc import RadioItems
from .helpers import label_widget, id_generator
  
def radioItems_with_label(label, 
                    options, 
                    value=None, 
                    style={}, 
                    className=None, 
                    id=None, 
                    kwargs={}
    ):

    id = id_generator(label, id)
    widget = RadioItems(options=options, 
                    value=value, 
                    style=style, 
                    className=className, 
                    id=id, **kwargs
    )

    return label_widget(label, widget)

