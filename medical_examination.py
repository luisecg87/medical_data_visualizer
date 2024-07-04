import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process_data(file_path):
    df = pd.read_csv(file_path)

    # Add 'overweight' column
    df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

    # Normalize data by making 0 always good and 1 always bad
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    # Clean the data
    df = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    return df

def draw_cat_plot(df):
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    fig = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar'
    ).fig

    fig.savefig('catplot.png')
    return fig

def draw_heat_map(df):
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, vmax=0.3, linewidths=0.5, cbar_kws={"shrink": 0.5})

    fig.savefig('heatmap.png')
    return fig
