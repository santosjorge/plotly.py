import _plotly_utils.basevalidators


class BarnormValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(self, plotly_name='barnorm', parent_name='layout', **kwargs):
        super(BarnormValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            values=['', 'fraction', 'percent'],
            **kwargs
        )