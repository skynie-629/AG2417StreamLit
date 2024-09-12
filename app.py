import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Generate random geospatial data
data = pd.DataFrame({
    'lat': np.random.uniform(37.7, 37.8, 100),
    'lon': np.random.uniform(-122.5, -122.4, 100),
})

st.title('Geospatial Data Visualization')

# Display the map
st.map(data)

# Use pydeck for more advanced visualization
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=37.75,
        longitude=-122.45,
        zoom=12,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
          'HexagonLayer',
          data=data,
          get_position='[lon, lat]',
          radius=100,
          elevation_scale=4,
          elevation_range=[0, 1000],
          pickable=True,
          extruded=True,
        ),
    ],
))
