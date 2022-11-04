import pandas as pd

def update_column(raw_file_path):
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
          # .drop(['Date1', 'dif_p', 'rfm','rfy','Month'], axis=1)
          # .dropna(axis=0)   
         )