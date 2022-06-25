from dash.html import Div, Label

def id_generator(label, id):
    if isinstance(label, str):
        labelid = label.strip().replace(" ", "-").lower()
    
    if id is None: 
        id = labelid 
    return id  

def label_widget(label, widget):
    return (
        Div(
            children=[
                Div(Label(label, id=label+'_label'), className='sidebar-item-label'), 
                Div(widget, className='sidebar-item-component')
            ], 
            className = 'sidebar-item-container',
            id = label+'_div'
        )

    )
     