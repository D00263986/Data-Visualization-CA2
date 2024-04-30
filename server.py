import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("healthcare_dataset.csv")

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define age groups
bins = [0, 18, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Define the layout for the "Age Analysis" page
def age_analysis_layout():
    
    # Dropdown for selecting gender
    gender_options = [{'label': 'All Genders', 'value': 'All'}] + [{'label': gender, 'value': gender} for gender in df['Gender'].unique()]
    gender_dropdown = dcc.Dropdown(
        id='gender-dropdown',
        options=gender_options,
        value='All',
        clearable=False,
        style={'width': '200px'}
    )
    
    # Dropdown for selecting blood type
    blood_type_options = [{'label': 'All Blood Types', 'value': 'All'}] + [{'label': blood_type, 'value': blood_type} for blood_type in df['Blood Type'].unique()]
    blood_type_dropdown = dcc.Dropdown(
        id='blood-type-dropdown',
        options=blood_type_options,
        value='All',
        clearable=False,
        style={'width': '200px'}
    )
    
    # Box Plot of Billing Amount by Age Group
    billing_boxplot = px.box(df, x='Age Group', y='Billing Amount', title="Billing Amount Distribution by Age Group")
    billing_boxplot.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    # Count of Admissions by Age Group
    admissions_count = px.histogram(df, x='Age Group', title="Count of Admissions by Age Group")
    admissions_count.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    return html.Div([
        html.H1("Age Analysis"),
        
        # Div to contain both dropdowns in one line
        html.Div([
            # Dropdown for selecting gender
            html.Div(gender_dropdown, style={'display': 'inline-block', 'margin-right': '10px'}),
            
            # Dropdown for selecting blood type
            html.Div(blood_type_dropdown, style={'display': 'inline-block'}),
        ], style={'text-align': 'center', 'margin-bottom': '20px'}),
        
        # Box Plot of Billing Amount by Age Group
        dcc.Graph(id='billing_boxplot', figure=billing_boxplot),
        
        # Count of Admissions by Age Group
        dcc.Graph(id='admissions_count', figure=admissions_count),
    ], style={'max-width': '800px', 'margin': 'auto', 'font-family': 'Arial, sans-serif'})

# Define callback to update visualizations based on dropdown selections for "Age Analysis" page
@app.callback(
    [Output('billing_boxplot', 'figure'),
     Output('admissions_count', 'figure')],
    [Input('gender-dropdown', 'value'),
     Input('blood-type-dropdown', 'value')]
)
def update_visualizations(selected_gender, selected_blood_type):
    filtered_df = df.copy()
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
    if selected_blood_type != 'All':
        filtered_df = filtered_df[filtered_df['Blood Type'] == selected_blood_type]
    
    # Box Plot of Billing Amount by Age Group
    billing_boxplot = px.box(filtered_df, x='Age Group', y='Billing Amount', title=f"Billing Amount Distribution by Age Group ({selected_gender}, {selected_blood_type})")
    billing_boxplot.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    # Count of Admissions by Age Group
    admissions_count = px.histogram(filtered_df, x='Age Group', title=f"Count of Admissions by Age Group ({selected_gender}, {selected_blood_type})")
    admissions_count.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    return billing_boxplot, admissions_count

# Define the layout for the "Insurance Provider Analysis" page
def insurance_provider_analysis_layout():
    
    # Dropdown for selecting gender
    gender_options = [{'label': 'All Genders', 'value': 'All'}] + [{'label': gender, 'value': gender} for gender in df['Gender'].unique()]
    gender_dropdown = dcc.Dropdown(
        id='gender-dropdown-provider',
        options=gender_options,
        value='All',
        clearable=False,
        style={'width': '200px'}
    )
    
    # Dropdown for selecting admission type
    admission_type_options = [{'label': 'All Admission Types', 'value': 'All'}] + [{'label': admission_type, 'value': admission_type} for admission_type in df['Admission Type'].unique()]
    admission_type_dropdown = dcc.Dropdown(
        id='admission-type-dropdown-provider',
        options=admission_type_options,
        value='All',
        clearable=False,
        style={'width': '200px'}
    )
    
    # Box Plot of Billing Amount by Insurance Provider
    billing_boxplot = px.box(df, x='Insurance Provider', y='Billing Amount', title="Billing Amount Distribution by Insurance Provider")
    billing_boxplot.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    # Count of Admissions by Insurance Provider
    admissions_count = px.histogram(df, x='Insurance Provider', title="Count of Admissions by Insurance Provider")
    admissions_count.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    return html.Div([
        html.H1("Insurance Provider Analysis"),
        
        # Div to contain both dropdowns in one line
        html.Div([
            # Dropdown for selecting gender
            html.Div(gender_dropdown, style={'display': 'inline-block', 'margin-right': '10px'}),
            
            # Dropdown for selecting admission type
            html.Div(admission_type_dropdown, style={'display': 'inline-block'}),
        ], style={'text-align': 'center', 'margin-bottom': '20px'}),
        
        # Box Plot of Billing Amount by Insurance Provider
        dcc.Graph(id='billing_boxplot_provider', figure=billing_boxplot),
        
        # Count of Admissions by Insurance Provider
        dcc.Graph(id='admissions_count_provider', figure=admissions_count),
    ], style={'max-width': '800px', 'margin': 'auto', 'font-family': 'Arial, sans-serif'})

# Define callback to update visualizations based on dropdown selections for "Insurance Provider Analysis" page
@app.callback(
    [Output('billing_boxplot_provider', 'figure'),
     Output('admissions_count_provider', 'figure')],
    [Input('gender-dropdown-provider', 'value'),
     Input('admission-type-dropdown-provider', 'value')]
)
def update_visualizations_provider(selected_gender, selected_admission_type):
    filtered_df = df.copy()
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
    if selected_admission_type != 'All':
        filtered_df = filtered_df[filtered_df['Admission Type'] == selected_admission_type]
    
    # Box Plot of Billing Amount by Insurance Provider
    billing_boxplot = px.box(filtered_df, x='Insurance Provider', y='Billing Amount', title=f"Billing Amount Distribution by Insurance Provider ({selected_gender}, {selected_admission_type})")
    billing_boxplot.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    # Count of Admissions by Insurance Provider
    admissions_count = px.histogram(filtered_df, x='Insurance Provider', title=f"Count of Admissions by Insurance Provider ({selected_gender}, {selected_admission_type})")
    admissions_count.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    return billing_boxplot, admissions_count

# Define the layout for the "Medical Condition Analysis" page
def medical_condition_analysis_layout():
    
    # Dropdown for selecting gender
    gender_options = [{'label': 'All Genders', 'value': 'All'}] + [{'label': gender, 'value': gender} for gender in df['Gender'].unique()]
    gender_dropdown = dcc.Dropdown(
        id='gender-dropdown-condition',
        options=gender_options,
        value='All',
        clearable=False,
        style={'width': '200px'}
    )
    
    # Dropdown for selecting insurance provider
    provider_options = [{'label': 'All Insurance Providers', 'value': 'All'}] + [{'label': provider, 'value': provider} for provider in df['Insurance Provider'].unique()]
    provider_dropdown = dcc.Dropdown(
        id='provider-dropdown',
        options=provider_options,
        value='All',
        clearable=False,
        style={'width': '200px'}
    )
    
    # Box Plot of Billing Amount by Medical Condition
    billing_boxplot = px.box(df, x='Medical Condition', y='Billing Amount', title="Billing Amount Distribution by Medical Condition")
    billing_boxplot.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    # Count of Admissions by Medical Condition
    admissions_count = px.histogram(df, x='Medical Condition', title="Count of Admissions by Medical Condition")
    admissions_count.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    return html.Div([
        html.H1("Medical Condition Analysis"),
        
        # Div to contain both dropdowns in one line
        html.Div([
            # Dropdown for selecting gender
            html.Div(gender_dropdown, style={'display': 'inline-block', 'margin-right': '10px'}),
            
            # Dropdown for selecting insurance provider
            html.Div(provider_dropdown, style={'display': 'inline-block'}),
        ], style={'text-align': 'center', 'margin-bottom': '20px'}),
        
        # Box Plot of Billing Amount by Medical Condition
        dcc.Graph(id='billing_boxplot_condition', figure=billing_boxplot),
        
        # Count of Admissions by Medical Condition
        dcc.Graph(id='admissions_count_condition', figure=admissions_count),
    ], style={'max-width': '800px', 'margin': 'auto', 'font-family': 'Arial, sans-serif'})

# Define callback to update visualizations based on dropdown selections for "Medical Condition Analysis" page
@app.callback(
    [Output('billing_boxplot_condition', 'figure'),
     Output('admissions_count_condition', 'figure')],
    [Input('gender-dropdown-condition', 'value'),
     Input('provider-dropdown', 'value')]
)
def update_visualizations_condition(selected_gender, selected_provider):
    filtered_df = df.copy()
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
    if selected_provider != 'All':
        filtered_df = filtered_df[filtered_df['Insurance Provider'] == selected_provider]
    
    # Box Plot of Billing Amount by Medical Condition
    billing_boxplot = px.box(filtered_df, x='Medical Condition', y='Billing Amount', title=f"Billing Amount Distribution by Medical Condition ({selected_gender}, {selected_provider})")
    billing_boxplot.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    # Count of Admissions by Medical Condition
    admissions_count = px.histogram(filtered_df, x='Medical Condition', title=f"Count of Admissions by Medical Condition ({selected_gender}, {selected_provider})")
    admissions_count.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    return billing_boxplot, admissions_count





# Define the layout for the "Medication Analysis" page
def medication_analysis_layout():
    
    # Dropdown for selecting gender
    gender_options = [{'label': 'All Genders', 'value': 'All'}] + [{'label': gender, 'value': gender} for gender in df['Gender'].unique()]
    gender_dropdown = dcc.Dropdown(
        id='gender-dropdown-medication',
        options=gender_options,
        value='All',
        clearable=False,
        style={'width': '200px'}
    )
    
    # Dropdown for selecting insurance provider
    provider_options = [{'label': 'All Insurance Providers', 'value': 'All'}] + [{'label': provider, 'value': provider} for provider in df['Insurance Provider'].unique()]
    provider_dropdown = dcc.Dropdown(
        id='provider-dropdown-medication',
        options=provider_options,
        value='All',
        clearable=False,
        style={'width': '200px'}
    )
    
    # Box Plot of Billing Amount by Medication
    billing_boxplot = px.box(df, x='Medication', y='Billing Amount', title="Billing Amount Distribution by Medication")
    billing_boxplot.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    # Count of Admissions by Medication
    admissions_count = px.histogram(df, x='Medication', title="Count of Admissions by Medication")
    admissions_count.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    return html.Div([
        html.H1("Medication Analysis"),
        
        # Div to contain both dropdowns in one line
        html.Div([
            # Dropdown for selecting gender
            html.Div(gender_dropdown, style={'display': 'inline-block', 'margin-right': '10px'}),
            
            # Dropdown for selecting insurance provider
            html.Div(provider_dropdown, style={'display': 'inline-block'}),
        ], style={'text-align': 'center', 'margin-bottom': '20px'}),
        
        # Box Plot of Billing Amount by Medication
        dcc.Graph(id='billing_boxplot_medication', figure=billing_boxplot),
        
        # Count of Admissions by Medication
        dcc.Graph(id='admissions_count_medication', figure=admissions_count),
    ], style={'max-width': '800px', 'margin': 'auto', 'font-family': 'Arial, sans-serif'})

# Define callback to update visualizations based on dropdown selections for "Medication Analysis" page
@app.callback(
    [Output('billing_boxplot_medication', 'figure'),
     Output('admissions_count_medication', 'figure')],
    [Input('gender-dropdown-medication', 'value'),
     Input('provider-dropdown-medication', 'value')]
)
def update_visualizations_medication(selected_gender, selected_provider):
    filtered_df = df.copy()
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]
    if selected_provider != 'All':
        filtered_df = filtered_df[filtered_df['Insurance Provider'] == selected_provider]
    
    # Box Plot of Billing Amount by Medication
    billing_boxplot = px.box(filtered_df, x='Medication', y='Billing Amount', title=f"Billing Amount Distribution by Medication ({selected_gender}, {selected_provider})")
    billing_boxplot.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    # Count of Admissions by Medication
    admissions_count = px.histogram(filtered_df, x='Medication', title=f"Count of Admissions by Medication ({selected_gender}, {selected_provider})")
    admissions_count.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False
    )
    
    return billing_boxplot, admissions_count







# Define the layout for the "Home" page
def home_layout():
    return html.Div(
        className="home-page",
        style={
            'display': 'flex',
            'justify-content': 'center',
            'align-items': 'center',
            'height': '100vh'
        },
        children=[
            html.Div(
                className="home-content",
                style={'text-align': 'center'},
                children=[
                    html.H1("Healthcare Analytics Dashboard", style={'font-size': '2.5rem', 'margin-bottom': '20px'}),
                    html.P("Explore different aspects of healthcare data analysis using this interactive dashboard.", style={'font-size': '1.2rem', 'margin-bottom': '40px'}),
                    html.Div(
                        className="home-links",
                        style={'display': 'flex', 'justify-content': 'center'},
                        children=[
                            html.Div(
                                html.A('Age Analysis', href='/age_analysis', style={'padding': '10px 20px', 'background-color': '#007BFF', 'color': '#fff', 'text-decoration': 'none', 'border-radius': '5px', 'transition': 'background-color 0.3s ease'}),
                                style={'margin-right': '20px'}
                            ),
                            html.Div(
                                html.A('Insurance Provider Analysis', href='/insurance_provider_analysis', style={'padding': '10px 20px', 'background-color': '#007BFF', 'color': '#fff', 'text-decoration': 'none', 'border-radius': '5px', 'transition': 'background-color 0.3s ease'}),
                                style={'margin-right': '20px'}
                            ),
                            html.Div(
                                html.A('Medical Condition Analysis', href='/medical_condition_analysis', style={'padding': '10px 20px', 'background-color': '#007BFF', 'color': '#fff', 'text-decoration': 'none', 'border-radius': '5px', 'transition': 'background-color 0.3s ease'}),
                                style={'margin-right': '20px'}
                            ),
                            html.Div(
                                html.A('Medication Analysis', href='/medication_analysis', style={'padding': '10px 20px', 'background-color': '#007BFF', 'color': '#fff', 'text-decoration': 'none', 'border-radius': '5px', 'transition': 'background-color 0.3s ease'}),
                            )
                        ]
                    )
                ]
            )
        ]
    )



# Define callback to display the appropriate analysis page based on URL pathname
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/age_analysis':
        return age_analysis_layout()
    elif pathname == '/insurance_provider_analysis':
        return insurance_provider_analysis_layout()
    elif pathname == '/medical_condition_analysis':
        return medical_condition_analysis_layout()
    elif pathname == '/medication_analysis':
        return medication_analysis_layout()
    else:
        return home_layout()

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
