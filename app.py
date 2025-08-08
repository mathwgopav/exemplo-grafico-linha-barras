import dash
from dash import dcc, html, Input, Output, callback
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

# Criando dados sintéticos baseados na imagem
def generate_synthetic_data():
    np.random.seed(42)
    
    # Dados para o gráfico de linha (2010-2023)
    years = list(range(2010, 2024))
    
    # Dados baseados na imagem para Fortaleza
    fortaleza_data = [36755, 37577, 38195, 39512, 37451, 35833, 32376, 29676, 28500]
    # Completar os anos restantes com tendência de declínio
    for i in range(len(fortaleza_data), len(years)):
        fortaleza_data.append(max(25000, fortaleza_data[-1] - np.random.randint(500, 1500)))
    
    # Dados para CE (estado) - valores menores que Fortaleza
    ce_data = [int(fortaleza_data[i] * 0.8 + np.random.randint(-2000, 2000)) for i in range(len(years))]
    
    # Dados para Brasil - valores maiores que Fortaleza
    brasil_data = [int(fortaleza_data[i] * 2.5 + np.random.randint(-5000, 5000)) for i in range(len(years))]
    
    # Dados para mortalidade infantil por raça/cor - 2023 (baseados na imagem)
    mortality_data = {
        'Brasil': {
            'Branca': 38.06,
            'Preta': 3.28,
            'Amarela': 1.45,
            'Parda': 50.01,
            'Indígena': 2.39,
            'Raça/cor ignorada': 6.11
        },
        'Ceará': {
            'Branca': 19.59,
            'Preta': 0.87,
            'Amarela': 1.45,
            'Parda': 66.44,
            'Indígena': 0.00,
            'Raça/cor ignorada': 11.60
        },
        'Fortaleza - CE': {
            'Branca': 20.81,
            'Preta': 0.87,
            'Amarela': 1.45,
            'Parda': 58.38,
            'Indígena': 0.00,
            'Raça/cor ignorada': 18.50
        }
    }
    
    # Dados para o gráfico de donut INC (baseados na imagem)
    inc_data = {
        'Crianças em situação de pobreza': 8.75,
        'Crianças de famílias monoparentais': 4.26,
        'Crianças com mães/cuidadores economicamente ativos': 23.98,
        'Crianças com deficiência': 2.00
    }
    
    return years, fortaleza_data, ce_data, brasil_data, mortality_data, inc_data

# Criando o aplicativo
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard de Indicadores"

# Gerando dados
years, fortaleza_data, ce_data, brasil_data, mortality_data, inc_data = generate_synthetic_data()

# Layout do aplicativo
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1([
                DashIconify(icon="mdi:chart-line", width=30, className="me-2"),
                "Dashboard de Indicadores"
            ], className="text-center mb-4"),
            html.Hr()
        ])
    ]),
    
    dbc.Row([
        # Gráfico de linha (esquerda)
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5([
                        DashIconify(icon="mdi:chart-line", width=20, className="me-2"),
                        "Nascidos vivos ",
                        DashIconify(icon="mdi:information", width=16, className="text-muted")
                    ], className="card-title mb-0")
                ]),
                dbc.CardBody([
                    dcc.Graph(
                        id='line-chart',
                        style={'height': '400px'}
                    ),
                    html.Div([
                        html.Span("Fonte: Ministério da Saúde - DATASUS (2010 - 2023)", 
                                 className="text-muted small"),
                        dbc.Button([
                            DashIconify(icon="mdi:information-outline", width=16, className="me-1"),
                            "Notas Técnicas"
                        ], id="open-modal-line", color="link", size="sm", className="ms-2")
                    ], className="d-flex justify-content-between align-items-center mt-2")
                ])
            ], className="shadow-sm border-0")
        ], width=6),
        
        # Gráfico de barras (direita)
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5([
                        DashIconify(icon="mdi:chart-bar", width=20, className="me-2"),
                        "Mortalidade infantil - por raça/cor ",
                        DashIconify(icon="mdi:information", width=16, className="text-muted")
                    ], className="card-title mb-0")
                ]),
                dbc.CardBody([
                    dcc.Graph(
                        id='bar-chart',
                        style={'height': '400px'}
                    ),
                    html.Div([
                        html.Span("Fonte: Ministério da Saúde - DATASUS (2023)", 
                                 className="text-muted small"),
                        dbc.Button([
                            DashIconify(icon="mdi:information-outline", width=16, className="me-1"),
                            "Notas Técnicas"
                        ], id="open-modal-bar", color="link", size="sm", className="ms-2")
                    ], className="d-flex justify-content-between align-items-center mt-2")
                ])
            ], className="shadow-sm border-0")
        ], width=6)
    ], className="mb-4"),
    
    # Novo card com gráfico de donut INC
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5([
                        DashIconify(icon="mdi:chart-donut", width=20, className="me-2"),
                        "Detalhamento - INC - Índice de Necessidade de Creche Estados e Capitais ",
                        DashIconify(icon="mdi:information", width=16, className="text-muted")
                    ], className="card-title mb-0")
                ]),
                dbc.CardBody([
                    dcc.Graph(
                        id='donut-chart',
                        style={'height': '400px'}
                    ),
                    html.Div([
                        html.Span("Fonte: Fundação Maria Cecília Souto Vidigal (2023). Atualizado com base na PNAD.", 
                                 className="text-muted small"),
                        dbc.Button([
                            DashIconify(icon="mdi:information-outline", width=16, className="me-1"),
                            "Notas Técnicas"
                        ], id="open-modal-donut", color="link", size="sm", className="ms-2")
                    ], className="d-flex justify-content-between align-items-center mt-2")
                ])
            ], className="shadow-sm border-0")
        ], width=12)
    ], className="mb-4"),
    
    # Cards de estatísticas
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        DashIconify(icon="mdi:city", width=30, className="text-primary"),
                        html.H4("Fortaleza - CE", className="mt-2 mb-1"),
                        html.P("Dados da capital", className="text-muted mb-0")
                    ], className="text-center")
                ])
            ], className="shadow-sm border-0 h-100")
        ], width=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        DashIconify(icon="mdi:map-marker", width=30, className="text-success"),
                        html.H4("Ceará", className="mt-2 mb-1"),
                        html.P("Dados do estado", className="text-muted mb-0")
                    ], className="text-center")
                ])
            ], className="shadow-sm border-0 h-100")
        ], width=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        DashIconify(icon="mdi:earth", width=30, className="text-info"),
                        html.H4("Brasil", className="mt-2 mb-1"),
                        html.P("Dados nacionais", className="text-muted mb-0")
                    ], className="text-center")
                ])
            ], className="shadow-sm border-0 h-100")
        ], width=4)
    ]),
    
    # Modais para Notas Técnicas
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Notas Técnicas - Nascidos vivos")),
        dbc.ModalBody([
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
            html.P("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
            html.P("Fontes primárias: Lorem Ipsum Nascidos Vivos (1994-presente) e Lorem Ipsum Óbitos Infantis (1996-presente).")
        ]),
        dbc.ModalFooter(
            dbc.Button("Fechar", id="close-modal-line", className="ms-auto")
        ),
    ], id="modal-line", is_open=False),
    
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Notas Técnicas - Mortalidade infantil por raça/cor")),
        dbc.ModalBody([
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
            html.P("Fontes primárias: Lorem Ipsum Óbitos Infantis (1996-presente).")
        ]),
        dbc.ModalFooter(
            dbc.Button("Fechar", id="close-modal-bar", className="ms-auto")
        ),
    ], id="modal-bar", is_open=False),
    
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Notas Técnicas - INC - Índice de Necessidade de Creche")),
        dbc.ModalBody([
            html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."),
            html.P("O Índice de Necessidade de Creche (INC) é uma ferramenta que identifica crianças que mais precisam de vagas em creches públicas."),
            html.P("Fontes primárias: Fundação Maria Cecília Souto Vidigal e PNAD.")
        ]),
        dbc.ModalFooter(
            dbc.Button("Fechar", id="close-modal-donut", className="ms-auto")
        ),
    ], id="modal-donut", is_open=False)
], fluid=True)

# Callback para o gráfico de linha
@app.callback(
    Output('line-chart', 'figure'),
    [Input('line-chart', 'clickData')]
)
def update_line_chart(click_data):
    fig = go.Figure()
    
    # Sempre mostrar as 3 linhas
    # Fortaleza - CE
    fig.add_trace(go.Scatter(
        x=years,
        y=fortaleza_data,
        mode='lines+markers',
        name='Fortaleza - CE',
        line=dict(
            color='#1f77b4',
            width=3
        ),
        marker=dict(
            size=8,
            symbol='circle',
            line=dict(width=2, color='white')
        ),
        hovertemplate='<b>Fortaleza - CE</b><br>' +
                     'Ano: %{x}<br>' +
                     'Nascimentos: %{y:,.0f}<br>' +
                     '<extra></extra>',
        hoverlabel=dict(
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#1f77b4',
            font_size=12
        )
    ))
    
    # CE
    fig.add_trace(go.Scatter(
        x=years,
        y=ce_data,
        mode='lines+markers',
        name='CE',
        line=dict(
            color='#7f7f7f',
            width=2
        ),
        marker=dict(
            size=6,
            symbol='diamond',
            line=dict(width=2, color='white')
        ),
        hovertemplate='<b>CE</b><br>' +
                     'Ano: %{x}<br>' +
                     'Nascimentos: %{y:,.0f}<br>' +
                     '<extra></extra>',
        hoverlabel=dict(
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#7f7f7f',
            font_size=12
        )
    ))
    
    # Brasil
    fig.add_trace(go.Scatter(
        x=years,
        y=brasil_data,
        mode='lines+markers',
        name='Brasil',
        line=dict(
            color='#7f7f7f',
            width=2
        ),
        marker=dict(
            size=6,
            symbol='square',
            line=dict(width=2, color='white')
        ),
        hovertemplate='<b>Brasil</b><br>' +
                     'Ano: %{x}<br>' +
                     'Nascimentos: %{y:,.0f}<br>' +
                     '<extra></extra>',
        hoverlabel=dict(
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#7f7f7f',
            font_size=12
        )
    ))
    
    fig.update_layout(
        title={
            'text': 'Nascidos vivos',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2c3e50'}
        },
        xaxis=dict(
            title='Ano',
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)',
            zeroline=False
        ),
        yaxis=dict(
            title='Nascimentos',
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)',
            zeroline=False
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='closest',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=50, r=50, t=80, b=50),
        font=dict(family="Arial, sans-serif")
    )
    
    return fig

# Callback para o gráfico de barras
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('bar-chart', 'clickData')]
)
def update_bar_chart(click_data):
    fig = go.Figure()
    
    # Categorias de raça/cor
    categories = ['Branca', 'Preta', 'Amarela', 'Parda', 'Indígena', 'Raça/cor ignorada']
    
    # Cores para cada localidade
    colors = {
        'Brasil': '#2ca02c',  # Verde
        'Ceará': '#d62728',   # Vermelho
        'Fortaleza - CE': '#1f77b4'  # Azul
    }
    
    # Adicionar barras para cada localidade
    for i, location in enumerate(['Brasil', 'Ceará', 'Fortaleza - CE']):
        values = [mortality_data[location][cat] for cat in categories]
        
        fig.add_trace(go.Bar(
            x=categories,
            y=values,
            name=location,
            marker_color=colors[location],
            hovertemplate='<b>%{fullData.name}</b><br>' +
                         'Raça/Cor: %{x}<br>' +
                         'Percentual: %{y:.2f}%<br>' +
                         '<extra></extra>',
            hoverlabel=dict(
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor=colors[location],
                font_size=12
            )
        ))
    
    fig.update_layout(
        title={
            'text': 'Mortalidade infantil - por raça/cor',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2c3e50'}
        },
        xaxis=dict(
            title='Raça/Cor',
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            title='Percentual',
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(128,128,128,0.2)',
            zeroline=False,
            range=[0, 80]
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=50, r=50, t=80, b=50),
        font=dict(family="Arial, sans-serif"),
        barmode='group'  # Barras agrupadas lado a lado
    )
    
    return fig

# Callback para o gráfico de donut
@app.callback(
    Output('donut-chart', 'figure'),
    [Input('donut-chart', 'clickData')]
)
def update_donut_chart(click_data):
    # Cores baseadas na imagem
    colors = ['#8B4513', '#8B0000', '#FF0000', '#FFB6C1']  # Roxo escuro, vermelho escuro, vermelho, rosa claro
    
    fig = go.Figure(data=[go.Pie(
        labels=list(inc_data.keys()),
        values=list(inc_data.values()),
        hole=0.6,  # Tamanho do buraco para criar o efeito donut
        marker_colors=colors,
        textinfo='percent+label',
        textposition='outside',
        hovertemplate='<b>%{label}</b><br>' +
                     'Percentual: %{percent:.2f}%<br>' +
                     'Valor: %{value:.2f}%<br>' +
                     '<extra></extra>',
        hoverlabel=dict(
            bgcolor='rgba(255,255,255,0.9)',
            font_size=12
        )
    )])
    
    fig.update_layout(
        title={
            'text': 'Detalhamento - INC - Índice de Necessidade de Creche Estados e Capitais',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': '#2c3e50'}
        },
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02
        ),
        margin=dict(l=50, r=150, t=80, b=50),
        font=dict(family="Arial, sans-serif")
    )
    
    return fig

# Callbacks para os modais
@app.callback(
    Output("modal-line", "is_open"),
    [Input("open-modal-line", "n_clicks"),
     Input("close-modal-line", "n_clicks")],
    prevent_initial_call=True,
)
def toggle_modal_line(n_open, n_close):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == "open-modal-line":
            return True
        elif button_id == "close-modal-line":
            return False
    return False

@app.callback(
    Output("modal-bar", "is_open"),
    [Input("open-modal-bar", "n_clicks"),
     Input("close-modal-bar", "n_clicks")],
    prevent_initial_call=True,
)
def toggle_modal_bar(n_open, n_close):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == "open-modal-bar":
            return True
        elif button_id == "close-modal-bar":
            return False
    return False

@app.callback(
    Output("modal-donut", "is_open"),
    [Input("open-modal-donut", "n_clicks"),
     Input("close-modal-donut", "n_clicks")],
    prevent_initial_call=True,
)
def toggle_modal_donut(n_open, n_close):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == "open-modal-donut":
            return True
        elif button_id == "close-modal-donut":
            return False
    return False

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
