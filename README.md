India Population Analysis

Project Source:  https://censusindia.gov.in/datagov/C-13/DDW-0000C-13.xls

 
Excel:
Excel is used for
•	Viewing raw dataset
•	Cleaning data
•	Creating columns like:
1.	Gender Ratio
2.	Urban %
3.	Rural %


Changes done in Excel:
•	Removed the Dist code
•	Rename the Area_Name. i.e., example State – Himachal Prades(02) to S-HP (02)
•	Gave proper name to every heading. ex: Area name to Area_Name
•	Added extra column Age_Category to differentiate that is it in All_ages or Age_wise
•	Added extra column Gender Ratio i.e., (Total_Females/Total_Males) * 100
•	Added extra column Urban_Percentage i.e., (Urban_Persons / Total_Population) * 100
•	Added extra column Rural_Percentage i.e., (Rural_Persons / Total_Population) * 100  


 



MySql:
•	Storing population dataset
•	Filtering data
•	Fetching only required records

Changes done in MySql:
•	Created the database Population_DB and used it
•	After that create the table called Population and import the all the details from the Excel Sheet

 

•	After checking the count from the table -- select count(*) from Population
 
•	Checked the values 
 Total Population (India)
select sum(Total_Population) as Total_Population from Population 
where age != "All ages"
and Area_Name != "India"
Total Population got 1210854971

-- Total Males
select sum(Total_Males) as Total_Males from Population 
where age != "All ages"
and Area_Name != "India"
-- 623270258

-- Total Females
select sum(Total_Females) as Total_Females from Population 
where age != "All ages"
and Area_Name != "India"
-- 587584713

-- Urban Population
select sum(Urban_Persons) as Urban_Population from Population 
where age != "All ages"
and Area_Name = "India"
-- 377106125

-- Urban Males
select sum(Urban_Males) as Urban_Males from Population 
where age != "All ages"
and Area_Name = "India"
-- 195489200

-- Urban Females
select sum(Urban_Females) as Urban_Females from Population 
where age != "All ages"
and Area_Name = "India"
-- 181616925

-- Rural Population
select sum(Rural_Persons) as Rural_Population from Population 
where age != "All ages"
and Area_Name = "India"
-- 833748852


-- Rural Male Population
select sum(Rural_Males) as Rural_Males from Population 
where age != "All ages"
and Area_Name = "India"
-- 427781058

-- Rural Female Population
select sum(Rural_Females) as Rural_Females from Population 
where age != "All ages"
and Area_Name = "India"
-- 405967794


Calculated the total Highest & lowest stated based on the requirements using below formulas
-- Highest Population State
select Area_Name  as Highest_Population_State,Total_Population from Population
where Area_Name != "India"
and Age = "All ages" 
order by Total_Population desc
limit 1
-- State - UTTAR PRADESH (09)	199812341

-- Lowest Population state
select Area_Name  as Lowest_Population_State,Total_Population from Population
where Area_Name != "India"
and Age = "All ages" 
order by Total_Population 
limit 1
-- State - LAKSHADWEEP (31)	64473

-- Highest Male Population State
select Area_Name  as Highest_Male_Population_State,Total_Males from Population
where Area_Name != "India"
and Age = "All ages" 
order by Total_Males desc
limit 1
State - UTTAR PRADESH (09)	104480510

-- Lowest Male Population State
select Area_Name  as Lowest_Population_State,Total_Males from Population
where Area_Name != "India"
and Age = "All ages" 
order by Total_Males
limit 1
-- State - LAKSHADWEEP (31)	33123



-- Highest Female Population State
select Area_Name  as Highest_Female_Population_State,Total_Females from Population
where Area_Name != "India"
and Age = "All ages" 
order by Total_Females desc
limit 1
State - UTTAR PRADESH (09)	95331831
-- Lowest Female Population State
select Area_Name  as Lowest_Female_Population_State,Total_Females from Population
where Area_Name != "India"
and Age = "All ages" 
order by Total_Females
limit 1
-- State - LAKSHADWEEP (31)	31350
-- Highest Rural Population State
select Area_Name  as Highest_Rural_Population_State,Rural_Persons from Population
where Area_Name != "India"
and Age = "All ages" 
order by Rural_Persons desc
limit 1
-- State - UTTAR PRADESH (09)	155317278
-- Lowest Rural Population state
select Area_Name  as Lowest_Rural_Population_State,Rural_Persons from Population
where Area_Name != "India"
and Age = "All ages" 
order by Rural_Persons 
limit 1
-- State - LAKSHADWEEP (31)	14141

-- Highest Rural Male Population State
select Area_Name  as Highest_Rural_Male_Population_State,Rural_Males from Population
where Area_Name != "India"
and Age = "All ages" 
order by Rural_Males desc
limit 1
-- State - UTTAR PRADESH (09)	80992995

-- Lowest Rural Male Population State
select Area_Name  as Lowest_Rural_Male_Population_State,Rural_Males from Population
where Area_Name != "India"
and Age = "All ages" 
order by Rural_Males 
limit 1
-- State - LAKSHADWEEP (31)	7243

-- Highest Rural Female Population State
select Area_Name  as Highest_Rural_Female_Population_State,Rural_Females from Population
where Area_Name != "India"
and Age = "All ages" 
order by Rural_Females desc
limit 1
-- State - UTTAR PRADESH (09)	74324283

-- Lowest Rural Female Population State
select Area_Name  as Lowest_Rural_Female_Population_State,Rural_Females from Population
where Area_Name != "India"
and Age = "All ages" 
order by Rural_Females 
limit 1
-- State - LAKSHADWEEP (31)	6898

-- Highest Urban Population State
select Area_Name  as Highest_Urban_Population_State,Urban_Persons from Population
where Area_Name != "India"
and Age = "All ages" 
order by Urban_Persons desc
limit 1
-- State - MAHARASHTRA (27)	50818259

-- Lowest Urban Population state
select Area_Name  as Highest_Urban_Population_State,Urban_Persons from Population
where Area_Name != "India"
and Age = "All ages" 
order by Urban_Persons 
limit 1
-- State - LAKSHADWEEP (31)	50332

-- Highest Urban Male Population State
select Area_Name  as Highest_Urban_Male_Population_State,Urban_Males from Population
where Area_Name != "India"
and Age = "All ages" 
order by Urban_Males desc
limit 1
-- State - MAHARASHTRA (27)	26704022

-- Lowest Urban Male Population State
select Area_Name  as Lowest_Urban_Male_Population_State,Urban_Males from Population
where Area_Name != "India"
and Age = "All ages" 
order by Urban_Males 
limit 1
-- State - LAKSHADWEEP (31)	25880


-- Highest Urban Female Population State
select Area_Name  as Highest_Urban_Female_Population_State,Urban_Females from Population
where Area_Name != "India"
and Age = "All ages" 
order by Urban_Females desc
limit 1
-- State - MAHARASHTRA (27)	24114237

-- Lowest Urban Female Population State
select Area_Name  as Lowest_Urban_Female_Population_State,Urban_Females from Population
where Area_Name != "India"
and Age = "All ages" 
order by Urban_Females
limit 1
-- State - LAKSHADWEEP (31)	24452













Python: 
•	Connecting to database (sqlalchemy)
•	Reading data (pandas)
•	Performing calculations (KPI metrics)
•	Creating dashboard (matplotlib)
•	Custom UI design (KPI cards, info boxes)


•	Imported all the libraries
•	# IMPORT LIBRARIES 
•	
•	from sqlalchemy import create_engine
•	import pandas as pd
•	import matplotlib.pyplot as plt
•	import seaborn as sns
•	from matplotlib.patches import Rectangle


•	Connected to the database
•	# DATABASE CONNECTION 
•	
•	db_config = {
•	    "host": "127.0.0.1",
•	    "user": "root",
•	    "password": "8465050707",
•	    "database": "Population_db",
•	    "port": 3306
•	}
•	
•	connection_string = (
•	    f"mysql+pymysql://{db_config['user']}:{db_config['password']}"
•	    f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
•	)
•	
•	engine = create_engine(connection_string)
•	


•	Fetching the data
•	
•	# FETCH DATA 
•	
•	query = """
•	SELECT *
•	FROM population
•	WHERE Area_Name != 'India'
•	AND Age = 'All ages'
•	"""
•	
•	df = pd.read_sql(query, engine)


•	All the KPI calculations

•	#  KPI CALCULATIONS
•	
•	total_population = df["Total_Population"].sum()
•	total_males = df["Total_Males"].sum()
•	total_females = df["Total_Females"].sum()
•	
•	urban_total = df["Urban_Persons"].sum()
•	urban_males = df["Urban_Males"].sum()
•	urban_females = df["Urban_Females"].sum()
•	
•	rural_total = df["Rural_Persons"].sum()
•	rural_males = df["Rural_Males"].sum()
•	rural_females = df["Rural_Females"].sum()
•	highest_state = df.sort_values("Total_Population", ascending=False).iloc[0]
•	lowest_state = df.sort_values("Total_Population").iloc[0]
•	
•	highest_Rural_state = df.sort_values("Rural_Persons", ascending=False).iloc[0]
•	lowest_Rural_state = df.sort_values("Rural_Persons").iloc[0]
•	
•	highest_Urban_state = df.sort_values("Urban_Persons", ascending=False).iloc[0]
•	lowest_Urban_state = df.sort_values("Urban_Persons").iloc[0]
•	
•	highest_Male_state = df.sort_values("Total_Males", ascending=False).iloc[0]
•	lowest_Male_state = df.sort_values("Total_Males").iloc[0]
•	
•	highest_Female_state = df.sort_values("Total_Females", ascending=False).iloc[0]
•	lowest_Female_state = df.sort_values("Total_Females").iloc[0]


•	Added all KPI cards
•	# KPI CARDS 
•	
•	kpi_titles = [
•	    "Total Population", "Total Males", "Total Females",
•	    "Urban Population", "Urban Males", "Urban Females",
•	    "Rural Population", "Rural Males", "Rural Females"
•	]
•	
•	kpi_values = [
•	    total_population, total_males, total_females,
•	    urban_total, urban_males, urban_females,
•	    rural_total, rural_males, rural_females
•	]
•	
•	kpi_colors = [
•	    "#FFFFFF", "#4FC3F7", "#F06292",
•	    "#81C784", "#BA68C8", "#FFD54F",
•	    "#64B5F6", "#4DB6AC", "#AED581"
•	]
•	
•	x_start = 0.03
•	for i in range(9):
•	    fig.add_artist(Rectangle((x_start + i*0.105, 0.86),
•	                             0.095, 0.07,
•	                             facecolor="#111B2E",
•	                             edgecolor="#1F2A44"))
•	
•	    fig.text(x_start + i*0.105 + 0.047,
•	             0.90,
•	             f"{round(kpi_values[i]/1000000)}M",
•	             ha='center',
•	             fontsize=15,
•	             color=kpi_colors[i],
•	             weight='bold')
•	
•	    fig.text(x_start + i*0.105 + 0.047,
•	             0.875,
•	             kpi_titles[i],
•	             ha='center',
•	             fontsize=8,
•	             color='white')
•	


•	Sizes of all boxes for Highest and lowest States
•	# FIXED SIZE INFO BOX
•	
•	def draw_info_box(y_pos, title, state, value, value_color):
•	
•	    box_x = 0.026
•	    box_width = 0.16
•	    box_height = 0.06
•	
•	    fig.add_artist(Rectangle(
•	        (box_x, y_pos),
•	        box_width,
•	        box_height,
•	        facecolor="#1E1E1E",
•	        edgecolor="#FFD54F",
•	        linewidth=1.2
•	    ))
•	
•	    fig.text(box_x + 0.01,
•	             y_pos + box_height - 0.02,
•	             title,
•	             fontsize=8,
•	             color="white",
•	             weight='bold')
•	
•	    fig.text(box_x + 0.01,
•	             y_pos + 0.018,
•	             state,
•	             fontsize=8,
•	             color=value_color)
•	
•	    fig.text(box_x + box_width - 0.01,
•	             y_pos + 0.018,
•	             f"{value:,}",
•	             fontsize=8,
•	             color=value_color,
•	             ha='right',
•	             weight='bold')

•	Values of all boxes

•	# HIGHEST / LOWEST INFO 
•	
•	draw_info_box(0.74, "Highest Population State", highest_state['Area_Name'], highest_state['Total_Population'], "#0FCF2F")
•	draw_info_box(0.67, "Lowest Population State", lowest_state['Area_Name'], lowest_state['Total_Population'], "#CC0E0E")
•	draw_info_box(0.60, "Highest Rural Population State", highest_Rural_state['Area_Name'], highest_Rural_state['Rural_Persons'], "#0FCF2F")
•	draw_info_box(0.53, "Lowest Rural Population State", lowest_Rural_state['Area_Name'], lowest_Rural_state['Rural_Persons'], "#CC0E0E")
•	draw_info_box(0.46, "Highest Urban Population State", highest_Urban_state['Area_Name'], highest_Urban_state['Urban_Persons'], "#0FCF2F")
•	draw_info_box(0.39, "Lowest Urban Population State", lowest_Urban_state['Area_Name'], lowest_Urban_state['Urban_Persons'], "#CC0E0E")
•	draw_info_box(0.32, "Highest Male Population State", highest_Male_state['Area_Name'], highest_Male_state['Total_Males'], "#0FCF2F")
•	draw_info_box(0.25, "Lowest Male Population State", lowest_Male_state['Area_Name'], lowest_Male_state['Total_Males'], "#CC0E0E")
•	draw_info_box(0.18, "Highest Female Population State", highest_Female_state['Area_Name'], highest_Female_state['Total_Females'], "#0FCF2F")
•	draw_info_box(0.11, "Lowest Female Population State", lowest_Female_state['Area_Name'], lowest_Female_state['Total_Females'], "#CC0E0E")



•	Grid Layout section
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

•	For top 5 States chart (Horizontal Bar Chart)
•	# TOP 5 STATES 
•	
•	ax1 = fig.add_subplot(gs[0,0])
•	top5 = df.sort_values("Total_Population", ascending=False).head(5)
•	
•	bars = ax1.barh(top5["Area_Name"], top5["Total_Population"],
•	                color="#42A5F5",height=0.90,edgecolor='white')
•	
•	ax1.set_title("Top 5 States by Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')
•	ax1.tick_params(colors='white')
•	
•	for bar in bars:
•	    ax1.text(
•	        bar.get_width() - (bar.get_width() * 0.05),
•	        bar.get_y() + bar.get_height() / 2,
•	        f"{int(bar.get_width()):,}",
•	        va='center',
•	        ha='right', 
•	        color='white',
•	        fontsize=8,
•	        weight='bold'
•	    )


•	For Urban Area Chart (Horizontal Bar Chart)
•	# URBAN 
•	
•	ax2 = fig.add_subplot(gs[0,1])
•	urban_data = [urban_total, urban_males, urban_females]
•	labels_u = ["Urban Total", "Urban Males", "Urban Females"]
•	
•	bars2 = ax2.barh(labels_u, urban_data, color="#66BB6A",edgecolor='white')
•	ax2.set_title("Urban Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')
•	ax2.tick_params(colors='white')
•	
•	for bar in bars2:
•	    ax2.text(bar.get_width(),
•	             bar.get_y() + bar.get_height()/2,
•	             f"{int(bar.get_width()):,}",
•	             va='center',
•	             ha='right',
•	             color='white',
•	             fontsize=8,
•	             weight='bold')    


•	For Rural Area Chart (Horizontal Bar Chart)
•	# RURAL 
•	
•	ax3 = fig.add_subplot(gs[0,2])
•	rural_data = [rural_total, rural_males, rural_females]
•	labels_r = ["Rural Total", "Rural Males", "Rural Females"]
•	
•	bars3 = ax3.barh(labels_r, rural_data, color="#FF7043",edgecolor='white')
•	ax3.set_title("Rural Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')
•	ax3.tick_params(colors='white')
•	
•	for bar in bars3:
•	    ax3.text(bar.get_width(),
•	             bar.get_y() + bar.get_height()/2,
•	             f"{int(bar.get_width()):,}",
•	             va='center',
•	             ha='right',
•	             color='white',
•	             weight='bold',
•	             fontsize=8)






•	For Urban and Rural chart (Donut chart)

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

•	For Total Population chart (Vertical Bar Chart)
•	# Total Population
•	
•	ax5 = fig.add_subplot(gs[1,1])
•	male_data = [total_population, urban_total, rural_total]
•	labels_m = ["Total", "Urban", "Rural"]
•	
•	bars5 = ax5.bar(labels_m, male_data, color="#42A5F5",edgecolor='white')
•	ax5.set_title("Total Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')
•	ax5.tick_params(colors='white')
•	
•	for bar in bars5:
•	    ax5.text(bar.get_x() + bar.get_width()/2,
•	             bar.get_height(),
•	             f"{int(bar.get_height()):,}",
•	             ha='center',
•	             va='bottom',
•	             color='white',
•	             weight='bold',
•	             fontsize=8)





•	For Male and Female Population chart (Pie Chart)

#  Male and Female Population

ax6 = fig.add_subplot(gs[1,2])
ax6.pie([urban_males, rural_males,rural_females,urban_females],
        labels=["Urban Males", "Rural Males", "Rural Females", "Urban Females"],
        autopct='%1.1f%%',
        colors=["#66BB6A", "#FFA726","#1B7EE8","#F1396D"],
        textprops={'color':'white'})

ax6.set_title("Male and Female Population", color="#71DC7F",fontsize=12, pad=12,fontweight='bold')

Final Dashboard:

 







Highest and Lowest Population states:
Total population
Highest population state is Uttar Pradesh with a total population of 199,812,341.
Lowest population state is Lakshadweep with a total population of 64,473.
Male population
Highest male population is in Uttar Pradesh with 104,480,510 males.
Lowest male population is in Lakshadweep with 33,123 males.
Female population
Highest female population is in Uttar Pradesh with 95,331,831 females.
Lowest female population is in Lakshadweep with 31,350 females.
Rural population
Highest rural population is in Uttar Pradesh with 155,317,278 rural population.
Lowest rural population is in Lakshadweep with 14,141 rural population.
Urban population
Highest urban population is in Maharashtra with 50,818,259 urban population.
Lowest urban population is in Lakshadweep with 50,332 urban population.



Insights and Key Findings
Demographic Structure
•	The population is predominantly concentrated in the younger and working-age groups (0–59 years).
•	The working-age population (15–59 years) represents the largest share of the total population.
•	The child population (0–14 years) forms a significant dependent segment.
•	The elderly population (60 years and above) is comparatively smaller but shows a gradual increasing trend.
Gender Distribution
•	The male population is higher than the female population across most regions.
•	Gender imbalance is observed across multiple age groups.
•	Urban regions show a higher level of gender imbalance compared to rural regions.
Rural and Urban Population Distribution
•	A majority of the population resides in rural areas.
•	Urban areas account for a smaller proportion of the population but are more densely populated.
•	Urban regions experience higher population pressure on infrastructure.
Urbanization and Migration Trends
•	Urban areas have a higher concentration of the working-age population.
•	The male population is more dominant in urban regions due to migration.
•	Migration from rural to urban areas is primarily driven by employment opportunities.
Policy and Planning Implications
•	The high proportion of the working-age population highlights the need for employment generation and skill development initiatives.
•	Rural population dominance emphasizes the importance of strengthening rural infrastructure and healthcare facilities.
•	Urban population growth calls for planned and sustainable urban development.
•	Gender imbalance indicates the need for focused gender equality and welfare programs.



Summary of Key Observations
•	The population structure reflects a young demographic profile.
•	Rural areas continue to accommodate the majority of the population.
•	Urban growth is largely influenced by migration.
•	Gender imbalance remains a significant demographic challenge.
•	Population data plays a critical role in evidence-based planning and policy formulation.
