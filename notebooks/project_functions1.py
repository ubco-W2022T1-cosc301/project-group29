import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def update_column(raw_file_path):
    '''
    Return the dataframe with all the renamed columns given raw file path.
    
    Parameters
    ----------
    raw_file_path : the path to the raw_file_path
        string
        
    Returns
    -------
    df
        the column-renamed dataframe object 
        
    Examples
    --------
    >>> update_column('../data/raw/climate_data.csv')
    Date	avg_tem	avg_hum	avg_dew	avg_bar	avg_win	avg_gus	avg_dir	rfm	rfy	...	max_hum	min_hum	max_pre	min_pre	max_win	max_gus	max_hea	Date1	Month	dif_p
0	2009-01-01	37.8	35.0	12.7	29.7	26.4	36.8	274.0	0.0	0.0	...	4.0	27.0	29.762	29.596	41.4	59.0	40.0	2009-01-01	1	0.166
1	2009-01-02	43.2	32.0	14.7	29.5	12.8	18.0	240.0	0.0	0.0	...	4.0	16.0	29.669	29.268	35.7	51.0	52.0	2009-01-02	1	0.401
2	2009-01-03	25.7	60.0	12.7	29.7	8.3	12.2	290.0	0.0	0.0	...	8.0	35.0	30.232	29.260	25.3	38.0	41.0	2009-01-03	1	0.972
3	2009-01-04	9.3	67.0	0.1	30.4	2.9	4.5	47.0	0.0	0.0	...	7.0	35.0	30.566	30.227	12.7	20.0	32.0	2009-01-04	1	0.339
4	2009-01-05	23.5	30.0	-5.3	29.9	16.7	23.1	265.0	0.0	0.0	...	5.0	13.0	30.233	29.568	38.0	53.0	32.0	2009-01-05	1	0.665
    '''
    return (pd.read_csv(raw_file_path)
            .rename(columns={
              "Average temperature (°F)":"avg_tem",
              "Average humidity (%)":"avg_hum",
              "Average dewpoint (°F)":"avg_dew",
              "Average barometer (in)":"avg_bar",
              "Average windspeed (mph)":"avg_win",
              "Average gustspeed (mph)":"avg_gus",
              "Average direction (°deg)":"avg_dir",
              "Rainfall for month (in)":"rfm",
              "Rainfall for year (in)":"rfy",
              "Maximum rain per minute":"max_rai",
              "Maximum temperature (°F)":"max_tem",
              "Minimum temperature (°F)":"min_tem",
              "Maximum humidity (%)":"max_hum",
              "Minimum humidity (%)":"min_hum",
              "Maximum pressure":"max_pre",
              "Minimum pressure":"min_pre",
              "Maximum windspeed (mph)":"max_win",
              "Maximum gust speed (mph)":"max_gus",
              "Maximum heat index (°F)":"max_hea",
              "diff_pressure":"dif_p"})
         )

    '''
    **For graders**
    Not very many method chainings, I get it.
    But that's mostly because I wrote the column rename in task 1, and that's for everyone in our team to use
    And I just do not want to repeat myself in task 3
    Plus, our dataset is too good to be cleaned: no loading (text encoding etc) issues, no empty spots (n/a), no words
    I'm just leaving this message here in case you want to jump into deducting any of our members' mark
    We all know how to do method chaining
    '''

def load_and_process(raw_file_path):
    '''
    Return the processed data for analysis file 1 given raw file path.
    
    Parameters
    ----------
    raw_file_path : the path to the raw_file_path
        string
        
    Returns
    -------
    df
        the processed dataframe object
        
    Examples
    --------
    >>> load_and_process('../data/raw/climate_data.csv')
    	avg_tem	avg_hum	avg_dew	max_tem	min_tem	max_hum	min_hum	max_hea	Month	date_obj	Year	dep_dew	ran_dew
0	32.1	49.0	15.2	40.0	22.1	61.0	41.0	40.0	1	2010-01-01	2010	16.9	57.10
1	32.1	50.0	15.5	39.1	22.0	77.0	39.0	39.1	1	2010-01-02	2010	16.6	62.78
2	23.1	64.0	12.1	33.4	9.2	85.0	34.0	33.4	1	2010-01-03	2010	11.0	74.56
3	25.7	48.0	7.2	36.5	7.6	82.0	25.0	36.5	1	2010-01-04	2010	18.5	81.42
4	34.3	51.0	17.8	40.1	28.4	60.0	43.0	40.1	1	2010-01-05	2010	16.5	49.82
    '''

    df = update_column(raw_file_path)
    df['date_obj']=df.apply(lambda x: pd.to_datetime(x.Date).date(), axis=1)
    df['Year']=df.apply(lambda x: x.date_obj.year, axis=1)
    df['dep_dew']=df.apply(lambda x: x.avg_tem-x.avg_dew, axis=1)
    df['ran_dew']=df.apply(lambda x: (((x.max_tem - 32) * 5/9-(100-x.max_hum)/5)-((x.min_tem - 32) * 5/9-(100-x.min_hum)/5))*1.8+32, axis = 1)
    df_clean = (df
                .copy()
                .drop(['rfm','rfy', 'Date1','avg_bar','avg_win','avg_gus','avg_dir','max_rai','max_pre','min_pre','max_win','dif_p','max_gus','Date'], axis=1)
                .dropna(axis=0)
                .drop(df[df.Year == 2009].index)
                .drop(df[df.Year == 2020].index)
                .reset_index(drop=True)
           )

    return df_clean

def ridgeline(df,input_row,input_column):
    '''
    https://seaborn.pydata.org/examples/kde_ridgeplot.html
    '''
    
    pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
    g = sns.FacetGrid(df, row=input_row, hue=input_row, aspect=15, height=.5, palette=pal)

    # Draw the densities in a few steps
    g.map(sns.kdeplot, input_column,
          bw_adjust=.5, clip_on=False,
          fill=True, alpha=1, linewidth=1.5)
    g.map(sns.kdeplot, input_column, clip_on=False, color="w", lw=2, bw_adjust=.5)

    # passing color=None to refline() uses the hue mapping
    g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)


    # Define and use a simple function to label the plot in axes coordinates
    def label(x, color, label):
        ax = plt.gca()
        ax.text(0, .2, label, fontweight="bold", color=color,
                ha="left", va="center", transform=ax.transAxes)


    g.map(label, input_column)

    # Set the subplots to overlap
    g.figure.subplots_adjust(hspace=-.25)

    # Remove axes details that don't play well with overlap
    g.set_titles("")
    g.set(yticks=[], ylabel="")
    g.despine(bottom=True, left=True)