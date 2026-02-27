# IMPORT LIBRARIES 

from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle


plt.rcParams['figure.facecolor'] = '#0B1220'
plt.rcParams['axes.facecolor'] = "#0D1C37"

# DATABASE CONNECTION 

db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "8465050707",
    "database": "Population_db",
    "port": 3306
}

connection_string = (
    f"mysql+pymysql://{db_config['user']}:{db_config['password']}"
    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
)

engine = create_engine(connection_string)

# FETCH DATA 

query = """
SELECT *
FROM population
WHERE Area_Name != 'India'
AND Age = 'All ages'
"""

df = pd.read_sql(query, engine)

#  KPI CALCULATIONS

total_population = df["Total_Population"].sum()
total_males = df["Total_Males"].sum()
total_females = df["Total_Females"].sum()

urban_total = df["Urban_Persons"].sum()
urban_males = df["Urban_Males"].sum()
urban_females = df["Urban_Females"].sum()

rural_total = df["Rural_Persons"].sum()
rural_males = df["Rural_Males"].sum()
rural_females = df["Rural_Females"].sum()

highest_state = df.sort_values("Total_Population", ascending=False).iloc[0]
lowest_state = df.sort_values("Total_Population").iloc[0]

highest_Rural_state = df.sort_values("Rural_Persons", ascending=False).iloc[0]
lowest_Rural_state = df.sort_values("Rural_Persons").iloc[0]

highest_Urban_state = df.sort_values("Urban_Persons", ascending=False).iloc[0]
lowest_Urban_state = df.sort_values("Urban_Persons").iloc[0]

highest_Male_state = df.sort_values("Total_Males", ascending=False).iloc[0]
lowest_Male_state = df.sort_values("Total_Males").iloc[0]

highest_Female_state = df.sort_values("Total_Females", ascending=False).iloc[0]
lowest_Female_state = df.sort_values("Total_Females").iloc[0]

# FIGURE 

fig = plt.figure(figsize=(20,10))
fig.patch.set_facecolor('#0B1220')

# TITLE
fig.text(0.50, 0.95, "Indian Population Analysis",
         ha='center', fontsize=20, color ="#f9f2df", weight='bold')


# KPI CARDS 

kpi_titles = [
    "Total Population", "Total Males", "Total Females",
    "Urban Population", "Urban Males", "Urban Females",
    "Rural Population", "Rural Males", "Rural Females"
]

kpi_values = [
    total_population, total_males, total_females,
    urban_total, urban_males, urban_females,
    rural_total, rural_males, rural_females
]

kpi_colors = [
    "#FFFFFF", "#4FC3F7", "#F06292",
    "#81C784", "#BA68C8", "#FFD54F",
    "#64B5F6", "#4DB6AC", "#AED581"
]

x_start = 0.03
for i in range(9):
    fig.add_artist(Rectangle((x_start + i*0.105, 0.86),
                             0.095, 0.07,
                             facecolor="#111B2E",
                             edgecolor="#1F2A44"))

    fig.text(x_start + i*0.105 + 0.047,
             0.90,
             f"{round(kpi_values[i]/1000000)}M",
             ha='center',
             fontsize=15,
             color=kpi_colors[i],
             weight='bold')

    fig.text(x_start + i*0.105 + 0.047,
             0.875,
             kpi_titles[i],
             ha='center',
             fontsize=8,
             color='white')


# FIXED SIZE INFO BOX

def draw_info_box(y_pos, title, state, value, value_color):

    box_x = 0.026
    box_width = 0.16
    box_height = 0.06

    fig.add_artist(Rectangle(
        (box_x, y_pos),
        box_width,
        box_height,
        facecolor="#1E1E1E",
        edgecolor="#FFD54F",
        linewidth=1.2
    ))

    fig.text(box_x + 0.01,
             y_pos + box_height - 0.02,
             title,
             fontsize=8,
             color="white",
             weight='bold')

    fig.text(box_x + 0.01,
             y_pos + 0.018,
             state,
             fontsize=8,
             color=value_color)

    fig.text(box_x + box_width - 0.01,
             y_pos + 0.018,
             f"{value:,}",
             fontsize=8,
             color=value_color,
             ha='right',
             weight='bold')


# HIGHEST / LOWEST INFO 

draw_info_box(0.74, "Highest Population State", highest_state['Area_Name'], highest_state['Total_Population'], "#0FCF2F")
draw_info_box(0.67, "Lowest Population State", lowest_state['Area_Name'], lowest_state['Total_Population'], "#CC0E0E")
draw_info_box(0.60, "Highest Rural Population State", highest_Rural_state['Area_Name'], highest_Rural_state['Rural_Persons'], "#0FCF2F")
draw_info_box(0.53, "Lowest Rural Population State", lowest_Rural_state['Area_Name'], lowest_Rural_state['Rural_Persons'], "#CC0E0E")
draw_info_box(0.46, "Highest Urban Population State", highest_Urban_state['Area_Name'], highest_Urban_state['Urban_Persons'], "#0FCF2F")
draw_info_box(0.39, "Lowest Urban Population State", lowest_Urban_state['Area_Name'], lowest_Urban_state['Urban_Persons'], "#CC0E0E")
draw_info_box(0.32, "Highest Male Population State", highest_Male_state['Area_Name'], highest_Male_state['Total_Males'], "#0FCF2F")
draw_info_box(0.25, "Lowest Male Population State", lowest_Male_state['Area_Name'], lowest_Male_state['Total_Males'], "#CC0E0E")
draw_info_box(0.18, "Highest Female Population State", highest_Female_state['Area_Name'], highest_Female_state['Total_Females'], "#0FCF2F")
draw_info_box(0.11, "Lowest Female Population State", lowest_Female_state['Area_Name'], lowest_Female_state['Total_Females'], "#CC0E0E")


# GRID SECTION 

gs = fig.add_gridspec(
    2, 3,
    left=0.32,
    right=0.96,
    bottom=0.10,
    top=0.78,
    wspace=0.48,
    hspace=0.44
)

# TOP 5 STATES 

ax1 = fig.add_subplot(gs[0,0])
top5 = df.sort_values("Total_Population", ascending=False).head(5)

bars = ax1.barh(top5["Area_Name"], top5["Total_Population"],
                color="#42A5F5",height=0.90,edgecolor='white')

ax1.set_title("Top 5 States by Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')
ax1.tick_params(colors='white')


for bar in bars:
    ax1.text(
        bar.get_width() - (bar.get_width() * 0.05),
        bar.get_y() + bar.get_height() / 2,
        f"{int(bar.get_width()):,}",
        va='center',
        ha='right', 
        color='white',
        fontsize=8,
        weight='bold'
    )



# URBAN 

ax2 = fig.add_subplot(gs[0,1])
urban_data = [urban_total, urban_males, urban_females]
labels_u = ["Urban Total", "Urban Males", "Urban Females"]

bars2 = ax2.barh(labels_u, urban_data, color="#66BB6A",edgecolor='white')
ax2.set_title("Urban Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')
ax2.tick_params(colors='white')


for bar in bars2:
    ax2.text(bar.get_width(),
             bar.get_y() + bar.get_height()/2,
             f"{int(bar.get_width()):,}",
             va='center',
             ha='right',
             color='white',
             fontsize=8,
             weight='bold')
    


# RURAL 

ax3 = fig.add_subplot(gs[0,2])
rural_data = [rural_total, rural_males, rural_females]
labels_r = ["Rural Total", "Rural Males", "Rural Females"]

bars3 = ax3.barh(labels_r, rural_data, color="#FF7043",edgecolor='white')
ax3.set_title("Rural Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')
ax3.tick_params(colors='white')

for bar in bars3:
    ax3.text(bar.get_width(),
             bar.get_y() + bar.get_height()/2,
             f"{int(bar.get_width()):,}",
             va='center',
             ha='right',
             color='white',
             weight='bold',
             fontsize=8)

# Urban and Rural DONUT
ax4 = fig.add_subplot(gs[1,0])

ax4.pie(
    [rural_total, urban_total],
    labels=["Rural Population", "Urban Population"],
    autopct='%1.1f%%',
    colors=["#29B6F6", "#FF7043"],
    textprops={'color':'white'}
)

centre_circle = plt.Circle((0,0), 0.65, fc='#0B1220')
ax4.add_artist(centre_circle)

ax4.set_title("Urban vs Rural Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')


# Total Population

ax5 = fig.add_subplot(gs[1,1])
male_data = [total_population, urban_total, rural_total]
labels_m = ["Total", "Urban", "Rural"]

bars5 = ax5.bar(labels_m, male_data, color="#42A5F5",edgecolor='white')
ax5.set_title("Total Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')
ax5.tick_params(colors='white')

for bar in bars5:
    ax5.text(bar.get_x() + bar.get_width()/2,
             bar.get_height(),
             f"{int(bar.get_height()):,}",
             ha='center',
             va='bottom',
             color='white',
             weight='bold',
             fontsize=8)

#  Male Population

ax6 = fig.add_subplot(gs[1,2])
ax6.pie([urban_males, rural_males,rural_females,urban_females],
        labels=["Urban Males", "Rural Males", "Rural Females", "Urban Females"],
        autopct='%1.1f%%',
        colors=["#66BB6A", "#FFA726","#1B7EE8","#F1396D"],
        textprops={'color':'white'})

ax6.set_title("Male and Female Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')

plt.show()