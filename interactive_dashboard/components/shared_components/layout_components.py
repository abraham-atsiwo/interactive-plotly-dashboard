# from plotly.io import templates
from plotly.io import templates
import plotly.colors as pc
import plotly.express as px
from interactive_dashboard.utils import all_plot_args
from interactive_dashboard.components.shared_components import dropdown_with_label, \
                                        radioItems_with_label, slider_with_label

# args_defaults = all_plot_args().items()
args_defaults = all_plot_args()

def create_component():
    for args in args_defaults:
        if args in ['facet_col_spacing', 'facet_row_spacing', 'opacity', 'hole']:
            yield slider_with_label(label=args, min=0.00, max=1.00, step=0.2, value=1 if args=='opacity' else 0.0) 
        elif args in ['facet_col_wrap']:
            yield slider_with_label(label=args, min=0, max=5, step=1, value=0)
        elif args in ['height']:
            yield slider_with_label(label=args, min=500, max=1000, step=200, value=600)
        elif args in ['width']:
            yield slider_with_label(label=args, min=600, max=1100, step=200, value=900)
        # elif args in ['range_x', 'range_y']:
        #     yield rangeSlider_with_label(label=args, min=0, max=10, step=1, value=[2, 3])
        elif args in ['nbins']:
            yield slider_with_label(label=args, min=0, max=10, step=1, value=4)
        elif args in ['size_max']:
            yield slider_with_label(label=args, min=0, max=50, step=10, value=20)
        elif args in ['orientation']:
            yield dropdown_with_label(label=args, options=['v', 'h'])
        elif args in ['marginal_x', 'marginal_y', 'marginal']:
            yield dropdown_with_label(label=args, options=['rug', 'box', 'violin', 'histogram'])  
        elif args in ['trendline']: #check plotly.express.trendline_functions for trendline options args
            yield dropdown_with_label(label=args, options=['ols', 'lowess', 'expanding', 'ewm'])
        elif args in ['log_x', 'log_y', 'markers', 'text_auto', 'cummulative', 'log_z', 'box', 'notched', 'lines']:
            yield radioItems_with_label(label=args, options=[{'label': 'True', 'value': True}, {'label': 'False', 'value': False}], \
                        value=False, style={'color':'white'})
        elif args in ['render_mode']:
            yield dropdown_with_label(label='render_mode', options=['auto', 'svg', 'webgl'], value='auto')
        elif args in ['trendline_scope']:
            yield dropdown_with_label(label='trendline_scope', options=['trace', 'overall'], value='trace')
        elif args in ['line_shape']:
            yield dropdown_with_label(label='line_shape', options=['linear', 'spline'], value='linear')
        elif args in ['barmode']:
            yield dropdown_with_label(label=args, options=['relative', 'group', 'overlay'], value='relative')
        elif args in ['barnorm']:
            yield dropdown_with_label(label=args, options=['fraction', 'percent'])
        elif args in ['histnorm']:
            yield dropdown_with_label(label=args, options=['percent', 'probability', 'density'])
        elif args in ['histfunc']:
            yield dropdown_with_label(label=args, options=['count', 'sum', 'avg', 'min', 'max'])
        elif args in ['trendline_color_override']: 
            # colorscales = px.colors.qualitative.Alphabet
            colorscales = ['red', 'purple', 'olive', 'orange', 'green', 'navy', 'maroon', 'aqua']
            yield dropdown_with_label(label=args, options=colorscales)
        elif args in ['color_continuous_scale', 'color_discrete_sequence', 'color_discrete_map']: 
            colorscales = px.colors.named_colorscales()          
            yield dropdown_with_label(label=args, options=colorscales)
        elif args in ['color_continuous_midpoint']: 
            yield slider_with_label(label=args, min=0, max=1000, step=4, value=40)
        elif args in ['symbol_sequence']: #optins here of map
            options = ['circle-open', 'circle', 'circle-open-dot', 'square']
            yield dropdown_with_label(label=args, options=options)
        elif args in ['points']: #optins here of map
            options = ['outliers', 'suspectedoutliers', 'all', False]
            yield dropdown_with_label(label=args, options=options, value='outliers')
        elif args in ['violinmode', 'boxmode']: #optins here of map
            options = ['group', 'overlay']
            yield dropdown_with_label(label=args, options=options, value='overlay')
        elif args in ['ecdfmode']:
            yield dropdown_with_label(label=args, options=['standard', 'complementary', 'reversed'], value='standard')
        elif args in ['ecdfnorm']:
            yield dropdown_with_label(label=args, options=['probability', 'percent'])
        elif args in ['stripmode']:
            yield dropdown_with_label(label=args, options=['group', 'overlay'], value='group')
        elif args in ['template']: #optins here of map
            options = list(templates)
            yield dropdown_with_label(label=args, options=options)
        else:
            yield dropdown_with_label(label=args, options=[])




