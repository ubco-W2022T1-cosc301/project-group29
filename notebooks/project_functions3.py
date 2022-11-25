
## ALl the functions except 'clear_data' should be use with cleared data not raw data!!

def clear_data(raw_file_path):
    
    '''
    Return a dataframe with only temperature ,humimdity , year, month and day.
    
    Parameters
    ----------
    raw_file_path : the path to the raw_file_path.
        string
        
    Returns
    -------
    dataframe
        a dataframe with only necessary data. 
        
    Examples
    --------
    >>> clear_data('../data/raw/climate_data.csv')
        Date	avg_tem	avg_hum	max_tem	min_tem	max_hum	min_hum	max_hea	Month	Day	Year
    0	2009-01-01	37.8	35.0	40.0	34.0	4.0	27.0	40.0	1	1	2009
    1	2009-01-02	43.2	32.0	52.0	37.0	4.0	16.0	52.0	1	2	2009
    2	2009-01-03	25.7	60.0	41.0	6.0	8.0	35.0	41.0	1	3	2009
    3	2009-01-04	9.3	67.0	19.0	-0.0	7.0	35.0	32.0	1	4	2009
    
    '''
    import pandas as pd 
    import project_functions1 as pf1
    
    df = pf1.update_column(raw_file_path)
    
    df['date_obj'] = df.apply(lambda x: pd.to_datetime(x.Date).date(), axis=1)
    df['Day'] = df.apply(lambda x: x.date_obj.day,axis=1)
    df['Year'] = df.apply(lambda x: x.date_obj.year,axis=1)

    df_cleared = (df.drop(['avg_dew', 'avg_bar', 'avg_win', 'avg_gus', 'avg_dir', 'rfm', 'rfy', 'max_rai', 'max_pre', 'min_pre', 'max_win', 'max_gus', 'dif_p', 'Date1', 'date_obj'], axis=1))
    
    return df_cleared


## Filter data by date ##


def filter_1month(dataframe, year, month):
    
    '''
    Return a dataframe with data within the inputed year.
    
    Parameters
    ----------
    dataframe : a cleared dataframe will obly necessary data.
        dataframe
        
    year : the year data will from.
        integer
    
    month : the year data will from.
        
    Returns
    -------
    dataframe
        with data within the inputed year. 
        
    Examples
    --------
    >>> filter_1year(df, 2010, 1)
            Date	avg_tem	avg_hum	max_tem	min_tem	max_hum	min_hum	max_hea	Month	Day	Year
    0	2010-01-01	32.1	49.0	40.0	22.1	61.0	41.0	40.0	1	1	2010
    1	2010-01-02	32.1	50.0	39.1	22.0	77.0	39.0	39.1	1	2	2010
    2	2010-01-03	23.1	64.0	33.4	9.2	85.0	34.0	33.4	1	3	2010
    3	2010-01-04	25.7	48.0	36.5	7.6	82.0	25.0	36.5	1	4	2010
    
    '''
    
    filtered = dataframe[(dataframe['Year'] == year) & (dataframe['Month'] == month)]
    filtered = filtered.reset_index()
    filtered = filtered.drop(['index'], axis=1)
    
    return filtered


def filter_1year(dataframe, year):
    
    '''
    Return a dataframe with data within the inputed year.
    
    Parameters
    ----------
    dataframe : a cleared dataframe will obly necessary data.
        dataframe
        
    year : the year data will from.
        integer
        
    Returns
    -------
    dataframe
        with data within the inputed year. 
        
    Examples
    --------
    >>> filter_1year(df, 2010)
        Date	avg_tem	avg_hum	max_tem	min_tem	max_hum	min_hum	max_hea	Month	Day	Year
    0	2010-01-01	32.1	49.0	40.0	22.1	61.0	41.0	40.0	1	1	2010
    1	2010-01-02	32.1	50.0	39.1	22.0	77.0	39.0	39.1	1	2	2010
    2	2010-01-03	23.1	64.0	33.4	9.2	85.0	34.0	33.4	1	3	2010
    3	2010-01-04	25.7	48.0	36.5	7.6	82.0	25.0	36.5	1	4	2010

    '''
    
    filtered = dataframe[dataframe['Year'] == year]
    filtered = filtered.reset_index()
    filtered = filtered.drop(['index'], axis=1)
    
    return filtered


def filter_years(dataframe, year1, year2):
    
    '''
    Return a dataframe with data between the inputed years.
    
    Parameters
    ----------
    dataframe : a cleared dataframe will obly necessary data.
        dataframe
        
    year1 : the year data starts.
        integer
        
    year2 : the year data ends.
        integer
        
    Returns
    -------
    dataframe
        with data between the year1 and year2. 
        
    Examples
    --------
    >>> filter_years(df, 2010, 2012)
        Date	avg_tem	avg_hum	max_tem	min_tem	max_hum	min_hum	max_hea	Month	Day	Year
    0	2010-01-01	32.1	49.0	40.0	22.1	61.0	41.0	40.0	1	1	2010
    1	2010-01-02	32.1	50.0	39.1	22.0	77.0	39.0	39.1	1	2	2010
    2	2010-01-03	23.1	64.0	33.4	9.2	85.0	34.0	33.4	1	3	2010
    ...
    945	2012-12-29	17.1	36.0	36.8	-0.2	59.0	19.0	36.8	12	29	2012
    946	2012-12-30	27.6	31.0	37.6	16.7	63.0	16.0	37.6	12	30	2012
    947	2012-12-31	12.5	73.0	23.5	1.1	81.0	61.0	23.5	12	31	2012
    
    '''
        
    filtered = dataframe[(dataframe['Year'] >= year1) & (dataframe['Year'] <= (year2))]
    filtered = filtered.reset_index()
    filtered = filtered.drop(['index'], axis=1)
    
    return filtered


## Average temperature ##


def filter_avg_temp_monthly(dataframe, year, month):
    
    '''
    Return a dataframe with average temperature within the month.
    
    Parameters
    ----------
    dataframe : a cleared dataframe will obly necessary data.
        dataframe
        
    year : the year data will from.
        integer
        
    month : the month the data will be.
        integer
        
    Returns
    -------
    dataframe
        Show daily average temperature monthly within the inputed year and month. 
        
    Examples
    --------
    >>> filter_avg_temp_monthly(df, 2010, 1)
        Day	avg_tem
    0	1	32.1
    1	2	32.1
    2	3	23.1
    3	4	25.7

    '''
    import project_functions3 as pf3
    
    dataframe = pf3.filter_1month(dataframe, year, month)
    
    filtered = dataframe[['avg_tem', 'Day']]
    filtered = filtered.groupby(['Day']).mean()
    filtered = filtered.reset_index()
    
    return filtered


def filter_avg_temp_yearly(dataframe, year1, year2):
    
    '''
    Return a dataframe with average temperature of each month.

    Parameters
    ----------
    dataframe : a cleared dataframe will obly necessary data.
        dataframe
        
    year1 : the year data will from.
        integer
        
    year2 : the year data ends.
        integer
        
    Returns
    -------
    dataframe
        Show monthly average temperature within the inputed years. 
        
    Examples
    --------
    >>> filter_avg_temp_yearly(df, 2010, 2012)
        Year	Month	avg_tem
    0	2010	1	28.319355
    1	2010	2	23.742857
    2	2010	3	33.793548
    ...
    32	2012	10	44.470968
    33	2012	11	41.310000
    34	2012	12	28.116129

    >>> filter_avg_temp_yearly(df, 2010, 2010)
        Year	Month	avg_tem
    0	2010	1	28.319355
    1	2010	2	23.742857
    2	2010	3	33.793548
    
    '''
    
    import project_functions3 as pf3
    
    if(year1 == year2):
        
        dataframe = pf3.filter_1year(dataframe, year1)
    
        filtered = dataframe[['avg_tem', 'Month', 'Year']]
        filtered = filtered.groupby(['Year', 'Month']).mean()
        filtered = filtered.reset_index()
        
    else:
        
        dataframe = pf3.filter_years(dataframe, year1, year2)
    
        filtered = dataframe[['avg_tem', 'Month', 'Year']]
        filtered = filtered.groupby(['Year', 'Month']).mean()
        filtered = filtered.reset_index()
    
    return filtered


## Average humidity ##


def filter_avg_humi_monthly(dataframe, year, month):
    
    '''
    Return a dataframe with average humidity within the month.
    
    Parameters
    ----------
    dataframe : a cleared dataframe will obly necessary data.
        dataframe
        
    year : the year data will from.
        integer
        
    month : the month data will from.
        
    Returns
    -------
    dataframe
        Show daily average humidity monthly within the inputed year and month. 
        
    Examples
    --------
    >>> filter_avg_humi_monthly(df, 2010, 1)
        Day	avg_hum
    0	1	49.0
    1	2	50.0
    2	3	64.0
    3	4	48.0

    '''
    import project_functions3 as pf3
    
    dataframe = pf3.filter_1month(dataframe, year, month)
    
    filtered = dataframe[['avg_hum', 'Day']]
    filtered = filtered.groupby(['Day']).mean()
    filtered = filtered.reset_index()
    
    return filtered


def filter_avg_humi_yearly(dataframe, year1, year2):
    
    '''
    Return a dataframe with average temperature of each month.
    
    Parameters
    ----------
    dataframe : a cleared dataframe will obly necessary data.
        dataframe
        
    year : the year data will from.
        integer
        
    Returns
    -------
    dataframe
        Show monthly average humidity within the inputed years. 
        
    Examples
    --------
    >>> filter_avg_temp_yearly(df, 2010, 2013)
        Year	Month	avg_tem
    0	2010	1	28.319355
    1	2010	2	23.742857
    2	2010	3	33.793548
    ...
    10	11	33.810000
    11	12	31.276667

    >>> filter_avg_humi_yearly(df, 2010, 2010)
        Month	avg_tem
    0	1	28.319355
    1	2	23.742857
    2	3	33.793548
    ...
    10	11	33.810000
    11	12	31.276667
    '''
    
    import project_functions3 as pf3
    
    if(year1 == year2):
        
        dataframe = pf3.filter_1year(dataframe, year1)
    
        filtered = dataframe[['avg_hum', 'Month', 'Year']]
        filtered = filtered.groupby(['Year', 'Month']).mean()
        filtered = filtered.reset_index()
        
    else:
        
        dataframe = pf3.filter_years(dataframe, year1, year2)
    
        filtered = dataframe[['avg_hum', 'Month', 'Year']]
        filtered = filtered.groupby(['Year', 'Month']).mean()
        filtered = filtered.reset_index()
    
    return filtered


# Combin average temperature and humidity data


def combin_m(df_temp, df_humi):
    
    '''
    Return a dataframe with daily average temperature and humidity within a month.
    
    Parameters
    ----------
    df_temp : a filtered dataframe with average temperature within a month.
        dataframe
        
    df_humi : a filtered dataframe with average humidity within a month.
        dataframe
        
    Returns
    -------
    dataframe
        Show daily average temperature and humidity within a month.
        
    Examples
    --------
    >>> combin_m(df_201001_temp, df_201001_humi)
        Day	Count	Type
    0	1	32	avg_tem
    1	2	32	avg_tem
    2	3	23	avg_tem
    ...
    60	30	63	avg_hum
    61	31	53	avg_hum
    
    '''

    import pandas as pd 
    import project_functions3 as pf3
    
    df_temp['Type'] = 'avg_tem'
    df_humi['Type'] = 'avg_hum'
    
    df_combin = pd.concat([df_temp, df_humi], ignore_index=True)
    df_combin.rename(columns = {'avg_tem':'Count', 'avg_hum':'Count1'}, inplace = True)
    
    df_combin['Data'] = df_combin['Count'].combine_first(df_combin['Count1']).astype(int)
    df_combin = df_combin[['Day', 'Data', 'Type']]
    
    return df_combin


def combin_y(df_temp, df_humi):
    
    '''
    Return a dataframe with monthly average temperature and humidity within a year.
    
    Parameters
    ----------
    df_temp : a filtered dataframe with average temperature within a month.
        dataframe
        
    df_humi : a filtered dataframe with average humidity within a month.
        dataframe
        
    Returns
    -------
    dataframe
        Show monthly average temperature and humidity within a year.
        
    Examples
    --------
    >>> combin_y(df_201001_temp, df_201001_humi)
        Day	Count	Type
    0	1	32	avg_tem
    1	2	32	avg_tem
    2	3	23	avg_tem
    ...
    60	30	63	avg_hum
    61	31	53	avg_hum
    
    '''

    import pandas as pd 
    import project_functions3 as pf3
    
    df_temp['Type'] = 'avg_tem'
    df_humi['Type'] = 'avg_hum'
    
    df_combin = pd.concat([df_temp, df_humi], ignore_index=True)
    df_combin.rename(columns = {'avg_tem':'Count', 'avg_hum':'Count1'}, inplace = True)
    
    df_combin['Data'] = df_combin['Count'].combine_first(df_combin['Count1']).astype(int)
    df_combin = df_combin[['Year', 'Month', 'Data', 'Type']]
    
    return df_combin

    
