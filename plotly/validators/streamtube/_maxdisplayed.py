import _plotly_utils.basevalidators


class MaxdisplayedValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='maxdisplayed', parent_name='streamtube', **kwargs
    ):
        super(MaxdisplayedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=0,
            role='info',
            **kwargs
        )
