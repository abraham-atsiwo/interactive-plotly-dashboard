from dash import Input, Output
from interactive_dashboard import app
from inspect import signature
from .utils import all_plot_args, data_sources, plot_types, exceptions
import plotly.graph_objects as go
import plotly.colors as pc

args = all_plot_args()
color_continuous_scale = {'algae':pc.sequential.algae, 
                        'amp':pc.sequential.amp, 'Blackbody':pc.sequential.Blackbody, 
                        'matter': pc.sequential.matter, 'Peach': pc.sequential.Peach
                        }
def init_callback():
    @app.callback(
        [Output('plotarea', 'figure')],
        inputs = {
            'data': Input('data', 'value'),
            'sample_size': Input('data_size', 'value'),
            'plt_type': Input('plot-types', 'value'),
            'all_inputs': {id_key: Input(id_key, 'value') for id_key in args},       
        }
    )
    def update_graph(data, sample_size, plt_type, all_inputs): 
        figure_func = plot_types[plt_type]
        actual_params = set(signature(figure_func).parameters.keys()) - exceptions
        pars = {}
        for key in actual_params:
            pars[key] = all_inputs[key]
        df = data_sources[data]().iloc[:sample_size]
        pars['data_frame'] = df
        figure = figure_func(**pars)
        return [figure]


    @app.callback([Output(id+"_div", 'style') for id in args],
            Input('plot-types', 'value')
    )
    def hide_redundant_parameters(plt_type):
        figure_func = plot_types[plt_type]
        actual_params = list(signature(figure_func).parameters.keys())
        styles = [{'display':'flex'} if val in actual_params else {'display':'none'} for val in args]
        return styles


    @app.callback([Output('x', 'options'), Output('y', 'options'), \
        Output('x', 'value'), Output('y', 'value'), \
        Output('names', 'value')

        #  Output('x', 'clearable'), Output('y', 'clearable')
        ],
        [Input('data', 'value'), Input('plot-types', 'value')]
    )
    def update_xy(data, plt_type):
        n = data_sources[data]()
        df_col = data_sources[data]().columns
        if plt_type in ['scatter', 'pie', 'strip']:
            xcol =  df_col[0]
            ycol = df_col[1]
        elif plt_type in ['line', 'box', 'ecdf', 'violin', 'bar']:
            xcol = None 
            ycol = df_col[1]
        elif plt_type in ['histogram']:
            ycol = None 
            xcol = df_col[0]
        else:
            xcol = df_col[0]
            ycol = df_col[1]
        return df_col, df_col, xcol, ycol, df_col[0]


    col_options = ['names', 'values','color', 'symbol', 'size', 'hover_name', 'hover_data', 'custom_data', 
        'text', 'facet_row', 'facet_col', 'error_x','error_x_minus', 'error_y', 'error_y_minus', 
        'animation_frame', 'animation_group', 'line_group', 'pattern_shape', 'base']
    @app.callback([Output(val, 'options') for val in col_options],
        Input('data', 'value')
    )
    def update_columns(data):
        df_col = data_sources[data]().columns
        n = len(col_options)
        return [df_col for j in range(n)]


    @app.callback([Output('data_size', value) for value in ['min', 'max', 'step', 'value']],
        [Input('data', 'value')] 
    )
    def data_size(data):
        n = len(data_sources[data]())
        step = n//5
        return 10 if n >=20 else 0, n, step, step*3

    