from cmath import exp
from plotly.express import scatter, line, ecdf, violin, box, histogram, bar, pie, strip, scatter_3d, line_3d, treemap, density_contour
from plotly.data import carshare, iris, election, experiment, gapminder, medals_long, tips, wind
from inspect import signature
import itertools

plot_types = {'scatter': scatter, 'line': line, 'box': box, 'ecdf': ecdf, 'violin': violin, 'histogram': histogram, 'bar':bar,\
            'pie': pie, 'strip': strip, 
            #'scatter_3d': scatter_3d, 'line_3d': line_3d, 'treemap': treemap, 'density_contour': density_contour
    }
data_sources = {'iris': iris, 'carshare':carshare, 'election':election, 'experiment':experiment, 
                'gapminder': gapminder, 'tips': tips
}



def model_parameters(plot_types):
    for key, value in plot_types.items():
        yield signature(value).parameters.keys()

exceptions=set(['category_orders', 'labels', 'range_color', 'symbol_sequence', 'symbol_map', 'trendline_options', 'line_dash_sequence',
        'range_x', 'range_y', 'data_frame', 'color_discrete_sequence', 'color_discrete_map', 'title', 'line_dash', 'line_dash_map', 
        'color_continuous_scale', 'pattern_shape_sequence', "pattern_shape_map",
        'color_continuous_midpoint', "trendline_color_override"
        ])
def all_plot_args(plot_types:dict=plot_types, exceptions=exceptions):
    result = model_parameters(plot_types) 
    flatten_list = list(itertools.chain(*result)) 
    res = sorted(set(flatten_list)-exceptions, key=flatten_list.index)
    return res




