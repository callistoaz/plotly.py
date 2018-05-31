import _plotly_utils.basevalidators


class DtickValidator(_plotly_utils.basevalidators.AnyValidator):

    def __init__(
        self,
        plotly_name='dtick',
        parent_name='scatterternary.marker.colorbar',
        **kwargs
    ):
        super(DtickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            implied_edits={'tickmode': 'linear'},
            role='style',
            **kwargs
        )