import pandas as pd
import project_functions1 as pf1

def load_and_process(raw_file_path):
    """
    Returns the processed data for analysis file 2 given raw data path.
    
    Returns a cleaned dataframe eliminating unused columns, and grouping those columns by month. It then returns the mean of the values in those columns before creating new columns with those averages.
    
    Parameters
    ----------
    raw_file_path : the path to the raw_file_path
        string
        
    Returns
    -------
    df_column_update
        The processed dataframe object.
    
    Examples
    --------
    >>> load_and_process('../data/raw/climate_data.csv')
    avg_win	avg_gus	avg_dir	rfm	Month	aag	aaw	aar	aad
    0	26.4	36.8	274.0	0.0	1	12.121138	8.186992	0.087669	243.075881
    1	12.8	18.0	240.0	0.0	1	12.121138	8.186992	0.087669	243.075881
    2	8.3	12.2	290.0	0.0	1	12.121138	8.186992	0.087669	243.075881
    """
#     loads the dataset using a sharedmethod and discards unneeded columns.
    df_column_update = (pf1.update_column(raw_file_path)
                        .drop(['Date','avg_tem','avg_hum','avg_dew','avg_bar','rfy','max_hum','min_hum','max_pre','min_pre','max_win','max_gus','max_hea','Date1','dif_p','max_rai','max_tem','min_tem'], axis=1)
                       )
    
    month_average = (df_column_update
                .groupby(by='Month')
                .mean()
                     )    
    
    df_column_update[['aag','aaw','aar','aad']] = (df_column_update.
                                                   apply(lambda x: month_average.iloc[int(x.Month)-1][['avg_gus','avg_win','rfm','avg_dir']], axis=1))
    
    return df_column_update
