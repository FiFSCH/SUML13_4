#-------------------------------------------------------------------------------------------------#
#                                             IMPORTS                                             #
#-------------------------------------------------------------------------------------------------#

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

import pickle
import streamlit as st

#-------------------------------------------------------------------------------------------------#
#                                            CONSTANTS                                            #
#-------------------------------------------------------------------------------------------------# 

# Load initial ML model
LOADED_MODEL = pickle.load(open('./suml_04_12_2023.pkl', 'rb'))

# Load original CSV dataset and create copy
DATASET = pd.read_csv('./Spotify-2000.csv')

df_copy = DATASET.drop('Index', axis=1, errors='ignore')


# Create new dataset with selected audio features
df_2 = df_copy[["Beats Per Minute (BPM)", "Loudness (dB)",
              "Liveness", "Valence", "Acousticness",
              "Speechiness"]]

# Scale features to range for clustering
for i in df_copy.columns:
    MinMaxScaler(i)

#-------------------------------------------------------------------------------------------------#
#                                             METHODS                                             #
#-------------------------------------------------------------------------------------------------# 

def format_year(x):
    return "{:.0f}".format(x)

def kmeans_clustering(input_data):

    # Create a new DataFrame with user input data
    new_row = pd.DataFrame([input_data], columns=df_2.columns)

    # Append new row to existing data
    df_3 = pd.concat([df_2, new_row], ignore_index=True)

    # Fit new data to loaded model
    new_clusters = LOADED_MODEL.fit_predict(df_3)

    return df_3, new_clusters

def browse_songs():

    # Display selected columns in a scrollable panel format
    with st.container():
        st.title("Spotify's Top 2000 Songs")

        # Apply formatting to the 'Year' column
        df_copy_styled = df_copy.style.format({'Year': format_year})

        st.dataframe(data=df_copy_styled, width=712)

def clustering_analysis(input_data):

    # Declare analysis variable
    clusters = ''
    
    # Clustering analysis
    if st.button("Get Result"):
        
        df_3 = kmeans_clustering(input_data)[0]
        clusters = kmeans_clustering(input_data)[1]
      
        # Add predicted clusters to new dataset
        df_3["Music Segments"] = clusters
        MinMaxScaler(df_3["Music Segments"])

        df_3["Music Segments"] = df_3["Music Segments"].map({1: "Cluster 1", 2:
            "Cluster 2", 3: "Cluster 3", 4: "Cluster 4", 5: "Cluster 5",
            6: "Cluster 6", 7: "Cluster 7", 8: "Cluster 8",
            9: "Cluster 9", 10: "Cluster 10"})  

        # Get cluster of input data
        rows = len(df_copy)
        new_row_cluster = df_3.loc[rows, "Music Segments"]

        # Get rows in the same cluster
        rows_with_cluster = df_3[df_3["Music Segments"] == new_row_cluster].index
        rows_2 = len(rows_with_cluster) - 1
        selected_rows = df_copy.iloc[rows_with_cluster[:rows_2], [0, 1, 2, 3]]

        # Display results in a scrollable panel format
        with st.container():
            st.title("Clustering Analysis Result")

            # Apply formatting to the 'Year' column
            selected_rows_styled = selected_rows.style.format({'Year': format_year})

            st.dataframe(data=selected_rows_styled, width=712)

        st.success(f"Music genre clustering analysis complete.\nNumber of results: {len(selected_rows.index)}")

#-------------------------------------------------------------------------------------------------#
#                                           MAIN METHOD                                           #
#-------------------------------------------------------------------------------------------------# 

def main():

    # Web app title
    st.title("Music Genre Analysis Web Application")

    # Menu selection
    menu_option = st.radio("Select an option:", ["Browse Available Songs", "Music Genre Clustering Analysis"])

    # Browse songs and features
    if menu_option == "Browse Available Songs":
        browse_songs()

    # Clustering analysis by features
    elif menu_option == "Music Genre Clustering Analysis":
        # Input data from user
        BPM = st.slider('Beats per minute (BPM)', 37, 206, 121, 1, help="Tempo of a song. It indicates the number of beats (rhythmic pulses) within a minute.")
        Loudness = st.slider('Loudness (DB)', -60, 0, -30, 1, help="The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track.")
        Liveness = st.slider('Liveness', 0, 100, 50, 1, help="Higher liveness values represent an increased probability that the track was performed live.")
        Valence = st.slider('Valence', 0.0, 1.0, 0.5, 0.01, help="Describes the musical positiveness conveyed by a track. Tracks with high valence sound more positive.")
        Acousticness = st.slider('Acousticness', 0, 100, 50, 1, help="Higher acousticness values represent an increased probability that the track was made with acoustic instruments and natural sounds.")
        Speechiness = st.slider('Speechiness', 0, 100, 50, 1, help="Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording, the closer to 1.0 the attribute value.")

        input_data = [BPM, Loudness, Liveness, Valence, Acousticness, Speechiness]

        clustering_analysis(input_data)

if __name__ == '__main__':
    main()