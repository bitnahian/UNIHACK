import pandas as pd

df = pd.read_csv('../data/cleaned_data.csv')

df_speed = df.loc[df['SPEED_IND'] == 'Y']
df_red = df.loc[df['RED_LIGHT_CAMERA_IND'] == 'Y']

df_speed = df_speed[['LOCATION_CODE', 'LOCATION_DETAILS', 'CAMERA_TYPE',
    'SCHOOL_ZONE_IND', 'SPEED_IND']]
df_red = df_red[['LOCATION_CODE', 'LOCATION_DETAILS', 'CAMERA_TYPE',
    'SCHOOL_ZONE_IND', 'RED_LIGHT_CAMERA_IND']]

df_speed_counts = df_speed["LOCATION_CODE"].value_counts()
df_red_counts = df_red["LOCATION_CODE"].value_counts()

df_speed = df_speed.groupby('LOCATION_CODE').agg({'CAMERA_TYPE':'first','LOCATION_DETAILS':'first', 'SCHOOL_ZONE_IND':'first', 'SPEED_IND':'first'}).reset_index()

df_red = df_red.groupby('LOCATION_CODE').agg({'CAMERA_TYPE':'first','LOCATION_DETAILS':'first','SCHOOL_ZONE_IND':'first', 'RED_LIGHT_CAMERA_IND':'first'}).reset_index()

df_speed_counts = df_speed_counts.to_frame().reset_index(level=0,inplace=True)
df_red_counts = df_red_counts.to_frame().reset_index(level=0,inplace=True)

df_speed_counts.columns=['LOCATION_CODE', 'COUNT']
df_red_counts.columns=['LOCATION_CODE', 'COUNT']

df_speed_final = pd.merge(df_speed, df_speed_counts, how='inner', on='LOCATION_CODE')
df_red_final = pd.merge(df_red, df_red_counts, how='inner', on='LOCATION_CODE')

