
LABELS = (
    # {
    #     "attributes" : {
    #         "type" : "rect",
    #         "class" : "Type",
    #         "id": [
    #             "P.v.R",
    #             "P.v.T",
    #             "P.v.S",
    #             "P.v.G",
    #             "P.v.-Unknown",
    #             "P.f.R",
    #             "P.f.T",
    #             "P.f.S",
    #             "P.f.G",
    #             "P.f.-Unknown",
    #             "P.m.R",
    #             "P.m.T",
    #             "P.m.S",
    #             "P.m.G",
    #             "P.m.-Unknown",
    #             "MP-Unknown-Type",
    #             "RBC",
    #             "WBC",
    #             "PLT"
    #         ]
    #     },
    #     "item": "sloth.items.RectItem",
    #     "inserter": "sloth.items.RectItemInserter",
    #     "text": "Type"
    # },
    {
        'attributes': {
            'class':      'Face',
            'color' : 'yellow'
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   'f',
        'text':     'Face(yellow)',
    },
    {
        'attributes': {
            'class':      'rect',
            'color' : 'red'
        },
        'inserter': 'sloth.items.RectItemInserter',
        'item':     'sloth.items.RectItem',
        'hotkey':   'r',
        'text':     'Rectangle(red)',
    },
    {
        'attributes': {
            'class':    'point',
            'color' : 'green'
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     'sloth.items.PointItem',
        'hotkey':   'p',
        'text':     'Point(green)',
    },
    {
        'attributes': {
            'class':    'polygon',
            'color' : 'white'
        },
        'inserter': 'sloth.items.PolygonItemInserter',
        'item':     'sloth.items.PolygonItem',
        'hotkey':   'o',
        'text':     'Polygon(white)',
    }
)
