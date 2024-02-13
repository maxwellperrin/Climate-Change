import pandas as pd
import streamlit as st
import numpy as np 
import plotly as plt
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import plotly.express as px
import streamlit_folium
import folium
from streamlit_folium import folium_static



st.header('',divider='rainbow')
texte_a_centrer = "Welcome on Feel-Freedom: an independent newspaper"

st.markdown(
    f"<div style='text-align: center;'><h1>{texte_a_centrer}</h1></div>",
    unsafe_allow_html=True
)
st.header('',divider='rainbow')
st.write("")

st.header("")
st.write("")
texte_a_centrer = "Global Warming"

st.markdown(
    f"<div style='text-align: center;'><h1>{texte_a_centrer}</h1></div>",
    unsafe_allow_html=True)


sea_level = pd.read_csv(r"sea_level.csv")
sea_temperature = pd.read_csv(r"sea_temperature.csv")
ocean_carbon = pd.read_csv(r"ocean_carbon.csv")
ArticSeaExtent = pd.read_csv(r"ArticSeaExtent.csv")
AntarticSeaExtent = pd.read_csv(r"AntarticSeaExtent.csv")
annual_greenhouse_gas_index = pd.read_csv(r'annual_greenhouse_gas_index')
agriculture_co2 = pd.read_csv(r'agriculture_co2.csv')
bunkerfuels_co2 = pd.read_csv(r'bunkerfuels_co2.csv')


fig = px.line(sea_level, x="year", y="values", labels={"values": "Sea Level (m)"},
              title="Global Mean Sea Level (m) per Year")


fig.update_layout(xaxis_title="Year", yaxis_title="Sea Level (m)", xaxis=dict(tickmode="linear", tick0=2010, dtick=1))


st.plotly_chart(fig)

st.write("Sea Level Measuring changes in absolute sea level due to ocean thermal expansion, land ice loss and terrestrial water storage changes")
st.write("")
st.write("Over 1993-2022, the global mean sea level rose on average by 3.3 ± 0.3 mm per year. A total of 9.57 cm over this period. The rate of increase is accelerating.")
st.write("The impact :")
st.write(":rainbow[Damage to people and infrastructure:] increased probability of flooding, aggravates coastal erosion, leading to population displacement, property damage, and loss of critical services.")
st.write(":rainbow[Damage to coastal habitats:] destruction of coastal habitats (dunes, coral reefs, wetlands) caused by erosion and saltwater intrusion.")
st.write(":rainbow[Higher risk of storm damage:] natural protection offered by coastal habitats is weakened, leading to higher impact of storms at the coast.")
st.write(":rainbow[More extreme sea levels:] extreme sea level events will happen more frequently due to sea levels rise and also due to weaker protection from coastal habitats")
st.write(":rainbow[Salinisation:] Saltwater intrusion in freshwater sources like estuaries, groundwater, aquifers and surface waters affects freshwater availability and agricultural land.")

####################################################################################################################

####################################################################################################################

st.title("Global Mean Sea Surface Temperature (°C) per Year")


fig, ax = plt.subplots(figsize=(20, 5))
sns.lineplot(data=sea_temperature, x="year", y="values", ax=ax)


ax.set_title("Global Mean Sea Surface Temperature (°C) per Year")
ax.set_ylabel("Sea Surface Temperature Anomalies (°C)")
ax.set_xlabel("Year")


ax.axhline(y=0, color='red', linestyle='--', label='Zero Anomaly')


st.pyplot(fig)

st.write("1993-2021 : Sea surface temperatures have increased globally on average by more than 0.4 (± 0.02) °C since 1993, a trend that is expected to continue. Shallower and (semi-) enclosed seas have warmed more than the global average.")
st.write("")
st.write("The impact:")
st.write(":rainbow[Ocean warming:] since the ocean takes centuries to millennia to respond to changes, irreversible ocean warming, and its associated sea level rise, is considered inevitable.")
st.write(":rainbow[Ocean circulation:] ocean warming can potentially impact the meridional overturning circulation (MOC), and upwelling processes.")
st.write(":rainbow[Decreased marine biodiversity:] migration of species, mass die-off events, invasive species, and degradation of ecosystems.")
st.write(":rainbow[Disruption of marine food systems:] marine food chains rely on phytoplankton, organisms living near the sea surface.")
st.write(":rainbow[Ocean stratification:] prevents ocean layers from mixing and distributing the nutrients.")
st.write(":rainbow[Threatened food security and loss of livelihood:] ecosystem damage, combined with biodiversity loss, leads to less fish catch")
st.write(":rainbow[Weather patterns and severe events:] warmer ocean temperatures can impact precipitation distribution and storm intensity.")
st.write(":rainbow[Sea ice melting:] combined sea and sea-ice surface temperatures cause melting.")

######################################################################################################################
######################################################################################################################

fig = px.line(ocean_carbon, x="year", y="values", labels={"values": "Ocean CO2 Uptake (PgC)"},
              title="Global Yearly Ocean CO2 Uptake")


fig.update_layout(xaxis_title="Year", yaxis_title="PgC", xaxis=dict(tickmode="linear", tick0=2010, dtick=1))


st.plotly_chart(fig)

st.write("1985-2021, the graph above shows how much carbon the ocean has absorbed per year, which sums to around 60 billion kg. The yearly uptake is increasing by around 40 thousand million kg (0.04 Pg) of carbon each year.")

st.write("The impact:")

st.write(":rainbow[Stronger global warming:] with increasing carbon dioxide emissions, ocean carbon uptake is projected to take up a decreasing proportion of these emissions, which would result in stronger global warming3.")
st.write(":rainbow[Ocean acidification:] absorption of carbon dioxide makes the ocean more acidic.Shell formation: calcifying organisms like corals, plankton and shellfish struggle to build shells and skeletons due to higher acidity in the environment.")
st.write(":rainbow[Disruption of marine ecosystems:] lower pH values can interfere with the growth and reproduction of marine organisms and the formation of coral reefs, an important habitat provider for many species – with cascading impacts in the food chain.")
st.write(":rainbow[Shoreline protection:] reduced shoreline protection and increased risk of floods and erosion, caused by coral destruction.")
st.write(":rainbow[Food insecurity and economic losses:] with the loss of biodiversity and weakened habitats people reliant on seafood and coastal zones can suffer.")

###########################################################################################################################
###########################################################################################################################

fig = px.line(ArticSeaExtent, x="year", y="values", labels={"values": "Sea Ice Extent (million km²)"},
              title="Arctic Monthly Mean Sea Ice Extent")


fig.update_layout(xaxis_title="Year", yaxis_title="km²", xaxis=dict(tickmode="linear", tick0=2010, dtick=1))


st.plotly_chart(fig)

st.write("1979-2021 : This represents an enormous loss in sea ice area per decade. From 1979 to 2021, 2.14 million square kilometres of sea ice cover was lost – an area six times the size of Germany.")


st.write("The impact:")

st.write(":rainbow[Feedback loops:] ice reflects more sunlight than the open ocean, so ice melt leads to more warming")
st.write(":rainbow[Ocean circulation systems and the global climate:] the Arctic plays a key role as a regulator of global temperature and in creating ocean currents and circulation")
st.write(":rainbow[Increased freshwater in the Arctic Ocean:] can change the density of the water, consequently modifying the meridional overturning circulation")
st.write(":rainbow[Impacted Arctic ecosystems:] native species can experience stress and even mortality")
st.write(":rainbow[Changing food webs:] warmer temperatures affect the timing of ice melt and bloom of phytoplankton")
st.write(":rainbow[Multifaceted challenges for Arctic communities:] includes risks to food and water security, increase in marine ice hazards, flooding and erosion")
st.write(":rainbow[Geopolitical changes and challenges:] the opening of the Arctic will make strategic regions more accessible, posing issues of security and sovereignty")
st.write(":rainbow[Ocean acidification:] colder temperatures in polar waters enhance solubility of carbon dioxide")
###########################################################################################################################
###########################################################################################################################

fig = px.line(AntarticSeaExtent, x="year", y="values", labels={"values": "Sea Ice Extent (million km²)"},
              title="Antarctic Monthly Mean Sea Ice Extent")


fig.update_layout(xaxis_title="Year", yaxis_title="km²", xaxis=dict(tickmode="linear", tick0=2010, dtick=1))


st.plotly_chart(fig)

st.write("The impact:")

st.write(":rainbow[Ocean circulation and the global climate:] the Antarctic is the key driver of ocean currents and the global circulation system, and plays an important role in the regulation of global temperature")
st.write(":rainbow[Sea level:] global mean sea level can rise with accelerating rates due to ice loss from the Antarctic ice sheet (on land)")
st.write(":rainbow[Freshwater release:] Antarctic mass loss gradually intensifies the freshening of the Southern Ocean (seas around Antarctica) possibly causing changes in water density and changes in ocean circulation")
st.write(":rainbow[Damaged Antarctic ecosystems:] Changes in sea ice cover and temperature affect the distribution and abundance of various species. Disruptions in the food web may cascade throughout the whole ecosystem and result in biodiversity loss")
st.write(":rainbow[Acidification:] polar waters, including those in the Antarctic, are especially susceptible to ocean acidification. The Antarctic is an important carbon pump, absorbing large amounts of carbon dioxide")

######################################################################################

fig = px.line(annual_greenhouse_gas_index, x="Year", y=["CO2", "CH4", "N2O"], line_group="variable",
              labels={"value": "Emission Level", "variable": "Gas"},
              title="Greenhouse Gas Emissions Over Time",
              template="plotly_white")

fig.update_xaxes(tickangle=45)


fig.update_layout(legend=dict(title=None, orientation="h", y=1.1, x=0.5),
                  xaxis=dict(tickmode="linear", tick0=1990, dtick=2))


st.plotly_chart(fig)

st.text("CO2 : carbon dioxide")
st.text("CH4 : Methane")
st.text("N2O: Nitrous oxide")


#######################################################################################################################################


fig = px.line(annual_greenhouse_gas_index, x="Year", y="Total.1",
              labels={"Total.1": "All GHG ppm"},
              title="Greenhouse Gas Emissions Over Time",
              line_shape="linear", line_dash_sequence=["dash"])


fig.update_layout(xaxis_title="Year", yaxis_title="All GHG ppm",
                  xaxis=dict(tickmode="linear", tick0=2010, dtick=1),
                  legend=dict(title=None, orientation="h", y=1.1, x=0.5))


st.plotly_chart(fig)

#############################################################################################################################
#############################################################################################################################

carte = folium.Map(location=[48.8566, 2.3522], zoom_start=1)

for index, row in agriculture_co2.iterrows():
    lat = row['Latitude (average)']
    lon = row['Longitude (average)']

    radius = row['2020'] / 20
    
 
    popup_content = f"<b>{row['Country']}</b><br>" \
                    f"Sector: {row['Sector']}<br>" \
                    f"Gas: {row['Gas']}<br>" \
                    f"Quantity: {row['2020']} {row['Unit']}"  

    
    folium.CircleMarker(location=[lat, lon], radius=radius, popup=popup_content, fill=True).add_to(carte)



st.title("GHG AGRICULTURE SECTOR 2020")
folium_static(carte)

######################################################################################################################################

carte = folium.Map(location=[48.8566, 2.3522], zoom_start=1)

for index, row in bunkerfuels_co2.iterrows():
    lat = row['Latitude (average)']
    lon = row['Longitude (average)']

    radius = row['2020'] / 20
    
 
    popup_content = f"<b>{row['Country']}</b><br>" \
                    f"Sector: {row['Sector']}<br>" \
                    f"Gas: {row['Gas']}<br>" \
                    f"Quantity: {row['2020']} {row['Unit']}"  

    
    folium.CircleMarker(location=[lat, lon], radius=radius, popup=popup_content, fill=True).add_to(carte)

st.title("GHG BUNKERFUELS SECTOR 2020")
folium_static(carte)



