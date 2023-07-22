import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_table
import base64
import io
from PIL import Image
from deepface import DeepFace
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1('Emotion Detector'),
    html.P("This application detects human emotions from uploaded images. Please upload an image and see the result."),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select an Image')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=False
    ),
    html.Div(id='output-image-upload'),
])


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        im = Image.open(io.BytesIO(decoded))
        im.save('tmp/' + filename)
        result = DeepFace.analyze('tmp/' + filename, actions=['emotion'])
        emotion = result[0]['emotion']
        df = pd.DataFrame([emotion.values()], columns=emotion.keys())

    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return html.Div([
        html.H5(filename),
        # HTML images accept base64 encoded strings in the same format
        html.Img(src=contents, style={'width': '300px'}),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            style_cell={'textAlign': 'left'},
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            }
        ),
        html.Hr(),
    ])


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'))
def update_output(contents, name):
    if contents is not None:
        children = parse_contents(contents, name)
        return children


if __name__ == '__main__':
    app.run_server(debug=True)
