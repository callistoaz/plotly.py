from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Annotation(BaseLayoutHierarchyType):

    # align
    # -----
    @property
    def align(self):
        """
        Sets the horizontal alignment of the `text` within the box. Has
        an effect only if `text` spans more two or more lines (i.e.
        `text` contains one or more <br> HTML tags) or if an explicit
        width is set to override the text width.
    
        The 'align' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['align']

    @align.setter
    def align(self, val):
        self['align'] = val

    # arrowcolor
    # ----------
    @property
    def arrowcolor(self):
        """
        Sets the color of the annotation arrow.
    
        The 'arrowcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['arrowcolor']

    @arrowcolor.setter
    def arrowcolor(self, val):
        self['arrowcolor'] = val

    # arrowhead
    # ---------
    @property
    def arrowhead(self):
        """
        Sets the end annotation arrow head style.
    
        The 'arrowhead' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 8]

        Returns
        -------
        int
        """
        return self['arrowhead']

    @arrowhead.setter
    def arrowhead(self, val):
        self['arrowhead'] = val

    # arrowside
    # ---------
    @property
    def arrowside(self):
        """
        Sets the annotation arrow head position.
    
        The 'arrowside' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['end', 'start'] joined with '+' characters
            (e.g. 'end+start')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        return self['arrowside']

    @arrowside.setter
    def arrowside(self, val):
        self['arrowside'] = val

    # arrowsize
    # ---------
    @property
    def arrowsize(self):
        """
        Sets the size of the end annotation arrow head, relative to
        `arrowwidth`. A value of 1 (default) gives a head about 3x as
        wide as the line.
    
        The 'arrowsize' property is a number and may be specified as:
          - An int or float in the interval [0.3, inf]

        Returns
        -------
        int|float
        """
        return self['arrowsize']

    @arrowsize.setter
    def arrowsize(self, val):
        self['arrowsize'] = val

    # arrowwidth
    # ----------
    @property
    def arrowwidth(self):
        """
        Sets the width (in px) of annotation arrow line.
    
        The 'arrowwidth' property is a number and may be specified as:
          - An int or float in the interval [0.1, inf]

        Returns
        -------
        int|float
        """
        return self['arrowwidth']

    @arrowwidth.setter
    def arrowwidth(self, val):
        self['arrowwidth'] = val

    # ax
    # --
    @property
    def ax(self):
        """
        Sets the x component of the arrow tail about the arrow head. If
        `axref` is `pixel`, a positive (negative)  component
        corresponds to an arrow pointing from right to left (left to
        right). If `axref` is an axis, this is an absolute value on
        that axis, like `x`, NOT a relative value.
    
        The 'ax' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['ax']

    @ax.setter
    def ax(self, val):
        self['ax'] = val

    # axref
    # -----
    @property
    def axref(self):
        """
        Indicates in what terms the tail of the annotation (ax,ay)  is
        specified. If `pixel`, `ax` is a relative offset in pixels
        from `x`. If set to an x axis id (e.g. *x* or *x2*), `ax` is
        specified in the same terms as that axis. This is useful  for
        trendline annotations which should continue to indicate  the
        correct trend when zoomed.
    
        The 'axref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['pixel']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self['axref']

    @axref.setter
    def axref(self, val):
        self['axref'] = val

    # ay
    # --
    @property
    def ay(self):
        """
        Sets the y component of the arrow tail about the arrow head. If
        `ayref` is `pixel`, a positive (negative)  component
        corresponds to an arrow pointing from bottom to top (top to
        bottom). If `ayref` is an axis, this is an absolute value on
        that axis, like `y`, NOT a relative value.
    
        The 'ay' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['ay']

    @ay.setter
    def ay(self, val):
        self['ay'] = val

    # ayref
    # -----
    @property
    def ayref(self):
        """
        Indicates in what terms the tail of the annotation (ax,ay)  is
        specified. If `pixel`, `ay` is a relative offset in pixels
        from `y`. If set to a y axis id (e.g. *y* or *y2*), `ay` is
        specified in the same terms as that axis. This is useful  for
        trendline annotations which should continue to indicate  the
        correct trend when zoomed.
    
        The 'ayref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['pixel']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self['ayref']

    @ayref.setter
    def ayref(self, val):
        self['ayref'] = val

    # bgcolor
    # -------
    @property
    def bgcolor(self):
        """
        Sets the background color of the annotation.
    
        The 'bgcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['bgcolor']

    @bgcolor.setter
    def bgcolor(self, val):
        self['bgcolor'] = val

    # bordercolor
    # -----------
    @property
    def bordercolor(self):
        """
        Sets the color of the border enclosing the annotation `text`.
    
        The 'bordercolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen

        Returns
        -------
        str
        """
        return self['bordercolor']

    @bordercolor.setter
    def bordercolor(self, val):
        self['bordercolor'] = val

    # borderpad
    # ---------
    @property
    def borderpad(self):
        """
        Sets the padding (in px) between the `text` and the enclosing
        border.
    
        The 'borderpad' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['borderpad']

    @borderpad.setter
    def borderpad(self, val):
        self['borderpad'] = val

    # borderwidth
    # -----------
    @property
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the annotation
        `text`.
    
        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['borderwidth']

    @borderwidth.setter
    def borderwidth(self, val):
        self['borderwidth'] = val

    # captureevents
    # -------------
    @property
    def captureevents(self):
        """
        Determines whether the annotation text box captures mouse move
        and click events, or allows those events to pass through to
        data points in the plot that may be behind the annotation. By
        default `captureevents` is *false* unless `hovertext` is
        provided. If you use the event `plotly_clickannotation` without
        `hovertext` you must explicitly enable `captureevents`.
    
        The 'captureevents' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['captureevents']

    @captureevents.setter
    def captureevents(self, val):
        self['captureevents'] = val

    # clicktoshow
    # -----------
    @property
    def clicktoshow(self):
        """
        Makes this annotation respond to clicks on the plot. If you
        click a data point that exactly matches the `x` and `y` values
        of this annotation, and it is hidden (visible: false), it will
        appear. In *onoff* mode, you must click the same point again to
        make it disappear, so if you click multiple points, you can
        show multiple annotations. In *onout* mode, a click anywhere
        else in the plot (on another data point or not) will hide this
        annotation. If you need to show/hide this annotation in
        response to different `x` or `y` values, you can set `xclick`
        and/or `yclick`. This is useful for example to label the side
        of a bar. To label markers though, `standoff` is preferred over
        `xclick` and `yclick`.
    
        The 'clicktoshow' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [False, 'onoff', 'onout']

        Returns
        -------
        Any
        """
        return self['clicktoshow']

    @clicktoshow.setter
    def clicktoshow(self, val):
        self['clicktoshow'] = val

    # font
    # ----
    @property
    def font(self):
        """
        Sets the annotation text font.
    
        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of plotly.graph_objs.layout.annotation.Font
          - A dict of string/value properties that will be passed
            to the Font constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.layout.annotation.Font
        """
        return self['font']

    @font.setter
    def font(self, val):
        self['font'] = val

    # height
    # ------
    @property
    def height(self):
        """
        Sets an explicit height for the text box. null (default) lets
        the text set the box height. Taller text will be clipped.
    
        The 'height' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self['height']

    @height.setter
    def height(self, val):
        self['height'] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of plotly.graph_objs.layout.annotation.Hoverlabel
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the background color of the hover label.
                    By default uses the annotation's `bgcolor` made
                    opaque, or white if it was transparent.
                bordercolor
                    Sets the border color of the hover label. By
                    default uses either dark grey or white, for
                    maximum contrast with `hoverlabel.bgcolor`.
                font
                    Sets the hover label text font. By default uses
                    the global hover font and size, with color from
                    `hoverlabel.bordercolor`.

        Returns
        -------
        plotly.graph_objs.layout.annotation.Hoverlabel
        """
        return self['hoverlabel']

    @hoverlabel.setter
    def hoverlabel(self, val):
        self['hoverlabel'] = val

    # hovertext
    # ---------
    @property
    def hovertext(self):
        """
        Sets text to appear when hovering over this annotation. If
        omitted or blank, no hover label will appear.
    
        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['hovertext']

    @hovertext.setter
    def hovertext(self, val):
        self['hovertext'] = val

    # name
    # ----
    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['name']

    @name.setter
    def name(self, val):
        self['name'] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the annotation (text + arrow).
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # showarrow
    # ---------
    @property
    def showarrow(self):
        """
        Determines whether or not the annotation is drawn with an
        arrow. If *true*, `text` is placed near the arrow's tail. If
        *false*, `text` lines up with the `x` and `y` provided.
    
        The 'showarrow' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showarrow']

    @showarrow.setter
    def showarrow(self, val):
        self['showarrow'] = val

    # standoff
    # --------
    @property
    def standoff(self):
        """
        Sets a distance, in pixels, to move the end arrowhead away from
        the position it is pointing at, for example to point at the
        edge of a marker independent of zoom. Note that this shortens
        the arrow from the `ax` / `ay` vector, in contrast to `xshift`
        / `yshift` which moves everything by this amount.
    
        The 'standoff' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['standoff']

    @standoff.setter
    def standoff(self, val):
        self['standoff'] = val

    # startarrowhead
    # --------------
    @property
    def startarrowhead(self):
        """
        Sets the start annotation arrow head style.
    
        The 'startarrowhead' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 8]

        Returns
        -------
        int
        """
        return self['startarrowhead']

    @startarrowhead.setter
    def startarrowhead(self, val):
        self['startarrowhead'] = val

    # startarrowsize
    # --------------
    @property
    def startarrowsize(self):
        """
        Sets the size of the start annotation arrow head, relative to
        `arrowwidth`. A value of 1 (default) gives a head about 3x as
        wide as the line.
    
        The 'startarrowsize' property is a number and may be specified as:
          - An int or float in the interval [0.3, inf]

        Returns
        -------
        int|float
        """
        return self['startarrowsize']

    @startarrowsize.setter
    def startarrowsize(self, val):
        self['startarrowsize'] = val

    # startstandoff
    # -------------
    @property
    def startstandoff(self):
        """
        Sets a distance, in pixels, to move the start arrowhead away
        from the position it is pointing at, for example to point at
        the edge of a marker independent of zoom. Note that this
        shortens the arrow from the `ax` / `ay` vector, in contrast to
        `xshift` / `yshift` which moves everything by this amount.
    
        The 'startstandoff' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['startstandoff']

    @startstandoff.setter
    def startstandoff(self, val):
        self['startstandoff'] = val

    # templateitemname
    # ----------------
    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.
    
        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['templateitemname']

    @templateitemname.setter
    def templateitemname(self, val):
        self['templateitemname'] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the text associated with this annotation. Plotly uses a
        subset of HTML tags to do things like newline (<br>), bold
        (<b></b>), italics (<i></i>), hyperlinks (<a href='...'></a>).
        Tags <em>, <sup>, <sub> <span> are also supported.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['text']

    @text.setter
    def text(self, val):
        self['text'] = val

    # textangle
    # ---------
    @property
    def textangle(self):
        """
        Sets the angle at which the `text` is drawn with respect to the
        horizontal.
    
        The 'textangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self['textangle']

    @textangle.setter
    def textangle(self, val):
        self['textangle'] = val

    # valign
    # ------
    @property
    def valign(self):
        """
        Sets the vertical alignment of the `text` within the box. Has
        an effect only if an explicit height is set to override the
        text height.
    
        The 'valign' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self['valign']

    @valign.setter
    def valign(self, val):
        self['valign'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this annotation is visible.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # width
    # -----
    @property
    def width(self):
        """
        Sets an explicit width for the text box. null (default) lets
        the text set the box width. Wider text will be clipped. There
        is no automatic wrapping; use <br> to start a new line.
    
        The 'width' property is a number and may be specified as:
          - An int or float in the interval [1, inf]

        Returns
        -------
        int|float
        """
        return self['width']

    @width.setter
    def width(self, val):
        self['width'] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the annotation's x position. If the axis `type` is *log*,
        then you must take the log of your desired range. If the axis
        `type` is *date*, it should be date strings, like date data,
        though Date objects and unix milliseconds will be accepted and
        converted to strings. If the axis `type` is *category*, it
        should be numbers, using the scale where each category is
        assigned a serial number from zero in the order it appears.
    
        The 'x' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # xanchor
    # -------
    @property
    def xanchor(self):
        """
        Sets the text box's horizontal position anchor This anchor
        binds the `x` position to the *left*, *center* or *right* of
        the annotation. For example, if `x` is set to 1, `xref` to
        *paper* and `xanchor` to *right* then the right-most portion of
        the annotation lines up with the right-most edge of the
        plotting area. If *auto*, the anchor is equivalent to *center*
        for data-referenced annotations or if there is an arrow,
        whereas for paper-referenced with no arrow, the anchor picked
        corresponds to the closest side.
    
        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        return self['xanchor']

    @xanchor.setter
    def xanchor(self, val):
        self['xanchor'] = val

    # xclick
    # ------
    @property
    def xclick(self):
        """
        Toggle this annotation when clicking a data point whose `x`
        value is `xclick` rather than the annotation's `x` value.
    
        The 'xclick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['xclick']

    @xclick.setter
    def xclick(self, val):
        self['xclick'] = val

    # xref
    # ----
    @property
    def xref(self):
        """
        Sets the annotation's x coordinate axis. If set to an x axis id
        (e.g. *x* or *x2*), the `x` position refers to an x coordinate
        If set to *paper*, the `x` position refers to the distance from
        the left side of the plotting area in normalized coordinates
        where 0 (1) corresponds to the left (right) side.
    
        The 'xref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^x([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self['xref']

    @xref.setter
    def xref(self, val):
        self['xref'] = val

    # xshift
    # ------
    @property
    def xshift(self):
        """
        Shifts the position of the whole annotation and arrow to the
        right (positive) or left (negative) by this many pixels.
    
        The 'xshift' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['xshift']

    @xshift.setter
    def xshift(self, val):
        self['xshift'] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the annotation's y position. If the axis `type` is *log*,
        then you must take the log of your desired range. If the axis
        `type` is *date*, it should be date strings, like date data,
        though Date objects and unix milliseconds will be accepted and
        converted to strings. If the axis `type` is *category*, it
        should be numbers, using the scale where each category is
        assigned a serial number from zero in the order it appears.
    
        The 'y' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # yanchor
    # -------
    @property
    def yanchor(self):
        """
        Sets the text box's vertical position anchor This anchor binds
        the `y` position to the *top*, *middle* or *bottom* of the
        annotation. For example, if `y` is set to 1, `yref` to *paper*
        and `yanchor` to *top* then the top-most portion of the
        annotation lines up with the top-most edge of the plotting
        area. If *auto*, the anchor is equivalent to *middle* for data-
        referenced annotations or if there is an arrow, whereas for
        paper-referenced with no arrow, the anchor picked corresponds
        to the closest side.
    
        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        return self['yanchor']

    @yanchor.setter
    def yanchor(self, val):
        self['yanchor'] = val

    # yclick
    # ------
    @property
    def yclick(self):
        """
        Toggle this annotation when clicking a data point whose `y`
        value is `yclick` rather than the annotation's `y` value.
    
        The 'yclick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['yclick']

    @yclick.setter
    def yclick(self, val):
        self['yclick'] = val

    # yref
    # ----
    @property
    def yref(self):
        """
        Sets the annotation's y coordinate axis. If set to an y axis id
        (e.g. *y* or *y2*), the `y` position refers to an y coordinate
        If set to *paper*, the `y` position refers to the distance from
        the bottom of the plotting area in normalized coordinates where
        0 (1) corresponds to the bottom (top).
    
        The 'yref' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['paper']
          - A string that matches one of the following regular expressions:
                ['^y([2-9]|[1-9][0-9]+)?$']

        Returns
        -------
        Any
        """
        return self['yref']

    @yref.setter
    def yref(self, val):
        self['yref'] = val

    # yshift
    # ------
    @property
    def yshift(self):
        """
        Shifts the position of the whole annotation and arrow up
        (positive) or down (negative) by this many pixels.
    
        The 'yshift' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['yshift']

    @yshift.setter
    def yshift(self, val):
        self['yshift'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        arrowcolor
            Sets the color of the annotation arrow.
        arrowhead
            Sets the end annotation arrow head style.
        arrowside
            Sets the annotation arrow head position.
        arrowsize
            Sets the size of the end annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        arrowwidth
            Sets the width (in px) of annotation arrow line.
        ax
            Sets the x component of the arrow tail about the arrow
            head. If `axref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from right
            to left (left to right). If `axref` is an axis, this is
            an absolute value on that axis, like `x`, NOT a
            relative value.
        axref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ax` is a relative
            offset in pixels  from `x`. If set to an x axis id
            (e.g. *x* or *x2*), `ax` is  specified in the same
            terms as that axis. This is useful  for trendline
            annotations which should continue to indicate  the
            correct trend when zoomed.
        ay
            Sets the y component of the arrow tail about the arrow
            head. If `ayref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from bottom
            to top (top to bottom). If `ayref` is an axis, this is
            an absolute value on that axis, like `y`, NOT a
            relative value.
        ayref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ay` is a relative
            offset in pixels  from `y`. If set to a y axis id (e.g.
            *y* or *y2*), `ay` is  specified in the same terms as
            that axis. This is useful  for trendline annotations
            which should continue to indicate  the correct trend
            when zoomed.
        bgcolor
            Sets the background color of the annotation.
        bordercolor
            Sets the color of the border enclosing the annotation
            `text`.
        borderpad
            Sets the padding (in px) between the `text` and the
            enclosing border.
        borderwidth
            Sets the width (in px) of the border enclosing the
            annotation `text`.
        captureevents
            Determines whether the annotation text box captures
            mouse move and click events, or allows those events to
            pass through to data points in the plot that may be
            behind the annotation. By default `captureevents` is
            *false* unless `hovertext` is provided. If you use the
            event `plotly_clickannotation` without `hovertext` you
            must explicitly enable `captureevents`.
        clicktoshow
            Makes this annotation respond to clicks on the plot. If
            you click a data point that exactly matches the `x` and
            `y` values of this annotation, and it is hidden
            (visible: false), it will appear. In *onoff* mode, you
            must click the same point again to make it disappear,
            so if you click multiple points, you can show multiple
            annotations. In *onout* mode, a click anywhere else in
            the plot (on another data point or not) will hide this
            annotation. If you need to show/hide this annotation in
            response to different `x` or `y` values, you can set
            `xclick` and/or `yclick`. This is useful for example to
            label the side of a bar. To label markers though,
            `standoff` is preferred over `xclick` and `yclick`.
        font
            Sets the annotation text font.
        height
            Sets an explicit height for the text box. null
            (default) lets the text set the box height. Taller text
            will be clipped.
        hoverlabel
            plotly.graph_objs.layout.annotation.Hoverlabel instance
            or dict with compatible properties
        hovertext
            Sets text to appear when hovering over this annotation.
            If omitted or blank, no hover label will appear.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the annotation (text + arrow).
        showarrow
            Determines whether or not the annotation is drawn with
            an arrow. If *true*, `text` is placed near the arrow's
            tail. If *false*, `text` lines up with the `x` and `y`
            provided.
        standoff
            Sets a distance, in pixels, to move the end arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        startarrowhead
            Sets the start annotation arrow head style.
        startarrowsize
            Sets the size of the start annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        startstandoff
            Sets a distance, in pixels, to move the start arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        text
            Sets the text associated with this annotation. Plotly
            uses a subset of HTML tags to do things like newline
            (<br>), bold (<b></b>), italics (<i></i>), hyperlinks
            (<a href='...'></a>). Tags <em>, <sup>, <sub> <span>
            are also supported.
        textangle
            Sets the angle at which the `text` is drawn with
            respect to the horizontal.
        valign
            Sets the vertical alignment of the `text` within the
            box. Has an effect only if an explicit height is set to
            override the text height.
        visible
            Determines whether or not this annotation is visible.
        width
            Sets an explicit width for the text box. null (default)
            lets the text set the box width. Wider text will be
            clipped. There is no automatic wrapping; use <br> to
            start a new line.
        x
            Sets the annotation's x position. If the axis `type` is
            *log*, then you must take the log of your desired
            range. If the axis `type` is *date*, it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is *category*, it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        xanchor
            Sets the text box's horizontal position anchor This
            anchor binds the `x` position to the *left*, *center*
            or *right* of the annotation. For example, if `x` is
            set to 1, `xref` to *paper* and `xanchor` to *right*
            then the right-most portion of the annotation lines up
            with the right-most edge of the plotting area. If
            *auto*, the anchor is equivalent to *center* for data-
            referenced annotations or if there is an arrow, whereas
            for paper-referenced with no arrow, the anchor picked
            corresponds to the closest side.
        xclick
            Toggle this annotation when clicking a data point whose
            `x` value is `xclick` rather than the annotation's `x`
            value.
        xref
            Sets the annotation's x coordinate axis. If set to an x
            axis id (e.g. *x* or *x2*), the `x` position refers to
            an x coordinate If set to *paper*, the `x` position
            refers to the distance from the left side of the
            plotting area in normalized coordinates where 0 (1)
            corresponds to the left (right) side.
        xshift
            Shifts the position of the whole annotation and arrow
            to the right (positive) or left (negative) by this many
            pixels.
        y
            Sets the annotation's y position. If the axis `type` is
            *log*, then you must take the log of your desired
            range. If the axis `type` is *date*, it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is *category*, it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        yanchor
            Sets the text box's vertical position anchor This
            anchor binds the `y` position to the *top*, *middle* or
            *bottom* of the annotation. For example, if `y` is set
            to 1, `yref` to *paper* and `yanchor` to *top* then the
            top-most portion of the annotation lines up with the
            top-most edge of the plotting area. If *auto*, the
            anchor is equivalent to *middle* for data-referenced
            annotations or if there is an arrow, whereas for paper-
            referenced with no arrow, the anchor picked corresponds
            to the closest side.
        yclick
            Toggle this annotation when clicking a data point whose
            `y` value is `yclick` rather than the annotation's `y`
            value.
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. *y* or *y2*), the `y` position refers to
            an y coordinate If set to *paper*, the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        yshift
            Shifts the position of the whole annotation and arrow
            up (positive) or down (negative) by this many pixels.
        """

    def __init__(
        self,
        arg=None,
        align=None,
        arrowcolor=None,
        arrowhead=None,
        arrowside=None,
        arrowsize=None,
        arrowwidth=None,
        ax=None,
        axref=None,
        ay=None,
        ayref=None,
        bgcolor=None,
        bordercolor=None,
        borderpad=None,
        borderwidth=None,
        captureevents=None,
        clicktoshow=None,
        font=None,
        height=None,
        hoverlabel=None,
        hovertext=None,
        name=None,
        opacity=None,
        showarrow=None,
        standoff=None,
        startarrowhead=None,
        startarrowsize=None,
        startstandoff=None,
        templateitemname=None,
        text=None,
        textangle=None,
        valign=None,
        visible=None,
        width=None,
        x=None,
        xanchor=None,
        xclick=None,
        xref=None,
        xshift=None,
        y=None,
        yanchor=None,
        yclick=None,
        yref=None,
        yshift=None,
        **kwargs
    ):
        """
        Construct a new Annotation object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.Annotation
        align
            Sets the horizontal alignment of the `text` within the
            box. Has an effect only if `text` spans more two or
            more lines (i.e. `text` contains one or more <br> HTML
            tags) or if an explicit width is set to override the
            text width.
        arrowcolor
            Sets the color of the annotation arrow.
        arrowhead
            Sets the end annotation arrow head style.
        arrowside
            Sets the annotation arrow head position.
        arrowsize
            Sets the size of the end annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        arrowwidth
            Sets the width (in px) of annotation arrow line.
        ax
            Sets the x component of the arrow tail about the arrow
            head. If `axref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from right
            to left (left to right). If `axref` is an axis, this is
            an absolute value on that axis, like `x`, NOT a
            relative value.
        axref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ax` is a relative
            offset in pixels  from `x`. If set to an x axis id
            (e.g. *x* or *x2*), `ax` is  specified in the same
            terms as that axis. This is useful  for trendline
            annotations which should continue to indicate  the
            correct trend when zoomed.
        ay
            Sets the y component of the arrow tail about the arrow
            head. If `ayref` is `pixel`, a positive (negative)
            component corresponds to an arrow pointing from bottom
            to top (top to bottom). If `ayref` is an axis, this is
            an absolute value on that axis, like `y`, NOT a
            relative value.
        ayref
            Indicates in what terms the tail of the annotation
            (ax,ay)  is specified. If `pixel`, `ay` is a relative
            offset in pixels  from `y`. If set to a y axis id (e.g.
            *y* or *y2*), `ay` is  specified in the same terms as
            that axis. This is useful  for trendline annotations
            which should continue to indicate  the correct trend
            when zoomed.
        bgcolor
            Sets the background color of the annotation.
        bordercolor
            Sets the color of the border enclosing the annotation
            `text`.
        borderpad
            Sets the padding (in px) between the `text` and the
            enclosing border.
        borderwidth
            Sets the width (in px) of the border enclosing the
            annotation `text`.
        captureevents
            Determines whether the annotation text box captures
            mouse move and click events, or allows those events to
            pass through to data points in the plot that may be
            behind the annotation. By default `captureevents` is
            *false* unless `hovertext` is provided. If you use the
            event `plotly_clickannotation` without `hovertext` you
            must explicitly enable `captureevents`.
        clicktoshow
            Makes this annotation respond to clicks on the plot. If
            you click a data point that exactly matches the `x` and
            `y` values of this annotation, and it is hidden
            (visible: false), it will appear. In *onoff* mode, you
            must click the same point again to make it disappear,
            so if you click multiple points, you can show multiple
            annotations. In *onout* mode, a click anywhere else in
            the plot (on another data point or not) will hide this
            annotation. If you need to show/hide this annotation in
            response to different `x` or `y` values, you can set
            `xclick` and/or `yclick`. This is useful for example to
            label the side of a bar. To label markers though,
            `standoff` is preferred over `xclick` and `yclick`.
        font
            Sets the annotation text font.
        height
            Sets an explicit height for the text box. null
            (default) lets the text set the box height. Taller text
            will be clipped.
        hoverlabel
            plotly.graph_objs.layout.annotation.Hoverlabel instance
            or dict with compatible properties
        hovertext
            Sets text to appear when hovering over this annotation.
            If omitted or blank, no hover label will appear.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        opacity
            Sets the opacity of the annotation (text + arrow).
        showarrow
            Determines whether or not the annotation is drawn with
            an arrow. If *true*, `text` is placed near the arrow's
            tail. If *false*, `text` lines up with the `x` and `y`
            provided.
        standoff
            Sets a distance, in pixels, to move the end arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        startarrowhead
            Sets the start annotation arrow head style.
        startarrowsize
            Sets the size of the start annotation arrow head,
            relative to `arrowwidth`. A value of 1 (default) gives
            a head about 3x as wide as the line.
        startstandoff
            Sets a distance, in pixels, to move the start arrowhead
            away from the position it is pointing at, for example
            to point at the edge of a marker independent of zoom.
            Note that this shortens the arrow from the `ax` / `ay`
            vector, in contrast to `xshift` / `yshift` which moves
            everything by this amount.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        text
            Sets the text associated with this annotation. Plotly
            uses a subset of HTML tags to do things like newline
            (<br>), bold (<b></b>), italics (<i></i>), hyperlinks
            (<a href='...'></a>). Tags <em>, <sup>, <sub> <span>
            are also supported.
        textangle
            Sets the angle at which the `text` is drawn with
            respect to the horizontal.
        valign
            Sets the vertical alignment of the `text` within the
            box. Has an effect only if an explicit height is set to
            override the text height.
        visible
            Determines whether or not this annotation is visible.
        width
            Sets an explicit width for the text box. null (default)
            lets the text set the box width. Wider text will be
            clipped. There is no automatic wrapping; use <br> to
            start a new line.
        x
            Sets the annotation's x position. If the axis `type` is
            *log*, then you must take the log of your desired
            range. If the axis `type` is *date*, it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is *category*, it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        xanchor
            Sets the text box's horizontal position anchor This
            anchor binds the `x` position to the *left*, *center*
            or *right* of the annotation. For example, if `x` is
            set to 1, `xref` to *paper* and `xanchor` to *right*
            then the right-most portion of the annotation lines up
            with the right-most edge of the plotting area. If
            *auto*, the anchor is equivalent to *center* for data-
            referenced annotations or if there is an arrow, whereas
            for paper-referenced with no arrow, the anchor picked
            corresponds to the closest side.
        xclick
            Toggle this annotation when clicking a data point whose
            `x` value is `xclick` rather than the annotation's `x`
            value.
        xref
            Sets the annotation's x coordinate axis. If set to an x
            axis id (e.g. *x* or *x2*), the `x` position refers to
            an x coordinate If set to *paper*, the `x` position
            refers to the distance from the left side of the
            plotting area in normalized coordinates where 0 (1)
            corresponds to the left (right) side.
        xshift
            Shifts the position of the whole annotation and arrow
            to the right (positive) or left (negative) by this many
            pixels.
        y
            Sets the annotation's y position. If the axis `type` is
            *log*, then you must take the log of your desired
            range. If the axis `type` is *date*, it should be date
            strings, like date data, though Date objects and unix
            milliseconds will be accepted and converted to strings.
            If the axis `type` is *category*, it should be numbers,
            using the scale where each category is assigned a
            serial number from zero in the order it appears.
        yanchor
            Sets the text box's vertical position anchor This
            anchor binds the `y` position to the *top*, *middle* or
            *bottom* of the annotation. For example, if `y` is set
            to 1, `yref` to *paper* and `yanchor` to *top* then the
            top-most portion of the annotation lines up with the
            top-most edge of the plotting area. If *auto*, the
            anchor is equivalent to *middle* for data-referenced
            annotations or if there is an arrow, whereas for paper-
            referenced with no arrow, the anchor picked corresponds
            to the closest side.
        yclick
            Toggle this annotation when clicking a data point whose
            `y` value is `yclick` rather than the annotation's `y`
            value.
        yref
            Sets the annotation's y coordinate axis. If set to an y
            axis id (e.g. *y* or *y2*), the `y` position refers to
            an y coordinate If set to *paper*, the `y` position
            refers to the distance from the bottom of the plotting
            area in normalized coordinates where 0 (1) corresponds
            to the bottom (top).
        yshift
            Shifts the position of the whole annotation and arrow
            up (positive) or down (negative) by this many pixels.

        Returns
        -------
        Annotation
        """
        super(Annotation, self).__init__('annotations')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.Annotation 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.Annotation"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout import (annotation as v_annotation)

        # Initialize validators
        # ---------------------
        self._validators['align'] = v_annotation.AlignValidator()
        self._validators['arrowcolor'] = v_annotation.ArrowcolorValidator()
        self._validators['arrowhead'] = v_annotation.ArrowheadValidator()
        self._validators['arrowside'] = v_annotation.ArrowsideValidator()
        self._validators['arrowsize'] = v_annotation.ArrowsizeValidator()
        self._validators['arrowwidth'] = v_annotation.ArrowwidthValidator()
        self._validators['ax'] = v_annotation.AxValidator()
        self._validators['axref'] = v_annotation.AxrefValidator()
        self._validators['ay'] = v_annotation.AyValidator()
        self._validators['ayref'] = v_annotation.AyrefValidator()
        self._validators['bgcolor'] = v_annotation.BgcolorValidator()
        self._validators['bordercolor'] = v_annotation.BordercolorValidator()
        self._validators['borderpad'] = v_annotation.BorderpadValidator()
        self._validators['borderwidth'] = v_annotation.BorderwidthValidator()
        self._validators['captureevents'
                        ] = v_annotation.CaptureeventsValidator()
        self._validators['clicktoshow'] = v_annotation.ClicktoshowValidator()
        self._validators['font'] = v_annotation.FontValidator()
        self._validators['height'] = v_annotation.HeightValidator()
        self._validators['hoverlabel'] = v_annotation.HoverlabelValidator()
        self._validators['hovertext'] = v_annotation.HovertextValidator()
        self._validators['name'] = v_annotation.NameValidator()
        self._validators['opacity'] = v_annotation.OpacityValidator()
        self._validators['showarrow'] = v_annotation.ShowarrowValidator()
        self._validators['standoff'] = v_annotation.StandoffValidator()
        self._validators['startarrowhead'
                        ] = v_annotation.StartarrowheadValidator()
        self._validators['startarrowsize'
                        ] = v_annotation.StartarrowsizeValidator()
        self._validators['startstandoff'
                        ] = v_annotation.StartstandoffValidator()
        self._validators['templateitemname'
                        ] = v_annotation.TemplateitemnameValidator()
        self._validators['text'] = v_annotation.TextValidator()
        self._validators['textangle'] = v_annotation.TextangleValidator()
        self._validators['valign'] = v_annotation.ValignValidator()
        self._validators['visible'] = v_annotation.VisibleValidator()
        self._validators['width'] = v_annotation.WidthValidator()
        self._validators['x'] = v_annotation.XValidator()
        self._validators['xanchor'] = v_annotation.XanchorValidator()
        self._validators['xclick'] = v_annotation.XclickValidator()
        self._validators['xref'] = v_annotation.XrefValidator()
        self._validators['xshift'] = v_annotation.XshiftValidator()
        self._validators['y'] = v_annotation.YValidator()
        self._validators['yanchor'] = v_annotation.YanchorValidator()
        self._validators['yclick'] = v_annotation.YclickValidator()
        self._validators['yref'] = v_annotation.YrefValidator()
        self._validators['yshift'] = v_annotation.YshiftValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('align', None)
        self.align = align if align is not None else _v
        _v = arg.pop('arrowcolor', None)
        self.arrowcolor = arrowcolor if arrowcolor is not None else _v
        _v = arg.pop('arrowhead', None)
        self.arrowhead = arrowhead if arrowhead is not None else _v
        _v = arg.pop('arrowside', None)
        self.arrowside = arrowside if arrowside is not None else _v
        _v = arg.pop('arrowsize', None)
        self.arrowsize = arrowsize if arrowsize is not None else _v
        _v = arg.pop('arrowwidth', None)
        self.arrowwidth = arrowwidth if arrowwidth is not None else _v
        _v = arg.pop('ax', None)
        self.ax = ax if ax is not None else _v
        _v = arg.pop('axref', None)
        self.axref = axref if axref is not None else _v
        _v = arg.pop('ay', None)
        self.ay = ay if ay is not None else _v
        _v = arg.pop('ayref', None)
        self.ayref = ayref if ayref is not None else _v
        _v = arg.pop('bgcolor', None)
        self.bgcolor = bgcolor if bgcolor is not None else _v
        _v = arg.pop('bordercolor', None)
        self.bordercolor = bordercolor if bordercolor is not None else _v
        _v = arg.pop('borderpad', None)
        self.borderpad = borderpad if borderpad is not None else _v
        _v = arg.pop('borderwidth', None)
        self.borderwidth = borderwidth if borderwidth is not None else _v
        _v = arg.pop('captureevents', None)
        self.captureevents = captureevents if captureevents is not None else _v
        _v = arg.pop('clicktoshow', None)
        self.clicktoshow = clicktoshow if clicktoshow is not None else _v
        _v = arg.pop('font', None)
        self.font = font if font is not None else _v
        _v = arg.pop('height', None)
        self.height = height if height is not None else _v
        _v = arg.pop('hoverlabel', None)
        self.hoverlabel = hoverlabel if hoverlabel is not None else _v
        _v = arg.pop('hovertext', None)
        self.hovertext = hovertext if hovertext is not None else _v
        _v = arg.pop('name', None)
        self.name = name if name is not None else _v
        _v = arg.pop('opacity', None)
        self.opacity = opacity if opacity is not None else _v
        _v = arg.pop('showarrow', None)
        self.showarrow = showarrow if showarrow is not None else _v
        _v = arg.pop('standoff', None)
        self.standoff = standoff if standoff is not None else _v
        _v = arg.pop('startarrowhead', None)
        self.startarrowhead = startarrowhead if startarrowhead is not None else _v
        _v = arg.pop('startarrowsize', None)
        self.startarrowsize = startarrowsize if startarrowsize is not None else _v
        _v = arg.pop('startstandoff', None)
        self.startstandoff = startstandoff if startstandoff is not None else _v
        _v = arg.pop('templateitemname', None)
        self.templateitemname = templateitemname if templateitemname is not None else _v
        _v = arg.pop('text', None)
        self.text = text if text is not None else _v
        _v = arg.pop('textangle', None)
        self.textangle = textangle if textangle is not None else _v
        _v = arg.pop('valign', None)
        self.valign = valign if valign is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v
        _v = arg.pop('width', None)
        self.width = width if width is not None else _v
        _v = arg.pop('x', None)
        self.x = x if x is not None else _v
        _v = arg.pop('xanchor', None)
        self.xanchor = xanchor if xanchor is not None else _v
        _v = arg.pop('xclick', None)
        self.xclick = xclick if xclick is not None else _v
        _v = arg.pop('xref', None)
        self.xref = xref if xref is not None else _v
        _v = arg.pop('xshift', None)
        self.xshift = xshift if xshift is not None else _v
        _v = arg.pop('y', None)
        self.y = y if y is not None else _v
        _v = arg.pop('yanchor', None)
        self.yanchor = yanchor if yanchor is not None else _v
        _v = arg.pop('yclick', None)
        self.yclick = yclick if yclick is not None else _v
        _v = arg.pop('yref', None)
        self.yref = yref if yref is not None else _v
        _v = arg.pop('yshift', None)
        self.yshift = yshift if yshift is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
