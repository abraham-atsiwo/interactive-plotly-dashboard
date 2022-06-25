from dash.dcc import RangeSlider
from .helpers import label_widget, id_generator
  
def rangeSlider_with_label(label, 
                    min, 
                    max,
                    step,
                    value=None, 
                    className=None, 
                    id=None, 
                    kwargs={}
    ):

    id = id_generator(label, id)
    widget =RangeSlider( min=min, 
                    max=max,
                    step=step,
                    value=value, 
                    className=className, 
                    id=id, **kwargs
    )

    return label_widget(label, widget)
